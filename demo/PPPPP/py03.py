# # # # st = 'hello'
# # # # print(st,id(st))
# # # #
# # # # st = 'bingbing'
# # # # print(st,id(st))
# # # #
# # # # s = {1,2,3,4,5}
# # # # print(type(s))
# # # # print(s,id(s))
# # # #
# # # # s.remove(2)
# # # # print(s,id(s))
# # # #
# # # # tua = (1,2,3)
# # # # print(tua,id(tua))
# # #
# # # def outer():
# # #     a = 10
# # #     def inner():
# # #         #nonlocal a
# # #         a = 20
# # #         def inner2():
# # #             nonlocal a
# # #             a = 30
# # #             print("Inner2的a为：",a)
# # #         inner2()
# # #         print('inner中的a为：',a)
# # #     inner()
# # #     print("outer中的a为：",a)
# # # outer()
# # #
# # # def add(a,b):
# # #     return a+b
# # #
# # # print(add(1,2))
# # #
# # # ad = lambda a,b:a+b
# # # print(ad(1,2))
# #
# #
# # # a = 8
# # # b = 5
# # # comp = lambda a,b:"a>b" if a > b else "a<b"
# # # print(comp(a,b))
# #
# # # import builtins
# # # print(dir(builtins))
# #
# # li=[1,2,3]
# # li2 = ['a','b','c']
# #
# # print(zip(li,li2))
# #
# # for i in zip(li,li2):
# #     print(i)
# #
# # print(list(zip(li,li2)))
# #
# # li =  [1,2,3]
# # def funa(x):
# #     return x * 5
# # print(map(funa,li))
# # from functools import reduce
# #
# # # import requests
# # # url = "https://api.mairui.club/hszb/boll/000001/60m/b997d4403688d5e66a"
# # # response = requests.get(url)
# # # data = response.json()
# # # print(data)
# #
# # li2=[1,2,3,4]
# # def add(x,y):
# #     return x+2*y
# # res = reduce(add,li2)
# print(res)
#
# arg = (1,2,3,4,5,6,7,8)
# # print(*arg)
#
# # def fun(a,b,*arg):
# #     print(a,b)
# #     print(*arg)
# # fun(*arg)
#
# # print(arg,*arg)
#
# a , *b = arg
# print(a)
# print(*b)

# def funa():
#     print("Interesting")
#     raise Exception("Error")
# funa()

# rightPwd = '123456789'
# def isPwd():
#     pwd = input("请输入密码：")
#     if len(pwd)<8:
#         raise Exception("密码位数不达标，请重新输入")
#
#     if pwd != rightPwd:
#         raise Exception("输入密码错误，请重新输入")
#
#     else:
#         return print("输入密码正确")
# isPwd()

def login():
    pwd = input("Enter your password: ")
    if len(pwd) >= 6:
        return "输入密码成功"
    raise Exception("密码小于6位，请重新输入")
#print(login())
try:
    print(login())
except Exception as e:
    print(e)
else:
    print("success")
finally:
    print("finally")

