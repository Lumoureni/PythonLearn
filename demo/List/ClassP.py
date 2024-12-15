#Part 1
# class Complex:
#     def __init__(self,realpart,imagpart):
#         self.r = realpart
#         self.i = imagpart
# x = Complex(3.0,-4.5)
# print(x.r,x.i)

#Part 2
# class Test:
#     def prt(self):
#         print(self)
#         print(self.__class__)
# t = Test()
# t.prt()

#Part 3
# class MyClass:
#     def __init__(self,value):
#         self.value = value
#     def display_value(self):
#         print(self.value
# obj  = MyClass(42)
# obj.display_value()

#Part 4
#初始类
# class people:
#     name = ''
#     age = 0
#     __weight = 0
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print("%s 说：我%d岁。"%(self.name, self.age))
# p = people('张三',23,75)
# p.speak()
#
# #单继承示例
# class student(people):
#     grand = ''
#     def __init__(self, n, a, w, g):
#         people.__init__(self, n, a, w)
#         self.grand = g
#     def talk(self):
#         print("%s 说：我%d岁,正在读%d年级"%(self.name, self.age,self.grand))
# s = student('李四',7,45,3)
# s.talk()
#
# #另一个类，多继承之前的准备
# class speaker():
#     topic = ''
#     name = ''
#     def __init__(self, n, t):
#         self.name = n
#         self.topic = t
#     def speak(self):
#         print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))
#
# #多继承
# class sample(speaker,student):
#     a = ''
#     def __init__(self,n,a,w,g,t):
#         student.__init__(self, n, a, w, g)
#         speaker.__init__(self, n, t)
# demo = sample("Tim",20,75,4,"Python")
# demo.speak()
# demo.talk()

#Part 5 重写
# class Parent:
#     def myMethod(self):
#         print("Parent class method called")
#
# class Child(Parent):
#     def myMethod(self):
#         print("Child class method called")
#
# c = Child()
# c.myMethod()
# super(Child, c).myMethod()

#Part 6 私有变量
# class JustCount:
#     __secretCount = 0
#     publicCount = 0
#
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print(self.__secretCount)
#
# counter = JustCount()
# counter.count()
# counter.count()
# print(counter.publicCount)

# class MyClass:
#     class_variable = "Hello, world!"
#
#     @classmethod
#     def class_method(cls):
#         print("Class variable:", cls.class_variable)
#
#     def instance_method(self):
#         print("Instance method:", self.class_variable)
# # 调用类方法
# MyClass.class_method()  # 输出：Class variable: Hello, world!
# # 创建类的实例
# my_instance = MyClass()
# # 调用实例方法
# my_instance.instance_method()  # 输出：Instance method: Hello, world!


# class Site:
#     def __init__(self, name, url):
#         self.name = name  # public
#         self.__url = url  # private
#
#     def who(self):
#         print('name  : ', self.name)
#         print('url : ', self.__url)
#
#     def __foo(self):  # 私有方法
#         print('这是私有方法')
#
#
#     def foo(self):  # 公共方法
#         print('这是公共方法')
#         self.__foo()
#
#
# x = Site('菜鸟教程', 'www.runoob.com')
# x.who()  # 正常输出
# x.foo()  # 正常输出
# x.__foo()  # 报错