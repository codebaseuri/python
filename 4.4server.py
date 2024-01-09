import socket
import socket
import socketcleint
import os
def givecode(body):
    if not b"not found"in body :
        print("200")
        return "200"
    else:
        print("404")
        return "404"
def read_jpg_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            byte_array = bytearray(file.read())
            return byte_array
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return b"not found error"
    except Exception as e:
        print(f"Error: {e}")
        return b""
def parsereqeust(socket):
    request=socketcleint.request(socket)
    if not request.method=="GET"or "HTTP" not in request.version:
        return b"erororrrr niggger" # means you need to close the server
    if request.url=="/":
        request.url="/pythonthingys/index.html"
    btsarray=read_jpg_file(request.url)
    if btsarray ==b"":
        return b"erororrrr niggger"
    header= 'Content-Length: ' + str(len(btsarray)) + '\r\n' + '\r\n'
    responce=socketcleint.responce(request.version,givecode(btsarray),"ok",header,btsarray)

    reply=f"{responce.version} {responce.code} {responce.prase}\r\n{header}".encode()+responce.body
    return reply



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0', 80))

    s.listen(5)
    client_socket, addr = s.accept()

    client_socket.send(parsereqeust(client_socket))

