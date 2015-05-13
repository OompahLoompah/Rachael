import re

class Rachael:
    debug = False
    irc = None
    hello = re.compile(r'^Hello.*')
    test = re.compile(r'^Test.*')

    def __init__(self,debug, irc):
        print "Starting Rachael"
        self.debug = debug
        self.irc = irc

    def _join(self, channel):
        self.irc.send('JOIN ' + channel + '\r\n')
        print "Joined " + channel
        self.irc.send('PRIVMSG ' + channel + ' :Hello\r\n')

    def parse(self, sender, message):
        if self.debug == True:
            print "Testing"
        else:
            print "sender: " + sender
            print "message: " + message
            if self.hello.search(message) is not None:
                self.irc.send('PRIVMSG #default :Hello\r\n')
                print "Returning greeting"
            elif self.test.search(message) is not None:
                self.irc.send('PRIVMSG #default :Indeed...\r\n')
                print "Testing"
