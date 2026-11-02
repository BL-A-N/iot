import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("127.0.0.1", 20001))
print("UDP server up and running")

while True:
    message, address = server.recvfrom(1024)
    print("Message from Client:", message)
    print("Client IP Address:", address)
    server.sendto(b"Hello UDP Client", address)
