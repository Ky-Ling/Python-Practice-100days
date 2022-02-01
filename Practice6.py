'''
Date: 2021-03-29 16:11:04
LastEditors: GC
LastEditTime: 2021-07-16 16:53:27
FilePath: \Python Practice100\Practice6.py
'''
# Practice 6:
#     --> Write a program that calculates and prints the value according to the given formula:
            # Q = Square root of [(2 _ C _ D)/H]
            # Following are the fixed values of C and H:
            # C is 50. H is 30.
            
            # D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:
            # 100,150,180
            # The output of the program should be:

            # 18,22,24


# Solution 1:
# import math
# c = 50
# h = 30
# value = []
# items = [x for x in input().split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

# print(','.join(value)) 

# Solution 2:
# from math import sqrt # import specific functions as importing all using *
#                       # is bad practice

# C, H = 50, 30

# def calc(D):
#     return sqrt((2 * C * D) / H)

# D = [int(i) for i in input().split(',')] # splits in comma position and set up in list
# D = [int(i) for i in D]                  # converts string to integer
# D = [calc(i) for i in D]                 # returns floating value by calc method for every item in D
# D = [round(i) for i in D]                # All the floating values are rounded
# D = [str(i) for i in D]                  # All the integers are converted to string to be able to apply join operation

# print(",".join(D))


# Solution 3:
# from math import sqrt

# C,H = 50,30

# def calc(D):
#     return sqrt((2 * C * D) / H)

# D = input().split(',')                     # splits in comma position and set up in list
# D = [str(round(calc(int(i)))) for i in D]  # using comprehension method. It works in order of the previous code
# print(",".join(D))


# Solution 4:
# from math import sqrt
# C,H = 50,30

# def calc(D):
#     return sqrt((2*C*D)/H)

# print(",".join([str(int(calc(int(i)))) for i in input().split(',')]))



# Solution 5:
# from math import * # importing all math functions
# C,H = 50,30

# def calc(D):
#     D = int(D)
#     return str(int(sqrt((2*C*D)/H)))

# D = input().split(',')
# D = list(map(calc,D))   # applying calc function on D and storing as a list
# print(",".join(D))



# Solution 6:
# from math import sqrt
# C, H = 50, 30
# mylist = input().split(',')
# print(*(round(sqrt(2*C*int(D)/H)) for D in mylist), sep=",")


# Soluiton 7:
my_list = [int(x) for x in input('').split(',')]
C, H, x = 50, 30, []

for D in my_list:
    Q = ((2*C*D)/H)**(1/2)
    x.append(round(Q))

print(','.join(map(str, x)))