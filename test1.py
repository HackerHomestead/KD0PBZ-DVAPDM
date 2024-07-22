# This script is the gennis of the tool and can be run to confirm
# The DVAP is connected and working correctly i.e. we can talk to it
# While it is not conversational it dose prove that the technical guide
#  is correct and what is a refernce for how to communicate. 
# 
# Next steps would be to actually init the device with RX/TX frequancies
#  and tx or rx something.


import serial
import struct

# Set up the serial connection
port = '/dev/ttyUSB0'  # Replace with your desired port (e.g. /dev/ttyUSB0, COM1, etc.)
baudrate = 230400
ser = serial.Serial(port, baudrate)

print("Sending ... ")
# Write the array of hex values to the serial device

# Make it say DVAP Dongle (ASCII String)
#data = "04200100" # [04][20] [01][00]

# Print Serial number (ASCII String)
data = "04200200" # [04][20] [02][00]

bytes_object = bytes.fromhex(data)
print(data)
ser.write(bytes_object)

# Read and print out any incoming data from the serial port
print("Listening...")
while True:
    try:
        #incoming_data = ser.read(1, timeout=0.1)  # Read up to 1 byte with a 100ms timeout
        incoming_data = ser.read()  # Read up to 1 byte with a 100ms timeout
        if incoming_data:
            print(f"Received: {incoming_data.hex()}")
    except serial.SerialTimeoutException:
        print("Break the loop")
        break  # No more data available
