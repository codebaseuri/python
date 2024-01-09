class request:
    def __init__(self,sock):

        data=b""
        while b"\r\n\r\n" not in data:
            data += sock.recv(8192)

        data=data.decode()
        split1=data.split("\r\n\r\n")
        self.body=split1[1]
        self.header=split1[0].split("\r\n")
        self.reqlines=self.header[0].split(" ")
        self.method=self.reqlines[0]
        self.url=self.reqlines[1]
        self.version=self.reqlines[2]
        self.header=self.header[1:]
        recvsize=-1
        for line in self.header:
            if "Content-Length" in line:
                recvsize=line[line.index(":"):line.index("\r\n")]
        print(recvsize)
        if  not recvsize==-1:
            data+=sock.recv(recvsize).decode()

class responce():
    def __init__(self,version,statuscode,prase,headers,body):
        self.version=version
        self.code=statuscode
        self.prase=prase
        self.headers=headers
        self.body=body






