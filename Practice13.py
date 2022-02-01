'''
Date: 2021-04-15 19:28:36
LastEditors: GC
LastEditTime: 2021-04-22 10:08:15
FilePath: \Python Work\.vscode\Python Practice100\Practice13.py
'''
# Practice 13:
    # --> Write a program that accepts a sentence and calculate the number of letters and digits.

    #     Suppose the following input is supplied to the program:

    #     hello world! 123
    #     Then, the output should be:

    #     LETTERS 10
    #     DIGITS 3

# Solution 1:
# sentences = input()
# letter, digit = 0, 0
# for i in sentences:
#     if (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
#         letter += 1
#     if (i >= "0" and i <= "9"):
#         digit += 1
# print(f"{letter}\n{digit}") 

        

# Solution 2:
# s = input()
# d = {"DIGITS":0, "LETTERS":0}
# for x in s:
#     if x.isdigit():
#         d["DIGITS"] += 1
#     elif x.isalpha():
#         d["LETTERS"] += 1
#     else:
#         pass
    
# print("LETTERS", d["LETTERS"])
# print("DIGITS", d["DIGITS"])


# Solution 3:
# word = input()
# digit, letter = 0, 0
# for i in word:
#     if i.isalpha():               
#         letter += 1               # returns True if alphabet
#     if i.isdigit():               # returns True if numeric
#         digit += 1
# print(f"{digit}\n{letter}")       # two different types of formating method is shown in both solution


# Solution 4:
# import re

# input_string = input('> ')
# print()
# counter = {"LETTERS":len(re.findall("[a-zA-Z]", input_string)), "NUMBERS":len(re.findall("[0-9]", input_string))}

# print(counter)


# Solution 5:
# sentences = input("").split(" ")
# alp, digit = 0, 0
# for i in sentences:
#     lst = [char for char in i]
#     for j in lst:
#         if 64 < ord(j) < 123:
#             alp += 1
#         if j.isdigit():
#             digit += 1
# print(f"{alp}\n{digit}")


# Solution 6:
# from functools import reduce

# def count_letters_digits(counters,char_to_check):
#     counters[0] += char_to_check.isalpha()
#     counters[1] += char_to_check.isnumeric()
#     return counters

# print('LETTERS {0}\nDIGITS {1}'.format(*reduce(count_letters_digits,input(),[0,0])))