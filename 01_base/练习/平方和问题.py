'''两个数字的平方和是2022，请问这2个数分别是多少'''


# 所有數都可以用質因數表示
# x^2 + y^2 = 2022
# 質數數對
# def fun(num, list=None):
#     if list is None:
#         list = []
#     for i in range(2, num):
#         while num % i == 0:
#             list.append(i)
#             num = int(num / i)
#             if num > 1:
#                 fun(num)
#     return list
# x = 9*5
# print(fun(x))

def fun(num,list=None):
    max = int(num**0.5)
    print("max =",max)
    i = 1
    while(i <= max):
        j = 1
        while(j <= max):
            if (i**2 + j**2) == num:
                return i,j
            j+=1
        i+=1
    return [1,2]
print(fun(25))
    



# def test(num):
#     for a in range(1,num):
#         if (num - a*a)**0.5 in range(1,num):
#             print(a)
