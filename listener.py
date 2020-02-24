import _thread
import time
import socket
import KeyboardDemo
import tkinter as tk
import random
import sys

class Listener:
    sock = None
    message = ""
    c = None

    def __init__(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        host = s.getsockname()[0]
        print("IP: ", host)
        s.close()
        self.sock = socket.socket()
        #host = "10.200.5.248"
        self.sock.bind((host, 8000))
        
    def connection(self):
        self.sock.listen(5)
        self.c, addr = self.sock.accept()
        print("Got connection from ", addr)
        while True:
            self.message = self.c.recv(1024)
            #c.close()

    def sender(self, message):
        try:
            self.c.send(bytes(message))
        except Exception as e:
            print(e)
            print("Failed to send message")

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


class KeyboardInput():
    root = None
    phrases = [
        b"Shut up meatbag\n",
        b"Hello World\n",
        b"Hunter is the best professor\n",
        b"I am alive meatbag\n",
        b"""The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues.  The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. A single lap should be completed each time you hear this sound.  Remember to run in a straight line, and run as long as possible.  The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start.\n""",
    ]
    
    specialPhrase = b"""What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little "clever" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo.\n"""

    currentPhrase = ""

    def __init__(self):
        pass
    
    def pressed(self, key):
        print(key.keycode)
        if key.keycode == 65:
            self.currentPhrase = random.choice(self.phrases)
            print(self.currentPhrase)
        elif key.keycode == 60:
            self.currentPhrase = self.specialPhrase

    def run(self):
        self.root = tk.Tk()
        self.root.bind('<space>', self.pressed)
        self.root.mainloop()



def networkControlRobot():
    # Socket instance
    server = Listener()
    # Keyboard control instance
    keyboardInput = KeyboardInput()

    # Listening for commmands on a thread
    try:
        _thread.start_new_thread(server.connection, ())
    except:
        print("Unable to start server thread")

    # Waiting for keyboard input to send messages with other thread
    try:
        _thread.start_new_thread(keyboardInput.run, ())
    except:
        print("Unable to start keyboard thread")

    controller = KeyboardDemo.NetworkControl()
    handler = MessageHandler(controller)
    
    while True:
        # Handle incoming messages
        if server.message is not "" and server.message is not b'':
            print(server.message)
            if "Disconnect" in str(server.message):
                print("Client disconnected")
                _thread.exit()
                break
            try:
                handler.messageParser(server.message)
                print(server.message)
                server.message = ""
                print("Executed commands")
            except:
                sys.exit(0)
        # Handle outgoing messages
        if keyboardInput.currentPhrase is not "":
            server.sender(keyboardInput.currentPhrase)
            print("Sent message to client")
            keyboardInput.currentPhrase = ""
        

def __main__():
    controlType = input("What form of control do you want? (network, keyboard): ")
    print("|%s|" % controlType)
    if controlType == "network":
        print("Network Control")
        networkControlRobot()
    else:
        print("Keyboard Control")
        KeyboardDemo.keyboardControl()
    
__main__()

sys.exit(0)
