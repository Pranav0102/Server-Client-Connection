from audioop import add
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#socket object. what type of socket(ipv4(AF_INET : family of ipv4) or ipv6) and type of protocol : UDP or TCP

s.bind(('127.0.0.1',1234))

s.listen(5)

client ,address =s.accept() 
print(address)

msg = client.recv(2048).decode()
print(msg)

client.send("Hello I am server".encode())
client.close()

s.close()
