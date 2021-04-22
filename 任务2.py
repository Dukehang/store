'''
从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
'''

cs=0#(次数)
zh=0#（总和）
zds=0#（最大数）
while cs<10:#（次数不大于10次）
    cs=cs+1#（次数+1）
    print("请输入数字:")
    cs1 = input()
    cs1 = int(cs1)
    zh = zh + cs1
    if zds< cs1:
        zds=cs1
print("总和为:",zh)
print("最大值为:",zds)
print("平均数为：",zh/cs1)