'''
请从00:00依次打印出一天的时间
示例：
23 : 52
23 : 53
23 : 54
23 : 55
23 : 56
23 : 57
23 : 58
23 : 59
'''


for i in range(0,24):
    for j in range(0,60):
        print('{:0>2d}:{:0>2d}'.format(i,j))






# for 时钟 in range(24):
#     for 分钟 in range(60):
#         print(时钟, ':', 分钟)
