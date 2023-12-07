__author__ = 'Yossi'
# 2.6  client server October 2021

import socket, sys,traceback

from PIL import Image
from io import BytesIO

def read_jpg_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            byte_array = bytearray( file.read())
            return byte_array
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def display_jpg(byte_array):
    print(byte_array)
    try:
        # Open the image from the byte array
        img = Image.open(BytesIO(byte_array))

        # Display the image
        img.show()
    except Exception as e:
        print("An error occurred:", e)

# Example usage:
# Replace the placeholder with the actual byte array of your JPG file


def logtcp(dir, byte_data):
    """
    log direction and all TCP byte array data
    return: void
    """
    if dir == 'sent':
        print(f'C LOG:Sent     >>>{byte_data}')
    else:
        print(f'C LOG:Recieved <<<{byte_data}')
__author__ = 'Yossi'
# 2.6  client server October 2021

import socket, sys,traceback



def send_data(sock, bdata):
    """
    send to client byte array data
    will add 8 bytes message length as first field
    e.g. from 'abcd' will send  b'00000004~abcd'
    return: void
    """
    bytearray_data = str(len(bdata)).zfill(8).encode() + b'~' + bdata
    sock.send(bytearray_data)
    logtcp('sent', bytearray_data)

def menu():
    """
    show client menu
    return: string with selection
    """
    print('\n  1. ask for screanshot')
    print('\n  2. ask for infofrom file')
    print('\n  3. ask for info of folder')
    print('\n  4. ask for removal of a file in the server')
    print('\n  5.ask to copy a file into the server')
    print('\n  6. run exe on server ')
    print('\n  7. disconnect from server')

    dict1={"1","2","3","4","5","6","7"}
    command=input('Input 1 - 7 > ' )
    if command=="1":
        return command+"~"+input("enter were you want to save file")
    elif command=="2":
        return command+"~"+input("enter wanted  path")
    elif command=="3":
        return command+"~"+input("enter wanted  path")
    elif command=="4":
        return command+"~"+input("enter wanted  path")
    elif command=="5":
        return command+"~"+input("enter file name")
    elif command=="6":
        return command+"~"+input("enter wanted exe")
    elif command=="7":
        return command
    else:
        print("input not correct dumbass do something good retard")


def protocol_build_request(from_user):
    """
    build the request according to user selection and protocol
    return: string - msg code
    """
    if from_user[0] == '1':
        return 'SCRN'+from_user[1:]
    elif from_user[0] == '2':
        return '"snfl"'+from_user[1:]
    elif from_user[0] == '3':
        return 'dire'+from_user[1:]
    elif from_user[0] == '4':
        return 'dlfl'+from_user[1:]
    elif from_user[0] == '5':
        return 'cpsr'+from_user[1:]
    elif from_user[0] == '6':
        return 'rexe'+from_user[1:]
    elif from_user[0] == '7':
        return 'exit'+from_user[1:]
    else:
        return ''


def protocol_parse_reply(reply):
    """
    parse the server reply and prepare it to user
    return: answer from server string
    """
    to_show = 'Invalid reply from server'

    fields = reply.split(b'~',maxsplit=2)

    code = reply[:4].decode()
    print(code)
    if code == 'SCRN':
        display_jpg(bytearray( fields[2]))

    elif code == 'RNDR':
        to_show = 'Server draw the number: ' +  fields[1]
    elif code == 'WHOR':
        to_show = 'Server name is: ' +  fields[1]
    elif code == 'ERRR':
        to_show = 'Server return an error: ' + fields[1] + ' ' + fields[2]
    elif code == 'EXTR':
        to_show = 'Server acknowledged the exit message'
    #except:
        #print ('Server replay bad format')
    return to_show




def main(ip):
    """
    main client - handle socket and main loop
    """
    connected = False

    sock= socket.socket()

    port = 1235
    try:
        sock.connect((ip,port))
        print (f'Connect succeeded {ip}:{port}')
        connected = True
    except:
        print(f'Error while trying to connect.  Check ip or port -- {ip}:{port}')

    while connected:
        from_user = menu()# gets from user wich op  they want to do and wanted path
        print(from_user)
        to_send = protocol_build_request(from_user)# this is the message to send after edditing
        if to_send =='':
            print("Selection error try again")
            continue
        try :
            send_data(sock,to_send.encode())
            byte_data = sock.recv(1000000)   # todo improve it to recv by message size
            if byte_data == b'':
                print ('Seems server disconnected abnormal')
                break
           # logtcp('recv',byte_data)
            byte_data = byte_data[9:]  # remove length field + remove the protocol and path
            #print(byte_data)
            protocol_parse_reply(byte_data)
         #   handle_reply(byte_data)

            if from_user == '4':
                print('Will exit ...')
                connected = False
                break
        except socket.error as err:
            print(f'Got socket error: {err}')
            break
        except Exception as err:
            print(f'General error: {err}')
            print(traceback.format_exc())
            break
    print ('Bye')
    sock.close()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('127.0.0.1')
















