'''
Date: 2021-04-25 20:37:47
LastEditors: GC
LastEditTime: 2021-04-27 15:24:24
FilePath: \Python Work\.vscode\Python Practice100\Practice27.py
'''
# Practice 27(1):
    # --> Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
    #     Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops.

# Solution 1:
# def printDict():
#     d = dict()
#     for i in range(1, 21):
#         d[i] = i * i
#         print(d)

# printDict()


# Solution 2:
# def printDict():
#     dict = {i: i * i for i in range(1, 21)}
#     print(dict)

# printDict()


# Practice 27(2):
    # --> Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. 
    #     The function should just print the keys only.

# Solution 1:
# def printDict():
#     d = dict()
#     for i in range(1, 21):
#         d[i] = i ** 2
#     for k in d.keys():
#         print(k)

# printDict()


# Solution 2:
# def printDict():
#     dict = {i: i ** 2 for i in range(1, 21)}
#     print(dict.keys())      # print keys of a dictionary
# printDict()


# Practice 27(3):
    # --> Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

# Solution 1:
# def printlist():
#     lst = list()
#     for i in range(1, 21):
#         lst.append(i ** 2)
#     print(lst)
# printlist()


# Solution 2:
# def printlist():
#     list = {i: i ** 2 for i in range(1, 21)}
#     print(list)
# printlist()
    

# Practice 27(4):
    # --> Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
    #     Then the function needs to print the first 5 elements in the list.

# Solution 1:
# def printlist():
#     lst = list()
#     for i in range(1, 21):
#         lst.append(i ** 2)
#     print(lst[:5])
# printlist()
    
    

# Solution 2:
# def printlist():
#     lst = [i ** 2 for i in range(1, 21)]
#     for i in range(5):
#         print(lst[i])
        
# printlist()


# Solution 3:
# def squares(n):
#     squares_list = [i ** 2 for i in range(1, n + 1)]
#     print(squares_list[0 : 5])

# squares(20)
    

# Solution 4:
# func = lambda :print([i ** 2 for i in range(1, 21)][:5])