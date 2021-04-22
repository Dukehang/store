import random
num = random.randint(0,100)
count = 0
G=9999

while True:
    count = count + 1
    G=G-100
    num1=input("请输入要猜的数字：")
    num1 = int(num1)
    if num1 > num:
        print("大了")
    elif num1 < num:
        print("小了")
    else:
        print("回答正确,本次中奖号码为",num,"您本次猜了",count,"次","剩余金额为",G)
        break