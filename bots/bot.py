from modules import messageHandler
from Queue import Queue

class bot(object):

    irc = None
    username = None
    chanList = None
    stopThread = True
    messageQueue = None

    def __init__(self, username, irc, chanList, messageQueue):
        self.username = username
        self.irc = irc
        self.chanList = chanList
        self.stopThread = False
        self.messageQueue = messageQueue
    def join(self, channel):
        self.irc.send('JOIN ' + channel + '\r\n')
        print "Joined " + channel
        self.irc.send('PRIVMSG ' + channel + ' :Hello\r\n')

    def send(self, channel, message):
        self.irc.send('PRIVMSG ' + channel + ' :' + message + '\r\n')

    def pong(self, irc, line):
        self.irc.send('PONG ' + line.split()[1] + '\r\n')

    def restart(self):
        for channel in self.chanList:
            self.send(channel, "Restarting!")
        print "requesting restart"

    def sortMessage(self, line):
        sender = messageHandler._getSender(line)
        channel = messageHandler._getChannel(line)
        message = messageHandler._getMessage(line)

        if self.username + ": Restart" in message and (sender == "sheuer" or sender == "masop"):
            print "starting restart"
            self.restart()
        else:
            self.parse(sender, channel, message)

    def parse(self, sender, channel, message):
        print "You should have overridden me! Do you really want your bot to do nothing?"

    #This is where the real meat is. All bots should begin on this function after being init'ed.
    def begin(self):
        while(not self.stopThread):
            
            data = self.irc.recv (4096)
            print data
            print "looking for connection"
            datasplit = data.splitlines()

            for line in datasplit:
                datasplit = line.split()
                if datasplit[0] == "PING":
                    self.pong(self.irc, line)
                elif((datasplit[1] == "376") or (datasplit[1] == "422")):
                    for chan in self.chanList:
                        self.join(chan)
                    self.run()

    def run(self):
        while(not self.stopThread):
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
