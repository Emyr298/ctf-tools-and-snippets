import socket

UDP_IP = "0.0.0.0"  # IP address to bind the socket
UDP_PORT = 12345  # Port number to bind the socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening on {UDP_IP}:{UDP_PORT}")

# Receive and print messages
while True:
    data, addr = sock.recvfrom(1024)  # Receive data with a buffer size of 1024 bytes
    message = data.decode()  # Decode the received data assuming it's in string format
    print(f"Received message from {addr}: {message}")