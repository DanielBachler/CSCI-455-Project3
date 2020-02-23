import _thread
import time
import socket
import KeyboardDemo

class Listener:
    sock = None
    message = ""

    def __init__(self):
        self.sock = socket.socket()
        host = "10.200.14.40"
        self.sock.bind((host, 8000))

    def connection(self):
        self.sock.listen(5)
        while True:
            c, addr = self.sock.accept()
            print("Got connection from ", addr)
            self.message = c.recv()

    



def __main__():
    server = Listener()
    try:
        _thread.start_new_thread(server.connection, ())
    except:
        print("Unable to start server thread")

    controller = KeyboardDemo.NetworkControl()
    oldmes = ""
    while True:
        curmes = server.message
        if oldmes == curmes:
            pass
        else:
            oldmes = curmes
            # Do thing with message
            controller.control(curmes)
__main__()
