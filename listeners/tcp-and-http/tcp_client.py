import socket

TCP_IP = "127.0.0.1"  # IP address of the server
TCP_PORT = 12345  # Port number of the server
MESSAGE = "Hello, TCP Server!"  # Message to send

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((TCP_IP, TCP_PORT))

# Send the message
client_socket.sendall(MESSAGE.encode())

# Receive and print the response
response = client_socket.recv(1024)
print(f"Received response: {response.decode()}")

# Close the connection
client_socket.close()