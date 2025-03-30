# TCP vs. UDP Comparison

## Overview
This assignment implements both TCP and UDP client-server models to compare performance in terms of latency, packet loss, and throughput. The TCP model ensures reliable communication with higher overhead, while the UDP model provides lower latency but with potential packet loss.

## Python Scripts
- **tcp_server.py**: TCP server code.
- **tcp_client.py**: TCP client code.
- **udp_server.py**: UDP server code.
- **udp_client.py**: UDP client code.

## How to Run the Programs

### TCP:
1. Open a terminal and start the `tcp_server.py`
2. Open another terminal and run the `tcp_client.py`

### UDP:
1. Open a terminal and start the `udp_server.py`
2. Open another terminal and run the `udp_client.py`



## Expected Outputs
- **TCP:**
    - The server will print each received message.
    - The client sends 100 messages, logs each round-trip time, and prints the average latency and estimated throughput.
- **UDP:**
    - The server will print received messages and indicate when a packet is dropped.
    - The client sends 100 messages, logs RTT for messages that receive a response, counts timeouts as dropped packets, and calculates the average latency, packet loss rate, and estimated throughput.

## Observations & Analysis
- **Latency Comparison:**
    - UDP typically shows lower latency because it avoids the overhead of establishing a connection and waiting for acknowledgments.
- **Reliability & Packet Loss:**
    - UDP can lose packets (simulated by random drops), while TCP ensures delivery through retransmissions.
- **Throughput:**
    - TCP may incur overhead due to its acknowledgment mechanism, potentially reducing throughput compared to UDP.
- **Use Cases:**
    - **TCP:** Used in applications requiring reliable data transfer (e.g., HTTP, file transfers).
    - **UDP:** Suitable for real-time applications where speed is critical and occasional loss is acceptable (e.g., VoIP, video streaming).

## References
- Python socket programming: [Python Docs](https://realpython.com/python-sockets/)
- Geeks for Geeks guide on socket programming: [GeeksforGeeks](https://www.geeksforgeeks.org/socket-programming-python/?ref=gcse_outind)
