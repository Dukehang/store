name = input("请输入您的姓名：")
age = input("请输入您的年龄：")
sex = input("请输入您的性别：")
sfz = input("请输入您的身份证号：")
stature = input("请输入您的身高：")
home = input("请输入您的居住地：")

info = '''
                        <><><><><><> 个人信息 <><<><><><>
                          姓名：%s,                   
                                                     
                          年龄：%s,                    
                                                     
                          性别：%s,                   
                                                     
                          身份证号：%s,               
                                                     
                          身高：%s,                   
                                                     
                          居住地：%s                   
                        <><><><><><><><><><><><><><<><><>
'''
print(info   %   (name,age,sex,sfz,stature,home))

