In this section I am going to store the scripts that I use for reading data out of the Sensor Bridge connected to the SEN55.

I am making use of these devices in a machine running ArchLinux. 

For this to work, I had to ensure that the device was loaded using the ftdi_sio driver
To do so, I had to take the following two steps:

Load the ftdi_sio module with:

sudo modprobe ftdi_sio

And then assign the driver to the device:

echo "0403 7168" | sudo tee /sys/bus/usb-serial/drivers/ftdi_sio/new_id



The commands to be used can be found in Table 12 of the SEN5x datasheet.

Some practically useful I2C commands:

0x00 0x20 : Start Measurement
0x02 0x02 : Read Data-Ready Flag
0x03 0xc4 : Read Measured Values



Please refer to  SEN5x datasheet for additional commands: https://sensirion.com/media/documents/6791EFA0/62A1F68F/Sensirion_Datasheet_Environmental_Node_SEN5x.pdf

Refer to section  6.1.5 to see the structure of the response to the "Read Measured Values" command.




So far, the scripts are:

# print_values.py

This is a minimal script that will fetch the measurement values, store them into a dictionary, and print the values to the console. This structure can serve as the basis for more complicated scripts. 

# log_data.py

This script allows you to write logged data into a postgresql database
