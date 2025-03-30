import socket
import time


host = '127.0.0.1' # Localhost
port = 5000 # Port number
num_messages = 100 # No. of messages to send
timeout = 1  # sec

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create a UDP socket
client_socket.settimeout(timeout) # Set timeout
print(f"UDP client sending to {host}:{port}")

latencies = [] # List to store RTTs
dropped = 0 # Count of dropped packets
with open("udp_log.txt", "w") as log_file:
    for i in range(1, num_messages + 1): # Send and receive messages
        message = f"Message {i}" # Create message
        start_time = time.time() # Start timing before sending
        client_socket.sendto(message.encode(), (host, port)) # Send message
        try: # Try to receive response
            data, addr = client_socket.recvfrom(1024)
            end_time = time.time()
            rtt = end_time - start_time
            latencies.append(rtt)
            log_line = f"{message} - RTT: {rtt:.6f} seconds\n"
            print(log_line.strip())
            log_file.write(log_line)
        except socket.timeout: # If timeout occurs
            dropped += 1
            log_line = f"{message} - Request timed out (dropped)\n"
            print(log_line.strip())
            log_file.write(log_line)

client_socket.close() # Close the socket

if latencies: # If there are any latencies
    avg_latency = sum(latencies) / len(latencies)
else:
    avg_latency = float('inf')
loss_rate = (dropped / num_messages) * 100
total_time = sum(latencies) if latencies else timeout * num_messages
avg_response_length = len("Received: Message X")
throughput = (num_messages * avg_response_length) / total_time

print(f"Average Latency: {avg_latency:.6f} seconds")
print(f"Packet Loss Rate: {loss_rate:.2f}%")
print(f"Throughput: {throughput:.2f} bytes/second")