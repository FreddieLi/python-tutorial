'''
给定一个列表，请你对列表的元素进行     从大到小排序   与从小到大排序
'''


# 可以參考這邊的動圖 概念上index從0開始跑到len-1,所以最後面list[len-1]會是最大或者最小 
# 下一次的循環就不需要從0~len-1，而是0~len-2 
# https://www.runoob.com/w3cnote/bubble-sort.html



list1 = [13, 22, 6, 99, 11, 0]
# list1.__len__()
print(list1.__len__())

i = 0
exchanged=1
while(i < list1.__len__() and exchanged == 1):
    exchanged =0
    j=0
    while(j<list1.__len__()-1-i):
        if (list1[j] > list1[j+1]):
            temp=list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = temp
            exchanged=1
        j+=1
    print("%d"%(i),end=" "); print(list1)
    i+=1
print(list1)


















# for a in range(len(list1)):
#     for b in range(a,len(list1)):
#         if list1[a] < list1[b]:  #如果m大于了n
#            list1[a] ,list1[b] =  list1[b],list1[a]#交换位置
# print(list1)