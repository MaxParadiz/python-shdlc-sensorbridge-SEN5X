import time
from sensirion_shdlc_driver import ShdlcSerialPort, ShdlcConnection
from sensirion_shdlc_sensorbridge import SensorBridgePort, SensorBridgeShdlcDevice



data = {}
data["PM1"]         = {'value':0, 'unit' :  'ug/m3'} 
data["PM2.5"]       = {'value':0, 'unit' :  'ug/m3'}  
data["PM4"]         = {'value':0, 'unit' :  'ug/m3'} 
data["PM10"]        = {'value':0, 'unit' :  'ug/m3'} 
data["Humidity"]    = {'value':0, 'unit' :  '%'} 
data["Temperature"] = {'value':0, 'unit' :  'C'} 
data["VOC"]         = {'value':0, 'unit' :  'VOC Index'} 
data["NOx"]         = {'value':0, 'unit' :  'NOx Index'} 

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
    print("-----------------------------------------\n\n\n")
    while True:
        rx_data = device.transceive_i2c(
            SensorBridgePort.ONE, address=0x69, tx_data=[0x02, 0x02], # 0x02 0x02 -> Read Data-Ready Flag Command
            rx_length=6, timeout_us=100e3)
        if rx_data[1] == 1:
            rx_data = device.transceive_i2c(
                SensorBridgePort.ONE, address=0x69, tx_data=[0x03, 0xc4], # 0x03 0xc4 -> Read Measured Values Command
                rx_length=24, timeout_us=100e3)
            data["PM1"]['value'] = int(rx_data[0:2].hex(),16)/10
            data["PM2.5"]['value'] = int(rx_data[3:5].hex(),16)/10
            data["PM4"]['value'] = int(rx_data[6:8].hex(),16)/10
            data["PM10"]['value'] = int(rx_data[9:11].hex(),16)/10
            data["Humidity"]['value'] = int(rx_data[12:14].hex(),16)/100
            data["Temperature"]['value'] = int(rx_data[15:17].hex(),16)/200
            data["VOC"]['value'] = int(rx_data[18:20].hex(),16)/10
            data["NOx"]['value'] = int(rx_data[21:23].hex(),16)/10
            for d in data:
                print(f"{d}: {data[d]['value']} {data[d]['unit']}")
            print("-----------------------------------------\n\n\n")



