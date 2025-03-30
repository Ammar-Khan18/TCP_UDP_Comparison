import socket
import random

host = '0.0.0.0' # Bind to all available interfaces
port = 5000 # This is the port to listen on
drop_probability = 0.3  # 30% chance to drop the packet

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create a UDP socket
server_socket.bind((host, port)) # Bind the socket to the specified host and port
print(f"UDP server listening on {host}:{port}")

while True: # This is the Loop to receive and send messages
    data, addr = server_socket.recvfrom(1024) # Receive data
    if not data: # If data is empty, break the loop
        continue
    message = data.decode() # Decode the received data
    print(f"Received from {addr}: {message}")
    if random.random() < drop_probability: # Simulate packet loss
        print("Simulating packet loss. Dropping packet.")
        continue
    response = f"Received: {message}" # Create response
    server_socket.sendto(response.encode(), addr) # Send the response