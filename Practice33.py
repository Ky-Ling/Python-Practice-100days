'''
Date: 2021-05-09 15:42:04
LastEditors: GC
LastEditTime: 2021-05-09 16:39:01
FilePath: \Python Work\.vscode\Python Practice100\Practice33.py
'''
# Practice 33(1):
    # -->  Please write assert statements to verify that every number in the list [2,4,6,8] is even.
    #      Use "assert expression" to make assertion.
        

# Solution 1:
# li = [2, 4, 6, 7, 8]
# for i in li:
#     assert i % 2 == 0, "{} is not an even number".format(i)
    


# Practice 33(2):
    # --> Please write a program which accepts basic mathematic expression from console and print the evaluation result.

    #     Example: If the following n is given as input to the program:

    #     35 + 3
    #     Then, the output of the program should be:
    #     38

    #     Use eval() to evaluate an expression.


# Solution 1:
# expression = input()
# print(eval(expression))



# Practice 33(3):
    # --> Please write a binary search function which searches an item in a sorted list. 
    #     The function should return the index of element to be searched in the list.
    #     Use if/elif to deal with conditions.


# Solution 1 (to be written)：
# def bin_search(lst, item):
#     low = 0
#     high = len(lst) - 1
    
#     while low <= high:
#         mid = round((low + high) / 2)

#         if lst[mid] == item:
#             return mid
#         elif lst[mid] > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None

# lst = [1, 3, 5, 7]
# print(bin_search(lst, 9))


# Solution 2:
# def binary_search_Ascending(array, target):
#     lower = 0
#     upper = len(array)
#     print('Array Length:',upper)
#     while lower < upper:
#         x = (lower + upper) // 2
#         print('Middle Value:',x)
#         value = array[x]
#         if target == value:
#             return x
#         elif target > value:
#             lower = x
#         elif target < value:
#             upper = x

# Array = [1,5,8,10,12,13,55,66,73,78,82,85,88,99]
# print('The Value Found at Index:',binary_search_Ascending(Array, 82))


# Solution 3:
# idx = 0
# def bs(num,num_list):
#     global idx
#     if (len(num_list) == 1):
#         if num_list[0] == num:
#             return idx
#         else:
#             return "No exit in the list"
#     elif num in num_list[:len(num_list)//2]:
#         return bs(num,num_list[:len(num_list)//2])
#     else:
#         idx += len(num_list)//2
#     return bs(num,num_list[len(num_list)//2:])

# print(bs(66,[1,5,8,10,12,13,55,66,73,78,82,85,88,99,100]))



# Practice 33(4):
    # --> Please generate a random float where the value is between 10 and 100 using Python module.
    #     Use random.random() to generate a random float in [0,1].


# Solution 1:
# import random
# print(random.random() * 100)


# Solution 2:
# import random
# print(random.uniform(10, 100))



# Practice 33(5):
    # --> Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.
    #     Use random.choice() to a random element from a list.


# Solution 1:
# li = [2, 4, 6, 8]
# import random
# print(random.choice([i for i in range(11) if i % 2 == 0]))



# Solution 2:
# import random
# print(random.choice([i for i in range(0, 11, 2)]))



# Practice 33(6):
    # --> Please write a program to output a random number, which is divisible by 5 and 7, 
    #     between 10 and 150 inclusive using random module and list comprehension.
    #     Use random.choice() to a random element from a list.


# Solution 1:
# import random
# print(random.choice([i for i in range(10, 151) if i % 5 == 0 and i % 7 == 0]))


# Solution 2:
# import random
# print(random.choice([i for i in range(10, 151) if i % 35 == 0]))


# Practice 33(7):
    # --> Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
    #     Use random.sample() to generate a list of random values.


# Solution:
# import random
# print(random.sample(range(100, 201), 5))



# Practice 33(8):
    # --> Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
    #     Use random.sample() to generate a list of random values.


# Solution 1:
# import random
# print(random.sample([i for i in range(100, 201) if i % 2 == 0], 5))


# Solution 2:
# import random
# print(random.sample(range(100, 201, 2), 5))


# Practice 33(9):
    # --> Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.
    #     Use random.sample() to generate a list of random values.

# Solution 1:
# import random
# print(random.sample([i for i in range(1, 1001) if i % 35 == 0], 5))




# Practice 33(10):
    # --> Please write a program to randomly print a integer number between 7 and 15 inclusive.
    #     Use random.randrange() to a random integer in a given range.


# Solution :
import random
print(random.randrange(7, 16))