import socket
import time

def cycle():
    port=1278
    while True:
        time.sleep(2)
        s = socket.socket()
        print("succses")
        s.connect(('127.0.0.1', port))

        sendinfo = input("enter a bloody port ") + "~" + input("if you want send another thing")
        sendlist=sendinfo.split("~")
        port=int(sendlist[0])
        s.send(sendinfo.encode())
        s.close()

        s = socket.socket()
        s.bind(('0.0.0.0', port))
        s.listen()

        (new_sock, address) = s.accept()
        data = new_sock.recv(1000).decode()
        print(data)
        if "exit" in data:
            break
        datalist = data.split("~")

        port = int(datalist[0])
        print(datalist[0])
        new_sock.close()
        s.close()

cycle()