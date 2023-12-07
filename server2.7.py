# 2.6  client server October 2021
import socket
import random
import traceback
import time
import threading
import os
import datetime
import pyautogui
__author__ = 'Yossi'

all_to_die = False  # global

def read_jpg_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            byte_array = bytearray(file.read())
            return byte_array
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def screanshot(path="d:\pythonlearning/screenshot.jpg"):
    x, y, width, height = 1000, 100, 80, 600
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save(path)
    # Define the path to the E: drive and create it if it doesn't exist
    return read_jpg_file(path)



def log_tcp(direction, tid, byte_data):
    """
    Log direction, tid, and all TCP byte array data
    return: void
    """
    if direction == 'sent':
        print(f'{tid} S LOG:Sent     >>> {byte_data}')
    else:
        print(f'{tid} S LOG:Received <<< {byte_data}')


def send_data(sock, tid, bdata):
    """
    Send to client byte array data
    Will add 8 bytes message length as the first field
    e.g. from 'abcd' will send b'00000004~abcd'
    return: void
    """
    bytearray_data = str(len(bdata)).zfill(8).encode() + b'~' + bdata
    sock.send(bytearray_data)
    log_tcp('sent', tid, bytearray_data)
    print("")


def check_length(message):
    """
    Check message length
    return: string - error message
    """
    size = len(message)
    if size < 13:  # 13 is the min message size
        return b'ERRR~003~Bad Format message too short'
    if int(message[:8].decode()) != size - 9:
        return b'ERRR~003~Bad Format, incorrect message length'
    return b''


def get_time():
    """Return local time"""
    return datetime.datetime.now().strftime('%H:%M:%S:%f')


def get_random():
    """Return random 1-10"""
    return str(random.randint(1, 10))


def get_server_name():
    """Return server name from the os environment"""
    return os.environ['COMPUTERNAME']


def protocol_build_reply(request):
    """
    Application Business Logic
    Function dispatcher! For each code will get to some function that handles specific request
    Handle client request and prepare the reply info
    string:return: reply
    """
    request_code = request[:4].decode()
    request = request.decode("utf8")
    if request_code == "SCRN":
       return ('SCRN' + '~').encode() + "penis".encode()# screanshot()
    elif request_code == 'RAND':
        reply = 'RNDR' + '~' + get_random()
    elif request_code == 'WHOU':
        reply = 'WHOR' + '~' + get_server_name()
    elif request_code == 'EXIT':
        reply = 'EXTR'
    else:
        reply = 'ERRR~002~code not supported'

        fields = ''
    return reply.encode()

def handlecommands(command):
    """
     Handle client request
     tuple:return: return message to send to the client and bool if to close the client socket
     """
    tosend=b""
    decommand=command[:4].decode("utf8")
    temp=command[5:].decode("utf8")
    s=""
    for i in temp:
        if i !="~":
            s+=i
        else :
            break

    try:
        if decommand=="SCRN":

            return ("SCRN"+"~"+s+"~").encode()+screanshot(s),False

        elif decommand=="snfl":
            return '''dooo some stuuf''',False

        elif decommand=="dlfl":
           return '''dooo some stuuf''',False

        elif decommand=="dire":
           return '''dooo some stuuf''',False

        elif decommand=="cpsr":# copy file to sever
            return "nigga1",False

        elif decommand=="rexe":# run exe on server
            return  "nigga2",False

        elif decommand=="exit":
            return "nigga",True
        else:
            return "error", True

    except Exception as err:
        print(traceback.format_exc())
        to_send = b'ERRR~001~General error'

    return to_send, False

#this handles the commands and returns reply as sting plus booleon value if to disconnect cleint


def handle_client(sock, tid, addr):
    """
    Main client thread loop (in the server),
    :param sock: client socket
    :param tid: thread number
    :param addr: client ip + reply port
    :return: void
    """
    global all_to_die

    finish = False
    print(f'New Client number {tid} from {addr}')
    while not finish:
        if all_to_die:
            print('will close due to the main server issue')
            break
        try:
            byte_data = sock.recv(1000000)  # todo improve it to recv by message size
            if byte_data == b'':
                print('Seems the client disconnected')
                break
            log_tcp('recv', tid, byte_data)
            err_size = check_length(byte_data)
            if err_size != b'':
                to_send = err_size
            else:
                byte_data = byte_data[9:]  # remove the length field
                to_send, finish = handlecommands(byte_data)
            if to_send != '':
                send_data(sock, tid, to_send)
                #this sends to cleint his wanted message
            if finish:
                time.sleep(1)
                break

        except socket.error as err:
            print(f'Socket Error exit client loop: err:  {err}')
            break
        except Exception as err:
            print(f'General Error %s exit client loop: {err}')
            print(traceback.format_exc())
            break

    print(f'Client {tid} Exit')
    sock.close()


def main():
    global all_to_die
    """
    main server loop
    1. accept TCP connection
    2. create a thread for each connected new client
    3. wait for all threads
    4. every X clients limit will exit
    """
    threads = []
    srv_sock = socket.socket()

    srv_sock.bind(('0.0.0.0', 1235))

    srv_sock.listen(20)

    # next line releases the port
    srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    i = 1
    while True:
        print('\nMain thread: before accepting ...')
        cli_sock, addr = srv_sock.accept()
        t = threading.Thread(target=handle_client, args=(cli_sock, str(i), addr))
        t.start()
        i += 1
        threads.append(t)
        if i > 100000000:  # for tests change it to 4
            print('\nMain thread: going down for maintenance')
            break

    all_to_die = True
    print('Main thread: waiting for all clients to die')
    for t in threads:
        t.join()
    srv_sock.close()
    print('Bye ..')


if __name__ == '__main__':
    #screanshot()
    main()
