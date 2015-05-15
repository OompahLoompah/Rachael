import re

#return (sender, channel, message) tuple
def _getPrivmsg(data):
    message = ''
    datasplit = data.split(' ')
    for i in range(3, len(datasplit)):
        message = message + ' ' + datasplit[i]
    return(_getSender(data), datasplit[2], message[2:])

def _getSender(data):
    split = re.split(' ', data)
    if 'PING' in split[0]:
        return ''
    else:
        split = re.split('!', split[0])
        split = re.split(':', split[0])
    return split[1]

def _getChannel(data):
    split = data.split(' ')
    return data[2]

def _getMessage(data):
    split = data.split(' ')
    message = ''
    if len(split) >= 4:
        regexp = re.compile(r'^#.+')
        if regexp.search(split[2]) is not None:
            for i in range(3, len(split)):
                message = message + ' ' + split[i]
            return message[1:]
        else:
            return ''
    else:
        return ''
