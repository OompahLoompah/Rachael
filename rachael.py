import re


class Rachael:
    debug = False
    irc = None
    channel = None
    hello = re.compile(r'^Hello.*')
    test = re.compile(r'^Test.*')
    test2 = re.compile(r'^Hi.*')


    def __init__(self,debug, irc, channel):
        print "Starting Rachael"
        self.debug = debug        
        self.irc = irc
        self.channel = channel

    def _join(self, channel):
        self.irc.send('JOIN ' + channel + '\r\n')
        print "Joined " + channel
        self.irc.send('PRIVMSG ' + channel + ' :Hello\r\n')

    def parse(self, sender, message):
        print "Sender: " + sender
        print "Message: " + message
        if self.debug == True:
            print "Testing!"
        else:
            if self.hello.search(message) is not None:
                self.irc.send('PRIVMSG ' + self.channel + ' :Hello\r\n')
            elif self.test.search(message) is not None:
                self.irc.send('PRIVMSG ' + self.channel + ' :Indeed...\r\n')
