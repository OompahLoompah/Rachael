import re


def _getMessage(data):
    message = ''
    datasplit = data.split(' ')
    for i in range(3, len(datasplit)):
        message = message + ' ' + datasplit[i]
    return(message[2:])

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
    return split[2]
