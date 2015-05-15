import ConfigParser

config = ConfigParser.ConfigParser()
cfile = open('com/uc/conf/default.ini', 'rb')

config.readfp(cfile)
packageName = config.get("event", "t1")
print packageName

testlist = config.get('list', 'tl')
# print testlist

ret = testlist.splitlines()
# print ret
