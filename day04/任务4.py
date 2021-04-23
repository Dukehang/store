'''
请编程统计列表中的每个数字出现的次数(百度初级测试开发笔试题)
List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
'''
List=[1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
List1=list(set(List))
a = len(List1)
b = 0
while b<a:
    print(List1[b],"出现",List.count(List1[b]),"次")
    b = b + 1
