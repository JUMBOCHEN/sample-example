'''找出整个目录树中最大的python源代码文件
搜索源代码库，并利用pprint模块漂亮的打印出来'''
import sys, os, pprint
trace = False
if sys.platform.startswith('win'):
    dirname = r'C:\Program Files (x86)\Python\Python36-32\Lib' #windows platform
else:
    dirname = 'usr/lib/python' #linux,unix and cygwin platform

allsizes = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    if trace: print(thisDir)
    for filename in filesHere:
        if filename.endswith('.py'):
            if trace: print('...', filename)
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, fullname))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])
