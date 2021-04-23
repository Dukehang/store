'''
有以下一个列表，求其中是5的倍数的和
a = [1,5,21,30,15,9,30,24]
'''

a = [1,5,21,30,15,9,30,24]
sl=0
zh=0
while sl<len(a):
    b= a[sl]/5
    b=int(b)
    if b*5==a[sl]:
        zh=zh+a[sl]
    sl=sl+1
print("5的倍数总和为：",zh)
