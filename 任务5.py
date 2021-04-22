'''
有以下两个数，使用+，-号实现两个数的调换。
A=56
B=78
实现效果：
A=78
B=56

'''
A=56
B=78
C=0
print("A=",A,"B=",B)
D=input("输入加减:")
if D=="+"or D=="-":
    C=A
    A=B
    B=C
    print("A=",A,"B=",B)

else:
    print("输入有误")


