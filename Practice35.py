'''
Date: 2021-05-10 15:16:05
LastEditors: GC
LastEditTime: 2021-05-10 15:44:58
FilePath: \Python Work\.vscode\Python Practice100\Practice35.py
'''
# Practice 35(1):
    # --> Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].
    #     Use list comprehension to delete a bunch of element from a list.



# Solution 1:
# li = [5,6,77,45,22,12,24]
# li = [x for x in li if x % 2 != 0]
# print(li)



# Solution 2:
# def isEven(n):
#     return n % 2 != 0

# li = [5,6,77,45,22,12,24]
# lst = list(filter(isEven, li))
# print(lst)



# Solution 3:
# li = [5,6,77,45,22,12,24]
# lst = list(filter(lambda n: n % 2 != 0 , li))
# print(lst)



# Practice 35(2):
    # --> By using list comprehension, 
    #     please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].



# Solution 1:
# li = [12,24,35,70,88,120,155]    
# lst = [x for x in li if x % 35 != 0]
# print(lst)



# Practice 35(3):
    # --> By using list comprehension, 
    #     please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
        
    #     Use list comprehension to delete a bunch of element from a list. Use enumerate() to get (index, value) tuple.



# Solution 1:
# li = [12,24,35,70,88,120,155]
# lst = [x for (i, x) in enumerate(li) if i % 2 != 0 and i <= 6]
# print(lst)


# Solution 2:
# li = [12,24,35,70,88,120,155]
# lst = [li[i] for i in range(len(li)) if i % 2 != 0 and i <= 6]
# print(lst)


# Solution 3:
# orig_lst = [12,24,35,70,88,120,155]
# indices = [0, 2, 4, 6]
# new_list= [i for(j, i) in enumerate(orig_lst) if j not in indices]
# print(new_list)




# Practice 35(4):
    # --> By using list comprehension, please write a program 
    #     to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].
    #     Use list comprehension to delete a bunch of element from a list. Use enumerate() to get (index, value) tuple.


# Solution 1:
# li = [12,24,35,70,88,120,155]
# lst = [x for(i, x) in enumerate(li) if i < 3 or i > 4]
# print(lst)


# Solution 2:
#to be written
# li = [12,24,35,70,88,120,155]
# li = [li[i] for i in range(len(li)) if i < 3 or i > 4]
# print(li)



# Solution 3:
# orig_list = [12,24,35,70,88,120,155]
# new_list = [i for(j, i) in enumerate(orig_list) if j not in range(1, 4)]
# print(new_list)




# Solution 4:
# orig_list = [12,24,35,70,88,120,155]
# lst = [i for i in orig_list if orig_list.index(i) not in range(2, 5)]
# print(lst)



# Practice 35(5):
    # --> By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
    #     Use list comprehension to make an array.


# Solution:
array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)