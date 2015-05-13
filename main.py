import socket
import rachael
import messageParser
#The following is mostly for testing. We'll want to move it later down the road to a config file.

nick = "rachael"
debug = False
network = "192.168.156.64"
port = 6667
chan = "#default"

def _restart(lib):
    print "Restarting!"
    reload(lib)

if debug == True:
    print "Testing"
else:
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc.connect((network,port))
    irc.recv(4096)
    irc.send('NICK ' + nick + '\r\n')
    irc.send('USER racheal racheal racheal :racheal IRC\r\n')
    bot1 = rachael.Rachael(debug, irc)
    #bot1._join(chan)

    sender = None
    message = None
    while True:
        data = irc.recv (4096)
        if "376 rachael" in data or "422 rachael" in data:
            bot1._join(chan)
        elif data.find('PING') != -1: #If PING is Found in the Data
            irc.send('PONG ' + data.split()[1] + '\r\n') #Send back a PONG
        else:
            sender = messageParser._getSender(data)
            print data
            message = messageParser._getMessage(data)
            print "Sender: " + repr(sender)
            print "Message: " + repr(message)
            if "rachael: Restart" in message and sender is "sheuer":
                irc.send('PRIVMSG #default :Restarting!\r\n')
                _restart(rachael)
                bot1 = rachael.Rachael(debug, irc)
                irc.send('PRIVMSG #default :Restarted\r\n')
            bot1.parse(sender, message)
