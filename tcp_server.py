import socket
import time

host = '0.0.0.0' # Bind to all available interfaces
port = 5000 # This is the port to listen on

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP socket
server_socket.bind((host, port)) # Bind the socket to the specified host and port
server_socket.listen(1) # Start listening for incoming connections for now we are only allowing one connection
print(f"TCP server listening on {host}:{port}")

conn, addr = server_socket.accept() # Accept incoming connection
print(f"Connected by {addr}")

while True: # This is the Loop to receive and send messages
    data = conn.recv(1024) # Receive data
    if not data: # If data is empty, break the loop
        break
    received_time = time.time()  # Timestamp when message is received
    message = data.decode() # Decode the received data
    print(f"Received at {received_time:.6f} seconds: {message}")

    response = f"Received: {message}"
    conn.sendall(response.encode()) # Send the response

    sent_time = time.time()  # Timestamp when response is sent
    print(f"Response sent at {sent_time:.6f} seconds")

conn.close() # Close the connection
server_socket.close() # Close the server socket