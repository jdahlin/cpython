DEVNULL = 0

def check_call(*args, **kwargs):
    pass

def check_output(*args, **kwargs):
    if args[0][0] == 'uname':
        return b'Linux 4.19.0\n'
    return b''
