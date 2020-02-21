from socket import socket, getaddrinfo
from socket import SOCK_STREAM
from socket import AF_INET
from socket import IPPRO
from shared import recv_data, send_data

family, type, proto, name, addr = getaddrinfo('127.0.0.1', 1234)[0]
s = socket(family, type, proto)
s.bind(addr)
s.listen(1)
client, addr = s.accept()
s.close()

while True():
    grid = recv_data(client)

