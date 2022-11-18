import socket

class Socket:
    def __init__(self, IP):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.IP = IP

    def close(self):
        self.socket.close()

    def send_to(self, port, BYTES):
        self.socket.sendto(BYTES, (self.IP, port))

