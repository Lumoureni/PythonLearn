people={}
for x in range(1,31):
    people[x]=1
print(people)
check = 0
i = 1
j = 0
#遍历人头，满30个人回到1个人重新开始
while i <= 31:
    if i == 31:
        i = 1
    #下船人数满足要求退出循环
    elif j == 15:
        break
    else:
        #已经下船的人状态为0，+1跳过
        if people[i] == 0:
            i+=1
            continue
        else:
            #开始报数
            check += 1
            if check == 9:
                people[i] = 0
                check = 0
                print("{}号下船了".format(i))
                j+=1
            else:
                i+=1
                continue