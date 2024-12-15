from random import choice

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"任务：{task}已添加")

def show_task():
    if not tasks:
        print("当前列表内没有任务")
    else:
        print("任务清单：")
        for index,task in enumerate(tasks,start=1):
            print(f"{index},{tasks}")

while True:
    print("\n选择一个选项：")
    print("1、添加任务")
    print("2、显示任务")
    print("3、退出")

    choice = input("输入选项编号：")

    if choice == "1":
        new_task = input("请输入新任务：")
        add_task(new_task)
    elif choice == "2":
        show_task()
    elif choice == "3":
        print("退出任务")
        break
    else:
        print("无效输入")