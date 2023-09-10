'''两个数字的平方和是2022，请问这2个数分别是多少'''

import math
# brutal force method
def fun(num,list=None):
    max = math.ceil(num**0.5) # ceiling 
    print("max =", max)
    i = 1
    while(i <= max):
        j = 1
        while(j <= max):
            if (i**2 + j**2) == num:
                return i,j
            j+=1
        i+=1
    return "Didn't found!"
print(fun(25))




# def test(num):
#     for a in range(1,num):
#         if (num - a*a)**0.5 in range(1,num):
#             print(a)
