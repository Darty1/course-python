from typing import Dict, Optional
from socket import socket
import json

def dump_data(obj: Dict) -> bytes:
    s = json.dumps(obj)
    return s.encode()

def load_data(data: bytes) -> Dict:
    s = data.decode()
    return json.loads(s)

def send_data(s: socket, obj: Dict) -> None:
    data = dump_data(obj)
    n = len(data)
    s.send(n.to_bytes(2,'little'))
    s.send(data)

def recv_data(s: socket) -> Optional[Dict]:
    data = s.recv(2)
    if not data:
        return None
    n = int.from_bytes(s.recv(2),'little')
    data = s.recv(n)
    return load_data(data)

