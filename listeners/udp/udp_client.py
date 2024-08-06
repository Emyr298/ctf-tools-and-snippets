import socket

UDP_IP = "127.0.0.1"  # IP address of the destination
UDP_PORT = 12345  # Port number of the destination

message = "Hello, UDP!"  # Message to send

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send the message
sock.sendto(message.encode(), (UDP_IP, UDP_PORT))

print(f"Message sent to {UDP_IP}:{UDP_PORT}")