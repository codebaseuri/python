import os
import socket, threading

exts_txt = ['.js', '.txt', '.css']
exts_bin = ['.html', '.jpg', '.gif', '.ico']

moved_302 = {'A/dog.jpg': 'B/dog.jpg', 'B/dog.jpg': 'B/dog2.jpg'}

exit_all = False

PROTOCOL = 'HTTP1.1'


def http_send(s, reply_header, reply_body):
    reply = reply_header.encode()
    if reply_body != b'':
        try:
            body_length = len(reply_body)
            reply_header += 'Content-Length: ' + str(body_length) + '\r\n' + '\r\n'
            reply = reply_header.encode() + reply_body
        except Exception as e:
            print(e)
    else:
        reply += b'\r\n'
    s.send(reply)
    print('SENT:', reply[:min(100, len(reply))])


def http_recv(sock : socket.socket, BLOCK_SIZE=8192):
    data = b""
    while b"\r\n\r\n" not in data:
        data += sock.recv(BLOCK_SIZE)
    lines = data.split(b"\r\n\r\n")
    request = lines[0]
    body = lines[1]
    headers = request.split(b'\r\n')
    return headers, body


def get_type_header(requested_file):
    pass


def get_file_data(requested_file):
    pass


def handle_request(request_header, body):
    resp_headers = b""



def handle_client(s_clint_sock, tid, addr):
    global exit_all
    print('new client arrive', tid, addr)
    while not exit_all:
        request_header, body = http_recv(s_clint_sock)
        if request_header == b'':
            print('seems client disconected, client socket will be close')
            break
        else:
            reply_header, body = handle_request(request_header, body)
            if PROTOCOL == "HTTP1.0":
                reply_header += "Connection': close\r\n"
            else:
                reply_header += "Connection: keep-alive\r\n"
            http_send(s_clint_sock, reply_header, body)
            if PROTOCOL == "HTTP1.0":
                break
    print("Client", tid, "Closing")
    s_clint_sock.close()


def main():
    global exit_all
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 80))
    server_socket.listen(5)
    threads = []
    tid = 1
    while True:
        try:
            # print('\nbefore accept')
            client_socket, addr = server_socket.accept()
            t = threading.Thread(target=handle_client, args=(client_socket, tid, addr))
            t.start()
            threads.append(t)
            tid += 1

        except socket.error as err:
            print('socket error', err)
            break
    exit_all = True
    for t in threads:
        t.join()

    server_socket.close()
    print('server will die now')


if __name__ == "__main__":
    main()
