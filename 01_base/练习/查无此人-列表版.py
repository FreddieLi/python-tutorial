"""
小明拿到了一个电影+演员的数据名单，他想设计一个程序，要求：
1.输入演员名
2.如果演员出演了电影，则打印他+他出演的全部电影。程序结束
3.如果演员没有出演电影，则打印查无此人。程序继续
电影 = [
'妖猫传',['黄轩','染谷将太'],
'无问西东',['章子怡','王力宏','祖峰'],
'超时空同居',['雷佳音','佟丽娅','黄轩']]
"""


# movie = [
# '妖猫传',['黄轩','染谷将太'],
# '无问西东',['章子怡','王力宏','祖峰'],
# '超时空同居',['雷佳音','佟丽娅','黄轩']]

# input = '黄轩'
# i=0
# for x in movie:
#     if (type(x) == list):
#         for y in x:
#             if (input == y):
#                 print(movie[i-1])
#     i+=1














电影 = [
'妖猫传',['黄轩','染谷将太'],
'无问西东',['章子怡','王力宏','祖峰'],
'超时空同居',['雷佳音','佟丽娅','黄轩']]
# 如果查到了：打印出演员+【所有的】电影，循环结束
# 如果没查到，就 循环继续，并且打印【查无此人】
找到了吗 = 0 
while True:
    name = input('你要找的演员')
    for i in 电影:
        if name not in i : 
            a = i #暂存---for 是逐一提取数据，并赋值
        else:
            print(name,'出演了',a)
            找到了吗 += 1        
    if 找到了吗 != 0 : # 不等于 0 就代表它找到了
        break
    print('【查无此人】') # 1号位