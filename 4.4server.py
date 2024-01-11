import socket
import socket
import requestresponce as socketcleint
import os
import threading
def magictype(file):
    file_name, file_extension = os.path.splitext(file)
    return file_extension[1:]
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
    btsarray=b""
    request=socketcleint.request(socket)
    if not request.method=="GET"or "HTTP" not in request.version:
        return b"eror" # means you need to close the server
    if request.url=="/":
        request.url="/pythonthingys/index.html"

    if  "calculate-next" in request.url:
        paramerter=request.url.split("=")
        paramerter=int(paramerter[1])
        btsarray= str(paramerter+1).encode()

    elif "calculate-area" in request.url:
        paramerter = request.url.split("&")
        var2=paramerter[1].split("=")
        var2=var2[1]
        var1=paramerter[0].split("=")
        var1=var1[1]

        btsarray = str(int(var1)*int(var2)//2).encode()


    else:
        btsarray=read_jpg_file(request.url)
    if btsarray ==b"":
        return b"eror"
    header="Content-Type:"+ magictype(request.url) +'\r\n'
    header+= 'Content-Length: ' + str(len(btsarray)) + '\r\n' +  '\r\n'
    responce=socketcleint.responce(request.version,givecode(btsarray),"ok",header,btsarray)
    #print(header)

    reply=f"{responce.version} {responce.code} {responce.prase}\r\n{header}".encode()+responce.body
    return reply

def handleclient(client_socket):
    while True:
        info=parsereqeust(client_socket)
        if info==b"eror":
            break
        client_socket.send(info)
        print("Reply was sent succses fully")

    client_socket.close()

def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', 80))
        s.listen(5)
        global exit_all
        threads = []
        tid = 1
        while True:
            try:
                # print('\nbefore accept')
                client_socket, addr = s.accept()
                t = threading.Thread(target=handleclient, args=[client_socket])
                t.start()
                threads.append(t)
                tid += 1

            except socket.error as err:
                print('socket error', err)
                break
        exit_all = True
        for t in threads:
            t.join()

        print('server will die now')


if __name__ == '__main__':
    main()
