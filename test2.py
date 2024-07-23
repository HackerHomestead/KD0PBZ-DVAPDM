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

CMD_INDEX = {
        "Request Name":                 "04200100",
        "Request Status / Error":       "04200500",
        "Request Status":               "04200500",
        "Set GMSK Mode" :               "0500280001",
        "Put into Normal Mode":         "05002a0000",
        "Put into CW Test Mode":        "05002a0001",
        "Put into Deviation Test Mode": "05002a0002",
        "Set Squelch to -100dBm"        "050080009C",
        "Set RX+TX to 146.520":         "08002002C0B7BB08",
        "Put DVAP into active state":   "0500180001",
        "Put DVAP into inactive state": "0500180000",
        }

MAX_LINE = 16
CHAR_COUNT = 16
# Read and print out any incoming data from the serial port
print("Listening...")
while True:
    try:
        rx = True
        line_width = 16
        while rx:
            incoming_data = ser.read(1)  # Read up to 1 byte with a 100ms timeout
            if incoming_data:
                print(f"{incoming_data.hex()} ", end='')
                rx = True
                CHAR_COUNT = CHAR_COUNT - 1
                if CHAR_COUNT == 0:
                    print("")
                    CHAR_COUNT = MAX_LINE
            else:
                print("")
                rx = False
                CHAR_COUNT = MAX_LINE
                

        data = input("HEX:")
        if len(data) > 0:
            if data == "quit":
                print("Exiting ... ")
                sys.exit(0)
            if data == "help":
                for item in CMD_INDEX:
                    print(item, ": " , CMD_INDEX[item])
            else:
                bytes_object = bytes.fromhex(data)
                ser.write(bytes_object)

        
    except serial.SerialTimeoutException:
        print("Break the loop")
        break  # No more data available
