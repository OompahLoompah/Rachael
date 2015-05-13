import re

def _getSender(data):
    split = re.split(' ', data)
    if 'PING' in split[0]:
        return ''
    else:
        split = re.split('!', split[0])
        split = re.split(':', split[0])
    return split[1]

def _getMessage(data):
    split = data.split(' ')
    message = ''
    if len(split) >= 4:
        regexp = re.compile(r'^#.+')
        if regexp.search(split[2]) is not None:
            for i in range(3, len(split)):
                print len(split)
                message = message + split[i]
                print "Split is: " + split[i]
                print "Message is: " + message
            return message[1:-2]
        else:
            return ''
    else:
        return ''
