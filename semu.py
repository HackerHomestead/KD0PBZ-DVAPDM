import os
import time

# Create a named pipe (FIFO) for the serial device
pipe_name = '/dev/ttyFFF0'
os.mkfifo(pipe_name)

print(f"Serial device created: {pipe_name}")

while True:
    # Read from the pipe (like receiving data from the serial device)
    with open(pipe_name, 'r') as f:
        data = f.read()
        if data:
            print(f"Received: {data.decode()}")  # Decode and print the received data

    time.sleep(0.01)  # Simulate a short delay between reads (like serial device latency)

    # Send some fake serial data to the pipe (like transmitting from the serial device)
    with open(pipe_name, 'w') as f:
        f.write(b"Hello from the serial device!")  # Write some fake data to the pipe

    time.sleep(0.01)  # Simulate a short delay between writes (like serial device latency)
