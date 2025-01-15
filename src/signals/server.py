import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(('', 12000))

print("listening...")

while True:
    message, address = socket.recvfrom(1024)
    print(message)