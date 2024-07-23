# This script is the gennis of the tool and can be run to confirm
# The DVAP is connected and working correctly i.e. we can talk to it
# While it is not conversational it dose prove that the technical guide
#  is correct and what is a refernce for how to communicate. 
# 
# Next steps would be to actually init the device with RX/TX frequancies
#  and tx or rx something.

import sys
import serial
import struct

# Set up the serial connection
port = '/dev/ttyUSB0'  # Replace with your desired port (e.g. /dev/ttyUSB0, COM1, etc.)
baudrate = 230400
ser = serial.Serial(port, baudrate, timeout=1)

print("Sending ... ")
# Write the array of hex values to the serial device

# Make it say DVAP Dongle (ASCII String)
data = "04200100" # [04][20] [01][00]

# Request Status / Error
data = "04200500" # [04][20] [05][00] 

# Modulation Type
data = "0500280001" # Set GMSK Mode

# Set RX/TX to 146.520
data = "08002002C0B7BB08" # LSB 0x08BBB7C0

# Set Run State
# 0500180000 # DVAP in inactive idle state
# 0500180001 # DVAP in active state

# Will get this when RX is on (1) when TX is on
# 0520180100

bytes_object = bytes.fromhex(data)
print(data)
ser.write(bytes_object)

# Read and print out any incoming data from the serial port
print("Listening...")
while True:
    try:
        rx = True
        while rx:
            incoming_data = ser.read(1)  # Read up to 1 byte with a 100ms timeout
            if incoming_data:
                print(f"{incoming_data.hex()} ", end='')
                rx = True
            else:
                print("")
                rx = False

        #Ok next step is to read until the buffer is empty

        data = input("HEX:")
        if len(data) > 0:
            if data == "quit":
                print("Exiting ... ")
                sys.exit(0)
            bytes_object = bytes.fromhex(data)
            #print("SND:", data)
            ser.write(bytes_object)

        
    except serial.SerialTimeoutException:
        print("Break the loop")
        break  # No more data available
