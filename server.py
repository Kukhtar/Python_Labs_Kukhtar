import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

clientsocket, address = s.accept()
print(f"Connection from {address} has been established")

while True:
	msg = clientsocket.recv(1024)
	sent = clientsocket.send(msg)

	full_msg = msg.decode("utf-8")
	print(full_msg)

	if full_msg.strip() == "stop":
		break

print("Connection closed!!")
s.close()

