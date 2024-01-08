import socket
def p1():
    sock = socket.socket()

    ip = "127.0.0.1"  # local host

    port = 3001

    sock.connect((ip, port))

    data = input("write data to send\n>")

    while data[:1] != 'q':

        sock.send(data.encode())
        print("Sent    >>>" + data)

        data = sock.recv(1024)

        if data == "":
            print ("Server Disconnected")
            break

        print (data)
        data = input(" write data to send\n >")

    sock.close()
class cleint(object):
    def __init__(self,ip,port):
        self.ip=ip
        self.port=port

    def sendata(self):
        sock.connect((self.ip, self.port))

    data = input("write data to send\n>")

    while data[:1] != 'q':
        sock.send(data.encode())
        print("Sent    >>>" + data)

        data = sock.recv(1024)

        if data == "":
            print ("Server Disconnected")
            break

        print (data)
        data = input(" write data to send\n >")

    sock.close()

    img_path = r"D:\uri\uwu.jpg"
    img = Image.open(img_path)
    # img.show()
    pixel = img.load()
    matrix = []
    width, height = img.size
    print(pixel[1, 21])
    color = ' .;-:!>7?CO$QHNM'
    color = "MNHQ$OC?7>!:-;. "

    for i in range(width):
        for j in range(height):
            matrix.append(sum(pixel[j, i]) // 3 // 16)
    picture = []
    for i in matrix:
        picture.append(color[i])

    print(picture)
    data = "".join(picture)
    start = 0
    with open(r"D:\uri\hello.txt", "w") as my_file:
        for i in range(width):
            my_file.write(data[start:start + height])
            my_file.write("\n")
            start += height




import cv2
import numpy as np
def array_to_matrix(input_array, matrix_width):
    # Check if the array length is divisible by the matrix width
    if len(input_array) % matrix_width != 0:
        raise ValueError("Array length is not divisible by the matrix width")

    # Reshape the array into a matrix
    matrix = np.array(input_array).reshape(-1, matrix_width)
    return matrix


# Open the video file
video_file = r"D:\uri\monkey.mp4"
cap = cv2.VideoCapture(video_file)

while cap.isOpened():
    ret, frame = cap.read()
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(width)

    if not ret:
        break
    #print (frame)
    # Display the frame

    cv2.imshow("Video Player",frame )
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
color = "MNHQ$OC?7>!:-;. "
matrix = []
for i in range(width):
    for j in range(height):
        matrix.append(sum(frame[j, i]) // 3 // 16)
picture = []
for i in matrix:
    picture.append(color[i])

# print(picture)
# data = "".join(picture)


frame = array_to_matrix(picture, width)
print(frame)
