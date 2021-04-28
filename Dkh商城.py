import random
shop=[
    ["sony音响",5000],
    ["无人机",10000],
    ["ipd 2021款插卡版",4000],
    ["iphone 13",8000],
    ["Alienware GT750",15000],
    ["Lenovo 笔记本电脑",5000],
    ["雷蛇 鼠标", 1000],
    ["百事可乐",5],
    ["乐事薯片",7],
    ["费列罗巧克力",500],
    ["辣条",4],
    ["梦龙雪糕",9],
    ["可爱多",3.5],
    ["跳跳糖",2],
    ["绿豆糕",2.5]
]

#输入我的薪资
Gz=input("请输入您的工资:")
Gz=int(Gz)
Gz1=Gz

#创建我的购物车
mycart = []

#10张辣条优惠券：满600减300
#20张Lenovo电脑优惠券：半折甩卖
yhq=[
    ["辣条优惠券：满600减300"],
    ["电脑优惠券：半折"]
]


print("********欢迎来到Dkh商城********")
zl = random.randint(0,len(yhq)-1)
youryhq = yhq[zl]
print("您获得的优惠券为：",youryhq)
if zl < 10:
    yh = 1
    yh = int(yh)
else:
    yh = 0
    yh = int(yh)


#展示商品
while True:
    for index,value in enumerate(shop):
        print(index,"",value)
    num=input("请输入需要购买的商品:")
    if num.isdigit():
        num=int(num)
        if num > len(shop):
            print("该商品不存在,请选择其他商品！！！")
        else:
            if Gz >=shop[num][1]:
                mycart.append(shop[num])
                Gz = Gz-shop[num][1]
                print("成功添加到购物车！！！余额为:",Gz)
            else:
                print("对不起,穷鬼,你的余额不足！请贷款再来")
    elif num == "Q" or num == "q":
        print("欢迎下次光临！！！")
        break
    else:
        print("输入非法！！！请重新输入！！！")

#打印小票
print("您本次购物商品如下:")
for index,value in enumerate(mycart):
    print(index,"",value)
jf = (Gz1 - Gz) / 10
print("您的余额为:",Gz,"您的积分为:",jf)