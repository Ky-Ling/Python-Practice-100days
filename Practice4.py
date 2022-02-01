'''
Date: 2021-03-29 15:36:29
LastEditors: GC
LastEditTime: 2021-07-15 15:59:05
FilePath: \Python Practice100\Practice4.py
'''

# Practice 4:
#    --> Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.


# Solution 1:
# list = input("Please input a series of numbers: ")
# l = list.split(",")
# t = tuple(l)
# print(l)
# print(t)


# Solution 2:
# lst = input().split(',')  # the input is being taken as string and as it is string it has a built in
#                           # method name split. ',' inside split function does split where it finds any ','
#                           # and save the input as list in lst variable

# tpl = tuple(lst)          # tuple method converts list to tuple
# print(lst)
# print(tpl)



# Solution 3:
# print(tuple(input("Enter a series of numbers separated by a comma :").split(',')))
