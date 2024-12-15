l = [0,1]
num = int(input("请输入你所需要的项数:"))
if(num<=0):
    print("请输入一个正整数")
elif(num<=2):
    if(num==1):
        print("数列是：1")
    else:
        print("数列是：0,1")
else:
    for i in range(2,num):
        f = l[i-1]+l[i-2]
        l.append(f)
    print("数组是:")
    print(l)