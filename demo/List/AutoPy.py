import pyautogui as pg


from demo.PPPPP.py03 import login

screenWidth, screenHeight = pg.size()
print(screenWidth, screenHeight)

currentMouseX, currentMouseY = pg.position()
print(currentMouseX, currentMouseY)

pwd = input("请输入密码")
print(login())
