import serial

class Comms:
    def __init__(self, port):
        self.serial = serial.Serial(port, 9600)

    def send(self):
        self.serial.write("a".encode())

    def read(self):
        return self.serial.readline().decode().strip()