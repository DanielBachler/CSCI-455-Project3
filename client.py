import socket
import time

s = socket.socket()
host = "10.200.5.248"
port = 8000

s.connect((host, port))

def multiTest(s): 
    s.send(bytes(b"98 0|"))
    s.send(bytes(b"98 1|"))
    s.send(bytes(b"98 0|"))
    s.send(bytes(b"98 1|"))
    #s.send(bytes(b"65 0|"))

def singleTest(s):
    s.send(bytes(b"65 0|"))


# Testing receiving message from server
# test = True
# m = ""
# while test:
#     m = s.recv(1024)
#     if m is not "" and m is not b'':
#         print(m)
#         m = ""

# Testing commands

# multiTest(s)
# time.sleep(5)
singleTest(s)