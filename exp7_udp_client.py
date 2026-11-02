import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b"Hello UDP Server", ("127.0.0.1", 20001))

message, address = client.recvfrom(1024)
print("Message from Server:", message)
