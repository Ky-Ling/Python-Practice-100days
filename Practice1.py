'''
Date: 2021-03-28 14:42:47
LastEditors: GC
LastEditTime: 2021-12-10 19:59:13
FilePath: \Python Practice100\Practice1.py
'''

# Practice 1:
#    --> Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#    --> between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.


# Solution 1:
# for i in range(2000, 3201):
#     if (i % 7 == 0) and (i % 5 != 0):
#         print(i, end=",")

# Solution 2:
# l=[]
# for i in range(2000, 3201):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))
# print(','.join(l))

# Solution 3:
# for i in range(2000,3201):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i, end=',')
# print("\b")


# Solution 4: Using generators and list comprehension
# print(*(i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0), sep=",")
