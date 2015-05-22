import re
import bot

class Rachael(bot.bot):
    hello = re.compile(r'^Hello.*')
    test = re.compile(r'^Test.*')
    test2 = re.compile(r'^Hi.*')

    def parse(self, sender, channel, message):
        print "Sender: " + sender
        print "Message: " + message
        if self.hello.search(message) is not None:
            self.irc.send('PRIVMSG ' + channel + ' :Hello\r\n')
        elif self.test.search(message) is not None:
            self.irc.send('PRIVMSG ' + channel + ' :Indeed...\r\n')
