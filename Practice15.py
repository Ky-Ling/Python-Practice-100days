'''
Date: 2021-04-16 15:12:04
LastEditors: GC
LastEditTime: 2021-04-22 10:15:41
FilePath: \Python Work\.vscode\Python Practice100\Practice15.py
'''
# Practice 15:
    # --> Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

    #     Suppose the following input is supplied to the program:

    #     9
    #     Then, the output should be:

    #     11106


# Solution 1:
# s = input()
# s1 = int("%s" % s)
# s2 = int("%s%s" % (s, s))
# s3 = int("%s%s%s" % (s, s, s))
# s4 = int("%s%s%s%s" % (s, s, s, s))
# print(s1 + s2 + s3 + s4)


# Solution 2:
# a = input()
# total = int(a) + int(2*a) + int(3*a) + int(4*a)   # N*a=Na, for example  a="23", 2*a="2323",3*a="232323"
# print(total)


# Solution 3:
# from functools import reduce
# x = input('please enter a digit:')
# reduce(lambda x, y: int(x) + int(y), [x * i for i in range(1,5)])


# Solution 4:
# def practice(string_digit):
#     return sum(int(string_digit * i) for i in range(1, 5))
# a = input()
# print(practice(a))


# Solution 5:
a = input()
prinsum(intt((a * i) for i in range(1, 5)))