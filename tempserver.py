import socket
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0', 80))

    s.listen(5)
    client_socket, addr = s.accept()

    x=client_socket.recv(80000)

x=x.decode()
print(x)
p1=x.split("\r\n\r\n")
body=p1[1]
p1=p1[0].split("\r\n")
first=p1[0]
first=first.split(" ")
p1=p1[1:]
recvsize=-1
for line in p1:
    if "Content-Length" in line:
        recvsize=line[line.index(":"):line.index("\r\n")]
print(recvsize)

reply="HTTP/1.1 200 ok\r\n\r\n uris the king".encode()
print(client_socket.send(reply))
