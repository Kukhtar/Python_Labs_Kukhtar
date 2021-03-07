import socket
from datetime import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

clientsocket, address = s.accept()
print(f"Connection from {address} has been established")

msg = clientsocket.recv(1024)
now = datetime.now()

full_msg = msg.decode("utf-8")
print(full_msg)
current_time = now.strftime("%H:%M:%S")
print("Time =", current_time)

clientsocket.send(bytes("Hello, client", "utf-8"))





