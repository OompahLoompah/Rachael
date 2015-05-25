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
package = "rachael"
directory = "bots"

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
    botList = [bot]
    for bot in botList:
        tmp = Thread(target = bot.begin)
        tmp.start

    while(True):
        time.sleep(1)
