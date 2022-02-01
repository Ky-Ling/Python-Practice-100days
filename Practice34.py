'''
Date: 2021-05-09 16:39:34
LastEditors: GC
LastEditTime: 2021-05-09 17:08:52
FilePath: \Python Work\.vscode\Python Practice100\Practice34.py
'''
# Practice 34(1):
    # --> Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
    #     Use zlib.compress() and zlib.decompress() to compress and decompress a string.


# Solution 1:
# import zlib
# s = 'hello world!hello world!hello world!hello world!'
# t = bytes(s, 'utf-8')
# z = zlib.compress(t)
# print(z)
# print(zlib.decompress(z))


# Solution 2:
# s = 'hello world!hello world!hello world!hello world!'
# y = bytes(s, 'utf-8')   # In Python 3 zlib.compress() accepts only DataType <bytes>
# x = zlib.compress(y)
# print(x)
# print(zlib.decompress(x))



# Practice 34(2):
    # --> Please write a program to print the running time of execution of "1+1" for 100 times
    #     Use timeit() function to measure the running time.


# Solution 1:
# from timeit import Timer
# t = Timer("for i in range(100): 1 + 1")
# print(t.timeit())


# Solution 2:
# import datetime
# before = datetime.datetime.now()

# for i in range(100):
#     x = 1 + 1

# after = datetime.datetime.now()
# execution_time = after - before
# print(execution_time.microseconds)


# Solution 3:
# import time 
# before = time.time()

# for i in range(100):
#     x = 1 + 1
# after = time.time()
# execution_time = after - before
# print(execution_time)



# Practice 34(3):
    # --> Please write a program to shuffle and print the list [3,6,7,8].
    #     Use shuffle() function to shuffle a list.


# Solution 1:
# from random import shuffle
# li = [2, 4, 5, 6, 7]
# shuffle(li)
# print(li)


# Solution 2:
# import random
# li = [22, 4, 5, 55, 667]
# random.shuffle(li)
# print(li)


# Solution 3:
# import random

# # shuffle with a chosen seed
# li = [2, 54, 6, 78]
# seed = 7
# random.Random(seed).shuffle(li)
# print(li)



# Practice 34(4):
    # --> Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] 
    #     and the object is in ["Hockey","Football"].
    #     Use list[index] notation to get a element from a list.



# Solution 1:
# subjects = ["I", "You"]
# verbs = ["Play", "Love"]
# objects = ["Hockey","Football"]
# for i in range(len(subjects)):
#     for j in range(len(verbs)):
#         for k in range(len(objects)):
#             sentences = "%s %s %s ." % (subjects[i], verbs[j], objects[k])
#             print(sentences)



# Solution 2:
# subjects=["I", "You"]
# verbs=["Play", "Love"]
# objects=["Hockey","Football"]

# for i in subjects:
#     for j in verbs:
#         for k in objects:
#             print("{} {} {}".format(i, j, k))


# Solution 3:
# import itertools
# subject = ["I", "You"]
# verb = ["Play", "Love"]
# objects = ["Hockey","Football"]

# sentences = [subject, verb, objects]
# n = list(itertools.product(*sentences))
# for i in n:
#     print(i)



# Solution 4:
from itertools import product

def question():
    subject = ["I", "You"]
    verb = ["Play", "Love"]
    object = ["Hockey", "Football"]
    
    prod = [p for p in product(range(2), repeat=3)]
    for combination in prod:
        print(f'{subject[combination[0]]} {verb[combination[1]]} {object[combination[2]]}')

question()