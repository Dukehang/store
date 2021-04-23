'''
有下列列表，请编程实现列表的数据翻转（京东金融的测试开发笔试题）可以选做
list = [1,2,3,4,5,6,7,8,9]
实现效果：list = [9,8,7,6,5,4,3,2,1]

'''
list = [1,2,3,4,5,6,7,8,9]
list2=[]
cs=0

while cs<len(list):
    cs=cs+1
    list2.insert(0,cs)
    print("list=",list2)




