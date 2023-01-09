import socket

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

c.connect(( '127.0.0.1',1234))

c.send("Hi Jaimit".encode())

msg = c.recv(2048).decode()

print(msg)

c.close()