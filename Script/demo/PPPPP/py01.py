def fun1():
    s = 0
    for i in range(1,101):
        s += i
    print(s)


def fun2(n):
    if n == 1:
        return 1
    return n + fun2(n-1)
#print(add2(5))

#斐波那契数组
def fun3(n):
    if n <= 1:
        return n
    else:
        return fun3(n-2) + fun3(n-1)
print(fun3(5))


#---------------------#
def fun4(n):
    m = 5
    def inner():
        return m+n
    return inner()
print(fun4(5))
#---------------------#

#---------------------#
def fun5(n):
    print("Fun5 = ",n)
    def fun6(m):
        print("Fun6 = ",m)
        return m+n
    return fun6
f5 = fun5(5)
f5(10)
print(f5(10))

a = fun5(10)(23)
print(a)
#---------------------#

