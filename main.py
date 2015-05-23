import socket
import time
from threading import Thread
from bots import rachael
from Queue import Queue

#The following is mostly for testing. We'll want to move it later down the road to a config file.
user = host = server = real = "rachael"
debug = False
network = "192.168.156.64"
port = 6667
chan = "#default"

#Soo.... yeah, this next part is really nasty code. I don't like it but it works.
def setupBot(_module, library, user, host, server, real, network, port, chanList):
    chanList = ["#default"]
    messageQueue = Queue(maxsize=0)
    bot = _module
    newBot = bot(user, host, server, real, chanList, messageQueue, network, port)
    newBot.begin()
    #return (botTuple)

def _restart(botTuple): #botTuple is (bot class, library name, username, irc, chanList, messageQueue, thread, bot object)
    print "Restarting!"
    reload(botTuple[1])
    bot = setupBot(botTuple)
    print "Done restarting!"
    return botTuple

if debug:
    print "Debugging!"

else:
    chanList = ["#default"]
    bot = setupBot(rachael.Rachael, rachael, user, host, server, real, network, port, chanList)
    #botList = [bot]
    print "started bot!"
    print "starting loop"
    #irc = connect(user, host, server, real, network, port)
    #chanList = ["#default"]
    #bot = _module
    #newBot = bot(user, irc, chanList)
    #newBot.begin()
