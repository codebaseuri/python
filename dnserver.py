import socket
dict1={"142.251.37.68":" 212.143.70.40"}
def handler(data,adress):
    pass




ip="0.0.0.0"
port=53
with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    s.bind((ip,port))
    print("slaayayyayaya")
    while True:
        data,adress=s.recvfrom(2330000)
        print(data.decode())
        s.sendto("142.251.37.68".encode(),adress)
