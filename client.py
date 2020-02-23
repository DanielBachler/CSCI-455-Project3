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

multiTest(s)
time.sleep(5)
singleTest(s)