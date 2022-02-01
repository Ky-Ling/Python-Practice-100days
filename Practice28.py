'''
Date: 2021-04-25 20:43:28
LastEditors: GC
LastEditTime: 2021-05-06 10:40:05
FilePath: \Python Work\.vscode\Python Practice100\Practice28.py
'''
# Practice 28(1)：
    # --> With a given tuple (1,2,3,4,5,6,7,8,9,10), 
    #     write a program to print the first half values in one line and the last half values in one line.


# Solution 1:
# tup = (1,2,3,4,5,6,7,8,9,10)
# t1 = tup[:5]
# t2 = tup[5:]
# print(t1)
# print(t2)


# Solution 2:
# tpl = (1,2,3,4,5,6,7,8,9,10)
# for i in range(0, 5):
#     print(tpl[i], end=" ")
# print()
# for i in range(5, 10):
#     print(tpl[i], end=" ")


# Solution 3:
# tpl = (1,2,3,4,5,6,7,8,9,10)
# t1, t2 = [], []

# for i in range(0, 5):
#     t1.append(tpl[i])

# for i in range(5, 10):
#     t2.append(tpl[i])

# print(t1)
# print(t2)


# Solution 4:
# tpl = (1,2,3,4,5,6,7,8,9,10)
# length = int(len(tpl) / 2)
# print(tpl[:length], tpl[length:])


# Solution 5:
# tp = (1,2,3,4,5,6,7,8,9,10)
# print('The Original Tuple:', tp)
# [print('Splitted List :{List}'.format(List = tp[x : x + 5])) for x in range(0, len(tp), 5)]


# Solution 6:
# tup = [i for i in range(1, 11)]
# print(f'{tuple(tup[:5])} \n {tuple(tup[5:])}')




# Practice 28(2)：
    # --> Write a program to generate and print another tuple whose values are even numbers(偶数) in the given tuple (1,2,3,4,5,6,7,8,9,10).


# Solution 1:
# tp = (1,2,3,4,5,6,7,8,9,10)
# li = list()
# for i in tp:
#     if tp[i] % 2 == 0: 
#         li.append(tp[i])
# tp2 = tuple(li)
# print(tp2)


# Solution 2:
# tp = (1,2,3,4,5,6,7,8,9,10)
# print(tuple(i for i in tp if i % 2 == 0))

# Solution 3:
# tp = (1,2,3,4,5,6,7,8,9,10)
# tp1 = tuple(filter(lambda x : x % 2 == 0, tp))      # Lambda function returns True if found even element.
# print(tp1)                                          # Filter removes data for which function returns False




# Practice 28(2)
    # --> Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

# Solution 1:
# li = [1,2,3,4,5,6,7,8,9,10]
# squaredNumbers = map(lambda x: x ** 2 , li)     # returns map type object data
# print(list(squaredNumbers))                     # converting the object into list
  

# Solution 2:
# def ss(items):
#     return items ** 2

# lst = [i for i in range(1, 11)]

# print(list(map(ss, lst)))



# Practice 28(3)：
    # --> Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].


# Solution 1:
# li = [1,2,3,4,5,6,7,8,9,10]
# evenNumbers = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, li))
# print(list(evenNumbers))


# Solution 2:
# def even(x):
#     return x % 2 == 0
# def sq(x):
#     return x * x
# li = [1,2,3,4,5,6,7,8,9,10]
# evenNumber = map(sq, filter(even, li))      # first filters number by even number and the apply map() on the resultant elements
# print(list(evenNumber))


# Solution 3:
# def even(items):
#     if items % 2 == 0:
#         return items ** 2

# lst = [i for i in range(1, 11)]
# print(list(filter(lambda j: j is not None, list(map(even, lst)))))


