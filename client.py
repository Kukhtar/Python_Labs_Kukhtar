import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

while True:
	msg = input()
	s.send(bytes(msg, "utf-8"))
	msg = s.recv(1024)
	full_msg = msg.decode("utf-8")