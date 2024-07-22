# This script is part of the first bit of reverse engennering of the
# DVAPTool, reading the technical guide and attempting to confirm writes
#  and returns from the device.

import serial
import time
import binascii

# Set up the serial connection (e.g., COM1 on Windows or /dev/ttyUSB0 on Linux)
port = '/dev/ttyUSB0'
baudrate = 230400

# Open the serial port in read-only mode (no writes)
ser = serial.Serial(port, baudrate, timeout=1)

try:
    while True:
        # Read data from the serial port
        data = ser.read()
        #data = ser.readline()
        if data:
                hex_data = binascii.hexlify(data)
                print(f"Received: {hex_data}")  # Print the received data in hexadecimal format
        if data:
            print(f"Received: {data.decode()}")  # Decode and print the received data

finally:
    # Close the serial port when done
    ser.close()
