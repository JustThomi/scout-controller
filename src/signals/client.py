from socket import *

class Client:
    def __init__(self):
        self.address = ('127.0.0.1', 12000)

        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.connect(self.address)
        

    def send_signal(self, msg):
        byte_string = msg.encode('utf-8')
        
        try:
            self.socket.send(byte_string)
        except socket.timeout:
            print("Socket timed out")