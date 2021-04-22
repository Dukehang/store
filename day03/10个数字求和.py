'''
实现输入10个数字，并打印10个数的求和结果
'''
cs = 0#(次数)
zh = 0#(总合)

while cs<10:#(次数不大于0次)
    cs = cs +1 #(次数+1)
    print("请输入数字：")
    cs1 = input()
    cs1 = int(cs1)
    zh = zh + cs1

print("输入数字之和为：",zh)


