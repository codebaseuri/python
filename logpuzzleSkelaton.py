import os
import re
import sys,subprocess
from urllib.request import urlretrieve

def createhtml():
    data=""
    for i in range(0,200):
        data +=f'<img src="{i}.jpg"/>'

    data = "<HTML>" + data + "</HTML>"
    with open("ophir.html","w") as file:
        file.write(data)


def nfilter(string):
    string=string.split("-")
    return string[-1]
def openfile2():
    with open("harmonious-khapse-0c6bda.netlify.app.log","r")as file:
        data=file.read()
    data=data.split("\n")
    fdata = [string for string in data if "cyberbit" in string]

    nfdata=[]
    for i in fdata:
        nfdata.append(i[i.find("cyberbit"):i.find("HTTP")])

    nfdata=set(nfdata)
    nfdata=list(nfdata)
    nfdata=sorted(nfdata,key=nfilter)

    n2=[]
    for z in nfdata:

        n2.append("harmonious-khapse-0c6bda.netlify.app/" + z)
    return n2


def openfile1():
    with open("superlative-unicorn-5c0110.netlify.app.log","r")as file:
        data=file.read()
    data=data.split("\n")
    fdata = [string for string in data if "cyberbit" in string]
   # sorted = sorted(fdata, key=lambda x: "" in x)
    for line in fdata:
        #print(line)
        pass

    nfdata =[]
    c=0
    for i in fdata:
        nfdata.append(i[i.find("cyberbit"):i.find("HTTP")])
    nfdata=set(nfdata)
    nfdata=list(nfdata)
    nfdata.sort()

    n2=[]

    for z in nfdata:
        n2.append("superlative-unicorn-5c0110.netlify.app/" + z)
    print(n2)
    return n2



def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    pass

def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.

    """
    cnt = 0
    for i in img_urls:
        urlretrieve(r"https://"+i, "d:\\"+str(cnt) + ".jpg")
        cnt += 1


def main():
    if len(sys.argv) < 3:
        print('usage: <log filename> <target location> ')
    else:
        print('start')
        log_filename = sys.argv[1]
        target_dir = sys.argv[2]

        img_urls = openfile()

        print(img_urls)

        if os.path.isdir(target_dir):
            download_images(img_urls, target_dir)
            print('Done')
            subprocess.call('index.html', stdin=None, stdout=None, stderr=None, shell=True)
        else:
            print('Traget dir not exist')


if __name__ == '__main__':
    #main()
    #openfile2()
    #download_images(openfile2(),1)
    createhtml()

