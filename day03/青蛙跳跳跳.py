'''
一只青蛙掉在井里了，井高20米，青蛙白天往上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
'''
Gdu=0
day=0

while Gdu<20:
    Gdu = Gdu + 3
    day = day + 1
    print("第几天",day)
    if Gdu >=20:
        break
    Gdu= Gdu - 2
    print("第几天",day)
