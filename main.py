import socket
import time
from threading import Thread
from bots import rachael

#The following is mostly for testing. We'll want to move it later down the road to a config file.
user = host = server = real = "rachael"
debug = False
network = "192.168.156.64"
port = 6667
chan = "#default"

def _restart(lib):
    print "Restarting!"
    reload(lib)

def connect(username, hostname, servername, realname, network, port):
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc.connect((network, port))
    irc.send('NICK ' + username + '\r\n')
    irc.send('USER ' + username + ' ' + hostname + ' ' + servername + ' ' + ':' + realname + ' IRC\r\n')
    return irc

if debug:
    print "Debugging!"

else:
    irc = connect(user, host, server, real, network, port)
    chanList = ["#default"]
    bot1 = rachael.Rachael(user, irc, chanList)
    botList = [bot1]
    bot1.run()
    #for bot in botList:
    #    tmp = Thread(target = bot.run())
    #    tmp.start()
    #    time.sleep(100000)
    while True:
        time.sleep(100000)
