import socket

server=socket.socket()
ip="0.0.0.0"
port=3001
server.bind((ip, port))

server.listen(5)
while True:
    (new_sock, address) = server.accept()
    while True:

        data = new_sock.recv(1024)
        if data == "" :
            print ("Client Disconnected")
            break

        print ("Received<<< " + data.decode())
        to_send = data.decode().upper()

        new_sock.send(to_send.encode())
        print ("Sent   >>>" + to_send)

    new_sock.close()

srv_sock.close()