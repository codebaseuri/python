import socket
import time
def cycle():
    port=1278
    while True:
        s = socket.socket()
        print("succses")
        s.bind(('0.0.0.0', int(port)))
        s.listen()

        (new_sock, address) = s.accept()
        data=new_sock.recv(1000).decode()
        print(data)
        if "exit"in data:
            break
        datalist=data.split("~")

        port=datalist[0]
        new_sock.close()
        s.close()

        time.sleep(1)
        s = socket.socket()
        s.connect(('127.0.0.1',int(port)))
        sendinfo=input("enter a bloody port ")+"~"+input("if you want send another thing")
        print(sendinfo)


        s.send(sendinfo.encode())
        s.close()



cycle()