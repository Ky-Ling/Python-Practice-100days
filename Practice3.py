'''
Date: 2021-03-28 15:49:11
LastEditors: GC
LastEditTime: 2021-07-15 15:52:15
FilePath: \Python Practice100\Practice3.py
'''
# Pactice 3:
    # --> With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). 
    # --> and then the program should print the dictionary.Suppose the following input is supplied to the program: 8
    # --> Then, the output should be:
    #         --> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


# Solution 1:
# num = int(input("Please input a number: "))
# 创建一个字典
# d = dict()  
# for i in range(1, num + 1):
#     d[i] = i * i
# print(d)

# Solution 2:
# n = int(input())
# ans = {}
# for i in range (1, n + 1):
#     ans[i] = i * i
# print(ans)


# Solution 3:
# n = int(input())
# ans={i : i * i for i in range(1, n + 1)}
# print(ans)

# Solution 4:
# try:
#     num = int(input("Enter a number: "))
# except ValueError as err:
#     print(err)

# diction = dict()
# for item in range(num + 1):
#     if item == 0:
#         continue
#     else:
# 	    diction[item] = item * item
# print(diction)


# Solution 5:
num = int(input("Number: "))
print(dict(enumerate([i*i for i in range(1, num+1)], 1)))