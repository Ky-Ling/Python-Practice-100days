'''
Date: 2021-05-06 20:05:54
LastEditors: GC
LastEditTime: 2021-05-09 15:43:02
FilePath: \Python Work\.vscode\Python Practice100\Practice32.py
'''
# Practice 32(1):
    # --> Write a program to compute:
    #     f(n)=f(n-1)+100 when n>0 and f(0)=0
        
    #     with a given n input by console (n>0).

    #     Example: If the following n is given as input to the program:
    #     5
    #     Then, the output of the program should be:
    #     500

    #     In case of input data being supplied to the question, it should be assumed to be a console input.

    #     We can define recursive function in Python.


# Solution 1:
# def f(n):
#     if n == 0:
#         return 0
#     else:
#         return f(n - 1) + 100

# n = int(input())
# print(f(n))


# Solution 2:
# n = int(input())
# f = lambda x: f(x - 1) + 100 if x > 0 else 0
# print(f(n)) 



# Practice 32(2):
    # --> The Fibonacci Sequence is computed based on the following formula:

    #     f(n)=0 if n=0
    #     f(n)=1 if n=1
    #     f(n)=f(n-1)+f(n-2) if n>1

    #     Please write a program to compute the value of f(n) with a given n input by console.

    #     Example: If the following n is given as input to the program:

    #     7
    #     Then, the output of the program should be:
    #     13

    #     In case of input data being supplied to the question, it should be assumed to be a console input.


# Solution 1:
# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1   
#     else:
#         return f(n - 1) + f(n - 2)

# n = int(input())
# print(f(n))


# Solution 2:
# def f(n):
#     if n < 2:
#         return n
#     else:
#         return f(n - 1) + f(n - 2)

# n = int(input())
# print(f(n)) 


# Solution 3:
# n = int(input())
# f = lambda x: 0 if x == 0 else 1 if x == 1 else f(x - 1) + f(x - 2)
# print(",".join([str(f(x))] for x in range(0, n + 1)))



# Practice 32(3):
    # --> The Fibonacci Sequence is computed based on the following formula:

    #     f(n)=0 if n=0
    #     f(n)=1 if n=1
    #     f(n)=f(n-1)+f(n-2) if n>1
    #     Please write a program to compute the value of f(n) with a given n input by console.

    #     Example: If the following n is given as input to the program:

    #     7
    #     Then, the output of the program should be:

    #     0,1,1,2,3,5,8,13
    #     In case of input data being supplied to the question, it should be assumed to be a console input.

    #     We can define recursive function in Python. 
    #     Use list comprehension to generate a list from an existing list. Use string.join() to join a list of strings.


# Solution 1:
# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return f(n - 1) + f(n - 2)
# n = int(input())
# values = [str(f(x)) for x in range(0, n + 1)]
# print(",".join(values))


# Solution 2:
# def f(n):
#     if n < 2:
#         fibo[n] = n
#         return fibo[n]
#     fibo[n] = f(n - 1) + f(n - 2)
#     return fibo[n]

# n = int(input())
# fibo = [0] * (n + 1)                # initialize a list of size (n+1)
# f(n)                                # call once and it will set value to fibo[0-n]
# fibo = [str(i) for i in fibo]       # converting integer data to string type
# print(",".join(fibo))               # joining all string element of fibo with ',' character


# Solution 3:
# def fibo(n):
#     if n < 2:
#         return n
#     return fibo(n -1) +fibo(n - 2)

# def print_fiblist(n):
#     fib_list = [(str(fibo(i))) for i in range(0, n + 1)]
#     return print(",".join(fib_list))

# n = int(input())
# print_fiblist(n)


# Solution 4:
# def f(n):
#     if n == 0:
#         return [0]
#     if n == 1:
#         return [0, 1]
#     sequence = [0, 1]
#     a, b = 0, 1
#     for x in range(2, n + 1):
#         c = a + b
#         sequence.append(c)
#         a = b
#         b = c
#     return sequence

# print(f(10))



# Practice 32(4):
    # --> Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

    #     Example: If the following n is given as input to the program:

    #     10
    #     Then, the output of the program should be:
    #     0,2,4,6,8,10

    #     In case of input data being supplied to the question, it should be assumed to be a console input.


# Solution 1:
# def EvenGenerator(n):
#     i = 0
#     while i < n:
#         if i % 2 == 0:
#             yield i
#         i += 1
    
# n = int(input())
# values = []
# for i in EvenGenerator(n):
#     values.append(str(i))

# print(",".join(values))


# Solution 2:
# n = int(input())
# for i in range(0, n + 1, 2):
#     if i < n - 1:
#         print(i, end=",")
#     else:
#         print(i)



# Practice 32(5):
    # --> Please write a program using generator to 
    #     print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
        
    #     Example: If the following n is given as input to the program:

    #     100
    #     Then, the output of the program should be:
    #     0,35,70

    #     In case of input data being supplied to the question, it should be assumed to be a console input.



# Solution 1:
# def NumGenerator(n):
#     for i in range(n + 1):
#         if i % 5 == 0 and i % 7 == 0:
#             yield i

# n = int(input())
# values = []
# for i in NumGenerator(n):
#     values.append(str(i))

# print(",".join(values))
    

# Solution 2:
def NumGenerator(n):
    for i in range(n + 1):
        if i % 35 == 0:    # 5*7 = 35, if a number is divisible by a & b then it is also divisible by a*b
            yield i

n = int(input())
resp = [str(i) for i in NumGenerator(n)]
print(",".join(resp))