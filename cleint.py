import socket

sock = socket.socket()

ip = "127.0.0.1"  # local host

port = 3001

sock.connect((ip, port))


data = input("write data to send\n>")

while data[:1] != 'q':

    sock.send(data.encode())
    print("Sent    >>>" + data)


    data = sock.recv(1024)

    if data == "":
        print ("Server Disconnected")
        break

    print (data)
    data =input(" write data to send\n >")

sock.close()