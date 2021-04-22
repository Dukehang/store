'''
从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
'''

print("请输入第一条边：")
a1=input()

print("请输入第二条边：")
b1=input()

print("请输入第三条边")
c1=input()

a=int(a1)
b=int(b1)
c=int(c1)

if  a+b>c and a+c>b and b+c>a:
    print("构成普通三角形")
    if a==b or a==c or b==c:
        print("构成等腰三角形")
    if  a*a+b*b==c*c or b*b+c*c==a*a or c*c+a*a ==b*b:
            print("构成直角三角形")
else:
    print("不构成三角形")