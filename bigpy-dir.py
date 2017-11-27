'''找出单个目录下最大的python源代码文件
搜索window python源代码库，除非指定了dir命令行参数'''
import os, sys, glob
dirname = r'C:\Program Files (x86)\Python\Python36-32\Lib' if len(sys.argv) == 1 else sys.argv[1]

allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py')
for filename in allpy:
    filesize = os.path.getsize(filename)
    allsizes.append((filesize, filename))

allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])