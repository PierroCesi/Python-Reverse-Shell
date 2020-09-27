import os

def exeCmd(cmd):
    return str(os.popen(cmd).read())


