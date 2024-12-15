#文件读取格式
# path = r"……………………"
# with open(路径,'读写二进制改写',encoding='utf-8') as x:
# w,w+（覆盖）,a,a+（写入追加），b（二进制），x（存在即失败）均可以创建新文件
#前提为r+
#x.read()逐字阅读
#x.readline()
#x.readlines()逐行阅读效率最高！
#前提为w
#x.write
#x.writelines
#dumps序列化
#loads反序列化

#----------------------------------#
path = r"/FileIO/test.txt"
path2 = r"D:\Code\Script\FileIO\test2.txt"
path3 = r"D:\Code\Script\FileIO\1.txt"


note = "Hello world"
word=["hello","world"]

# with open(path,'w+',encoding='utf-8') as f:
#     f.write(note+"\n")

# with open(path2,'a',encoding='utf-8') as f:
#     f.writelines(word)

# with open(path,'r',encoding='utf-8') as r:
#     while True:
#         note = r.read()#read(n)n指一次读取几个字节
#         if note:
#             print(note)
#         else:
#             break

# with open(path2,'r',encoding='utf-8') as r:
#     word = r.readline()
#     print(word,end=" ")

# with open(path3,'r',encoding='utf-8') as r:
#     for i in r.read():
#         print(i,end=" ")

# with open(path3,'r',encoding='utf-8') as r:
#     for i in r.readlines():
#         print(i,end=" ")

# with open(path2,'r',encoding='utf-8') as r:
#     line = r.readline()
#     while line is not None and line != '':
#         print(line)
#         line = r.readline()

# with open(path3,'r',encoding='utf-8') as r:
#     for i in r.read():
#         print(i,end=" ")

# with open(path3,'r',encoding='utf-8') as r:
#     for line in r:
#         print(line,end=" ")

# with open(path3,'r',encoding='utf-8') as r:
#     line2 = r.readlines()
#     for line in line2:
#         print(line)

#----------------------------#

import os
#os.remove(path2)删除文件
# n1 = r"D:\Code\Script\demo\n2.txt"
# n2 = r"D:\Code\Script\demo\test2.txt"
# os.rename(n1,n2)重命名文件

import pickle
# text1 = "Gaming Start"
# data = pickle.dumps(text1)
# print(data)
#
# data2 = pickle.loads(data)
# print(data2)

# datapath = r"D:\Code\Script\FileIO\datapath.txt"
# with open(datapath,'wb') as dp:
#     pickle.dump(text1,dp)

#
# with open(datapath,'rb') as dp2:
#     content = pickle.load(dp2)
#     print(content)


# import json
# fruit ={"name":"banana","price":100}
# print(fruit)
# print(type(fruit))
#
# data = json.dumps(fruit)
# print(data)
# print(type(data))
#
# obj = json.loads(data)
# print(obj)
# print(type(obj))