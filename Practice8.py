'''
Date: 2021-04-06 15:11:46
LastEditors: GC
LastEditTime: 2021-07-16 17:23:41
FilePath: \Python Practice100\Practice8.py
'''
# Practice 8:
    # --> Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
    #     Suppose the following input is supplied to the program:
    #         without,hello,bag,world
    #     Then, the output should be:
    #         bag,hello,without,world


# Solution 1:
# i = [x for x in input().split(",")]
# i.sort()
# print(",".join(i))


# Solution 2:
# lst = input().split(",")
# lst.sort()
# print(",".join(lst))


# Solution 3:
# def my_func(e):
#      return e[0]


# lst = input("Please enter a comma seperated string: ").split(",")
# lst.sort(key=my_func)
# print(",".join(lst))


