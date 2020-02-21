from socket import socket, create_connection, SHUT_WR
from random import random
from shared import send_data, recv_data

client = create_connection(('127.0.0.1', 1234))


for i in range(5):
    grid = {
        'grid': [
            ['x' if random() < 0.5 else 'o' for i in range(3)],
            ['x' if random() < 0.5 else 'o' for i in range(3)],
            ['x' if random() < 0.5 else 'o' for i in range(3)]
        ]
    }
    send_data(client, grid)
    result = recv_data(client)

client.shutdown(SHUT_WR)
client.close()