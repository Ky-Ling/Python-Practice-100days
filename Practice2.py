'''
Date: 2021-03-28 15:04:00
LastEditors: GC
LastEditTime: 2021-07-15 15:41:17
FilePath: \Python Practice100\Practice2.py
'''
# Practice 2:
#     --> Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.
#     --> Suppose the following input is supplied to the program: 8 Then, the output should be:40320


# My Solution:
# num = int(input("Please input a number: "))
# sum = 1
# while num != 0:
#     sum *= num
#     num = num - 1
# print(sum)


# Solution 1:
# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)


# x = int(input("Please input a number: "))
# print(fact(x))


# Solution 2:
# n = int(input()) #input() function takes input as string type
#                  #int() converts it to integer type
# fact = 1
# i = 1
# while i <= n:
#     fact = fact * i
#     i = i + 1
# print(fact)


# Solution 3:
# n = int(input()) #input() function takes input as string type
#                  #int() converts it to integer type
# fact = 1 
# for i in range(1, n + 1):
#     fact = fact * i
# print(fact)


# Solution 4: (Using Lambge Function)
# n = int(input())
# def shortFact(x): return 1 if x <= 1 else x * shortFact(x - 1)
# print(shortFact(n)) 


# Solution 5:
# while True:
#     try:
#         num = int(input("Enter a number: "))
#         break
#     except ValueError as err:
#         print(err)

# org = num
# fact = 1
# while num:
#     fact = num * fact
#     num = num - 1
# print(f'the factorial of {org} is {fact}')


# Solution 6:
# from functools import reduce

# def fun(acc, item):
# 	return acc * item

# num = int(input())
# print(reduce(fun, range(1, num+1), 1))