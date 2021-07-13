from dataclasses import dataclass
from socket import socket, AF_INET, SOCK_STREAM

import time

@dataclass
class SocketObject:
    def __init__(self, addr: str, port: int):
        self.smtp_socket = socket(AF_INET, SOCK_STREAM)
        self.addr = addr
        self.port = port

    def connect(self) -> str:
        self.smtp_socket.connect((self.addr, self.port))
        time.sleep(.005)
        ret_mesg = self.smtp_socket.recv(1024).decode()
        
        return ret_mesg

    def send_command(self, command) -> str:
        self.smtp_socket.send(command.encode())
        time.sleep(.005)
        ret_mesg = self.smtp_socket.recv(1024).decode()

        return ret_mesg

    def send_no_ret_command(self, command):
        self.smtp_socket.send(command.encode())
        time.sleep(.005)

    def close_connection(self):
        quit_command = "QUIT\r\n".encode()
        self.smtp_socket.send(quit_command)

