import socket
import time
size_header_size=6
import re

def extract_valid_words(input_string):
    pattern = r'(?<=[\x21-\x2F]{2})\b\w+\b(?=[\x21-\x2F]{2})'

    matches = re.findall(pattern, input_string)
    return matches

def __recv_amount(sock, size=4):
    buffer = b''
    while size:
        new_bufffer = sock.recv(size)
        if not new_bufffer:
            return b''
        buffer += new_bufffer
        size -= len(new_bufffer)
    return buffer


def recv_by_size(sock, return_type="bytes"):
    try:
        data = b''
        data_len = int(__recv_amount(sock, size_header_size))
        # code handle the case of data_len 0
        data = __recv_amount(sock, data_len)
        if return_type == "string":
            return data.decode()
    except OSError:
        data = '' if return_type == "string" else b''
    return data

def f1():
    for i in range(26):
        str1 = chr(i + 65)
        for j in range(15):
            str2=chr(j+32)
            for i in range(10):
                str3=str(i)
                for i in range(10):
                    str4 = str(i)

                    s.send((str1+str2+str3+str4).encode())
                    var=s.recv(500).decode()
                    if "CONFIRM" in var:
                        print(str1 + str2 + str3 + str4)
                        print(var)
                        break
                        break
                        break
s=socket.socket()
ip="10.68.121.30"
port=8576
s.connect((ip,port))
var=s.recv(10000)
print(var)
s.send("help".encode())
var=s.recv(10000).decode()
print(var)
str1=""
code="S'88"
code="0000"
s.send(code.encode())

var = s.recv(10000000).decode()

print(var)
s.send("CONFIRM".encode())
var=b""
for i in range(13):
    var +=recv_by_size(s)


with open(r"D:\uri\image67.jpg","wb") as f1:
    f1.write(var)
#print(var)
pas="23 0 30 13 23"
pas3=chr(80)+chr(78)+chr(65)+chr(97)+chr(73)
#print(pas3)
pas2="7378659773 "
s.send(pas3.encode())
rev=s.recv(1000)
#print(rev)
s.send(chr(4).encode())
rev=s.recv(1000).decode()
print(rev)
s.send("CONFIRM".encode())
saved=s.recv(1000000).decode()
#print(extract_valid_words(saved))
print(saved)
s.close()