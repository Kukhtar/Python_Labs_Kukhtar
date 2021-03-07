import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

clientsocket, address = s.accept()
print(f"Connection from {address} has been established")

msg = clientsocket.recv(1024)
time.sleep(5)

sent = clientsocket.send(msg)

print(sent)
print(len(msg))

if sent==len(msg):
	print("Sent succesfuly")
else:
	print("Failed")

s.close()

