import psycopg2
from psycopg2 import pool
import time
from sensirion_shdlc_driver import ShdlcSerialPort, ShdlcConnection
from sensirion_shdlc_sensorbridge import SensorBridgePort, SensorBridgeShdlcDevice

# Replace these variables with your actual database connection details

db_params = {
    "database": "sensors",
    "user": "sensors",
    "password": "your_password",
    "host": "localhost",
    "port": "5432"
}



data = {}
data["PM1"]         = {'value':0, 'unit' :  'ug/m3'} 
data["PM2.5"]       = {'value':0, 'unit' :  'ug/m3'}  
data["PM4"]         = {'value':0, 'unit' :  'ug/m3'} 
data["PM10"]        = {'value':0, 'unit' :  'ug/m3'} 
data["Humidity"]    = {'value':0, 'unit' :  '%'} 
data["Temperature"] = {'value':0, 'unit' :  'C'} 
data["VOC"]         = {'value':0, 'unit' :  'VOC Index'} 
data["NOx"]         = {'value':0, 'unit' :  'NOx Index'} 

# SQL statement for inserting data

def log_sen55(values):
    insert_sql = """
    INSERT INTO sen55 (temperature, humidity, pm1, pm2_5, pm4, pm10, voc, nox) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """
    conn = conn_pool.getconn()
    try:
        with conn.cursor() as curs:
            curs.execute(insert_sql, values)
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        conn_pool.putconn(conn)



# Initialize the connection pool
conn_pool = pool.SimpleConnectionPool(minconn=1, maxconn=10, **db_params)

with ShdlcSerialPort(port='/dev/ttyUSB0', baudrate=460800) as port:
    device = SensorBridgeShdlcDevice(ShdlcConnection(port), slave_address=0)
    # Print some device information
    print("Version: {}".format(device.get_version()))
    print("Product Name: {}".format(device.get_product_name()))
    print("Serial Number: {}".format(device.get_serial_number()))
    # Enable port 1 with an I2C frequency of 100kHz and a voltage of 5V
    device.set_i2c_frequency(SensorBridgePort.ONE, frequency=100e3)
    device.set_supply_voltage(SensorBridgePort.ONE, voltage=5)
    device.switch_supply_on(SensorBridgePort.ONE)
    # Perform synchronous I2C transceive on port 1
    rx_data = device.transceive_i2c(
        SensorBridgePort.ONE, address=0x69, tx_data=[0x00, 0x21],  # 0x00 0x21 -> Start Measurement Command
        rx_length=3, timeout_us=100e3)
    print("Data logging has started")
    while True:
        rx_data = device.transceive_i2c(
            SensorBridgePort.ONE, address=0x69, tx_data=[0x02, 0x02], # 0x02 0x02 -> Read Data-Ready Flag Command
            rx_length=6, timeout_us=100e3)
        if rx_data[1] == 1:
            rx_data = device.transceive_i2c(
                SensorBridgePort.ONE, address=0x69, tx_data=[0x03, 0xc4], # 0x03 0xc4 -> Read Measured Values Command
                rx_length=24, timeout_us=100e3)
            PM1 = int(rx_data[0:2].hex(),16)/10
            PM2_5 = int(rx_data[3:5].hex(),16)/10
            PM4 = int(rx_data[6:8].hex(),16)/10
            PM10 = int(rx_data[9:11].hex(),16)/10
            humidity = int(rx_data[12:14].hex(),16)/100
            temperature = int(rx_data[15:17].hex(),16)/200
            VOC = int(rx_data[18:20].hex(),16)/10
            NOx = int(rx_data[21:23].hex(),16)/10
            values = (temperature, humidity, PM1, PM2_5, PM4, PM10, VOC, NOx)
            log_sen55(values)
            print(values)





