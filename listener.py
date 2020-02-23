import _thread
import time
import socket
import KeyboardDemo

class Listener:
    sock = None
    message = ""

    def __init__(self):
        self.sock = socket.socket()
        host = "10.200.5.248"
        self.sock.bind((host, 8000))
        
    def connection(self):
        self.sock.listen(5)
        c, addr = self.sock.accept()
        print("Got connection from ", addr)
        while True:
            self.message = c.recv(1024)
            #c.close()

    def sender(self, message):
        self.c.send(bytes(message))      

class MessageHandler():
    id = 0
    controller = None

    def __init__(self, controller):
        self.controller = controller

    def executeCode(self, keycode, id):
        if self.id == id:
            pass
        else:
            self.id = id
            # Do thing with message
            passm = int(keycode)
            self.controller.control(passm)

    # Message format: keyCode1 0|keyCode2 1|keyCode3 0|etc
    def messageParser(self, message):
        message = str(message)
        command = ""
        if message is not "":
            #print("Trim message: ",message[2:])
            messages = message.split("|")
            print(messages)
            #sys.stop()
            for i in range(len(messages)-1):
                if i is 0:
                    test = messages[i][2:]
                    self.messageExecute(test)
                else:
                    self.messageExecute(messages[i])

    def messageExecute(self, message):
        conts = message.split(" ")
        keycode = conts[0]
        id = conts[1]
        self.executeCode(keycode, id)



def networkControlRobot():
    server = Listener()
    try:
        _thread.start_new_thread(server.connection, ())
    except:
        print("Unable to start server thread")

    controller = KeyboardDemo.NetworkControl()
    handler = MessageHandler(controller)
    while True:
        if server.message is not "" and server.message is not b'':
            handler.messageParser(server.message)
            print(server.message)
            server.message = ""
            print("Executed commands")
            

def __main__():
    networkControlRobot()
    
__main__()
