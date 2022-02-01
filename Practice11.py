'''
Date: 2021-04-08 11:05:10
LastEditors: GC
LastEditTime: 2021-04-13 16:07:31
FilePath: \Python Work\.vscode\Python Practice100\Practice11.py
'''
#Practice 11:
#     --> Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

#         Example:

#         0100,0011,1010,1001
#         Then the output should be:

#         1010
#         Notes: Assume the data is input by console.


# Solution 1:
# value = []
# items = [x for x in input().split(",")]
# for p in items:
#     intp = int(p, 2)
#     if not intp % 5:
#         value.append(p)
# print(" ".join(value))


# Solution 2:
# def check(x):                       # check function returns true if divisible by 5
#     return int(x, 2) % 5 == 0       # int(x,b) takes x as string and b as base from which
#                                     # it will be converted to decimal
# data = input().split(",")
# data = list(filter(check, data))    # in filter(func,object) function, elements are picked from 'data' if found True by 'check' function
# print(" ".join(data))


# Solution 3:
# data = input().split(",")
# data = list(filter(lambda i: int(i, 2) % 5 == 0, data))  # lambda is an operator that helps to write function of one line
# print(" ".join(data))


# Solution 4:
# data = input().split(",")
# data = [num for num in data if int(num, 2) % 5 == 0]
# print(" ".join(data))


# Solution 5:
print(*(binary for binary in input().split(',') if int(binary, base = 2) % 5 == 0