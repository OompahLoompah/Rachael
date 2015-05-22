from modules import messageHandler


class bot(object):

    irc = None
    username = None
    chanList = None

    def __init__(self, username, irc, chanList):
        self.username = username
        self.irc = irc
        self.chanList = chanList

    def join(self, channel):
        self.irc.send('JOIN ' + channel + '\r\n')
        print "Joined " + channel
        self.irc.send('PRIVMSG ' + channel + ' :Hello\r\n')

    def send(self, channel, message):
        self.irc.send('PRIVMSG ' + channel + ' :' + message + '\r\n')

    def pong(self, irc, line):
        self.irc.send('PONG ' + line.split()[1] + '\r\n')

    def sortMessage(self, line):
        sender = messageHandler._getSender(line)
        channel = messageHandler._getChannel(line)
        message = messageHandler._getMessage(line)

        if self.username + ": Restart" in message and (sender == "sheuer" or sender == "masop"):
            print "We would send a restart request here. This isn't implemented... yet."
        else:
            self.parse(sender, channel, message)

    def parse(self, sender, channel, message):
        print "You should have overridden me! Do you really want your bot to do nothing?"

    #This is where the real meat is. All bots should begin on this function after being init'ed.
    def run(self):
        endloop = False
        while(True):
            if endloop:
                break
            
            data = self.irc.recv (4096)
            print data
            datasplit = data.splitlines()

            for line in datasplit:
                datasplit = line.split()
                if datasplit[0] == "PING":
                    self.pong(self.irc, line)
                elif((datasplit[1] == "376") or (datasplit[1] == "422")):
                    for chan in self.chanList:
                        self.join(chan)
                    endloop = True

        while(True):
            data = self.irc.recv (4096)
            datasplit = data.splitlines()
            print datasplit

            for line in datasplit:
                print(line)
                datasplit = line.split()

                if datasplit[0] == "PING":
                    self.pong(self.irc, line)

                elif datasplit[1] == "PRIVMSG":
                    self.sortMessage(line)
                
 
#                    if user + ": Restart" in message[2] and (message[0] == "sheuer" or message[0] == "masop"):

#                        try:
#                            messageHandler._send('Restarting!', chan, irc)
#                            _restart(rachael)
#                            _restart(messageHandler)
#                            bot1 = rachael.Rachael(debug, irc, chan)
#                            messageHandler._send('Restarted', chan, irc)

#                        except Exception as errormsg:
#                            messageHandler._send(("ERROR: " + str(errormsg)), chan, irc)
#                            print(traceback.format_exc())

#                    try:
#                        bot1.parse(message[0], message[2])

#                    except Exception as errormsg:
#                        messageHandler._send(("ERROR: " + str(errormsg)), chan, irc)
#                        print(traceback.format_exc())
