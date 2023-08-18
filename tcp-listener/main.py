import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.bind(('0.0.0.0', 12345))  
sock.listen(5)  

print("="*32)
while True:  
    connection,address = sock.accept()  
    data = connection.recv(1024)
    print("From: {}:{}".format(address[0], address[1]))
    print("-"*32)
    print(data.decode())
    print("="*32)
    if b"HTTP" in data:
        connection.send(b"HTTP/1.1 200 OK\r\nContent-Length: 0\r\n\r\n")
    else:
        connection.send(b"Success")
    connection.close()
