# encoding: utf-8
from com.uc.conf import Conf


def inred(s):
    return"%s[1;31;40m%s%s[0m"%(chr(27), s, chr(27))

def ingreen(s):
    return"%s[1;32;40m%s%s[0m"%(chr(27), s, chr(27))

def inyellow(s):
    return"%s[1;33;40m%s%s[0m"%(chr(27), s, chr(27))

def inblue(s):
    return"%s[1;34;40m%s%s[0m"%(chr(27), s, chr(27))

def debugLog(s):
	if Conf.DEBUG_LOG:
		print inyellow(s)