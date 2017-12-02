# 需要安装bitarray模块
# from bitarray import bitarray
#
# a = bitarray(endian = 'big')
# b = bitarray(endian = 'big')
# c = bitarray(endian = 'big')
# e = bitarray(endian = 'big')
# a.setall(0)
# b.setall(0)
# c.setall(0)
# e.setall(0)
# print(a)
# print(b)
# print(c)
#
# a.frombytes(b'\x03')
# print(a)
# print(a[-3:])
#
# c.frombytes(b'\x05')
# print(c)
# print(c[-5:])
#
# b = bitarray(a[-3:])
# b.extend(bitarray(c[-5:]))
# print(b)
# d = b.tobytes()
# print(hex(ord(d)))
#
# inputData = '255'
# data = int(inputData)
# print(bin(data))
# data2 = str(bin(data)).replace('b','0')
#
# e.extend(data2)
# print(e)
from bitarray import bitarray
import sys
import importlib

importlib.reload(sys)


def process(icdDict, paramDict):
    frame = bitarray(endian='big')
    frame.setall(0)

    for i in icdDict.keys():
        for j in paramDict.keys():
            if j == i:
                inputdata = paramDict[j]
                startBit = icdDict[i][0]
                length = icdDict[i][1]
                print('Input:%s StartBit:%s Length:%s' % (inputdata, str(startBit), str(length)))
                # 输入数据转换为二进制
                data = int(inputdata)
                print("Binary Format:", bin(data))
                # bitarray均是针对字符串进行处理，因此将二进制数据转换为字符串表示
                data2 = str(bin(data)).replace('b', '0')
                # 长度不足在字符串左侧补0
                if len(data2) < length:
                    data2 = data2.zfill(length)

                print('Binary Format in string', data2)
                # 在二进制字符串中取ICD要求的位数
                data3 = data2[-length:]
                # 填入该信号的bitarray中
                signal = bitarray(endian='big')
                signal.setall(0)
                signal.extend(data3)
                # 将该信号填入帧中
                frame.extend(signal)
                print('Current Frame :', frame)
                print()

    # 把二进制字符串形式的帧转换为字节
    byteStr = bitarray(endian='big')
    byteStr = frame.tobytes()
    print(type(byteStr), len(byteStr))
    print(byteStr[0], hex(byteStr[0]), "%#04x" % byteStr[0])
    print(byteStr[1], hex(byteStr[1]), "%#04x" % byteStr[1])
    print(byteStr[2], hex(byteStr[2]), "%#04x" % byteStr[2])
    print(byteStr[3], hex(byteStr[3]), "%#04x" % byteStr[3])

if __name__ == '__main__':
    # ICD配置文件解析结果：{参数名称：[起始位，长度]}
    icdDict = {'param1': [0, 3], 'param2': [3, 5], 'param3': [8, 24]}
    # 前端传过来的参数
    paramDict = {'param1': '3', 'param2': '10', 'param3': '123456'}
    # 将前端数据按照ICD转换为字节
    # 参数1值为3，占3bit,参数2值为10，占5bit，参数3为20，占8bit
    # 共占16bit,两个字节，值为0x6a14
    process(icdDict, paramDict)