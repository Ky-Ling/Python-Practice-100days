'''
Date: 2021-03-30 15:57:52
LastEditors: GC
LastEditTime: 2021-07-16 17:16:47
FilePath: \Python Practice100\Practice7.py
'''
# Practice 7:

#    --> Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
#        The element value in the i-th row and j-th column of the array should be i _ j.*
#        Note: i=0, 1.., X-1; j=0, 1, ..., ­Y-1. Suppose the following inputs are given to the program: 3, 5
#        Then, the output of the program should be:
#        [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]


# Solution 1:
# input_str = input()
# dimensions = [int(x) for x in input_str.split(',')]
# # 行
# row_num = dimensions[0] 
# # 列
# col_num = dimensions[1] 
# multilist = [[0 for col in range(col_num)] for row in range(row_num)]

# for row in range(row_num):
#     for col in range(col_num):
#         multilist[row][col] = row * col

# print(multilist)


# Solution 2:
# x, y = map(int, input().split(','))  对于函数map(function, iterable,...) 
#                                               --> 一般情况下，对可迭代函数“Iterable”中的每一个元素应用“Function”方法，将结果作为list返回
# lst = []

# for i in range(x):
#     tmp = []
#     for j in range(y):
#         tmp.append(i * j)
#     lst.append(tmp)

# print(lst)


# Solution 3:
# x, y = map(int, input().split(','))
# lst = [[i * j for j in range(y)] for i in range(x)]
# print(lst)


 

