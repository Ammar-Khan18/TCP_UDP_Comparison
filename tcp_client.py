import socket
import time

host = '127.0.0.1' # Localhost
port = 5000 # Port number
num_messages = 100  # No. of messages to send

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP socket
client_socket.connect((host, port)) # Connect to the server
print(f"Connected to TCP server at {host}:{port}")

latencies = [] # List to store RTTs
with open("tcp_log.txt", "w") as log_file: # Open log file
    for i in range(1, num_messages + 1): # Send and receive messages
        message = f"Message {i}" # Create message
        start_time = time.time()  # Start timing before sending
        client_socket.sendall(message.encode()) # Send message
        data = client_socket.recv(1024) # Receive response
        end_time = time.time()  # End timing after receiving response
        rtt = end_time - start_time  # Calculate RTT
        latencies.append(rtt) # Add RTT to list
        log_line = f"{message} - RTT: {rtt:.6f} seconds\n"
        print(log_line.strip())
        log_file.write(log_line)

client_socket.close() # Close the socket

avg_latency = sum(latencies) / len(latencies) # Calculate average RTT
print(f"Average RTT: {avg_latency:.6f} seconds")
