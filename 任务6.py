'''
实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
'''
YHM = ""
MM = ""
CS = 0

while CS<3:
    CS=CS+1
    YHM=input("请输入用户名：")
    MM=input("请输入密码：")

    if YHM=="root"and MM=="admin":
        print("登录成功，欢迎回家")
        break
    else:
        print("登录失败")
else:
    while True:
        print("系统已锁定")
