'''
Date: 2021-04-15 20:21:33
LastEditors: GC
LastEditTime: 2021-04-22 10:12:48
FilePath: \Python Work\.vscode\Python Practice100\Practice14.py
'''
# Practice 14:
    # --> Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

    #     Suppose the following input is supplied to the program:

    #     Hello world!
    #     Then, the output should be:

    #     UPPER CASE 1
    #     LOWER CASE 9


# Solution 1:
# sentences = input()
# Upper, lower = 0, 0
# for i in sentences:
#     if i.isupper():
#         Upper += 1
#     if i.islower():
#         lower += 1

# print(f"{Upper}\n{lower}")


# Solution 2:
# s = input()
# d = ["UPPER CASE":0, "LOWER CASE":0]
# for i in s:
#     if i.isupper():
#         d["UPPER CASE"] += 1
#     elif i.islower():
#         d["LOWER CASE"] += 1
#     else:
#         pass
# print("UPPER CASE", d["UPPER CASE"])
# print("LOWER CASE", d["LOWER CASE"])


# Solution 3:
# sentences = input()
# lower, upper = 0, 0
# for i in sentences:
#     if i >= "a" and i <= "z":
#         lower += 1
#     if i >= "A" and i <= "Z":
#         upper += 1
# print("UPPER CASE {0}\nLOWER CASE {1}".format(upper, lower))


# Solution 4:
# sentences = input()
# lower, upper = 0, 0
# for i in sentences:
#     lower += i.islower()
#     upper += i.isupper()
# print("UPPER CASE {0}\nLOWER CASE {1}".format(upper, lower))


# Solution 5:
# sentences = input()
# upper = sum(1 for i in sentences if i.isupper())
# lower = sum(1 for i in sentences if i.islower())
# print("UPPER CASE {0}\nLOWER CASE {1}".format(upper, lower))


# Solution 6:
# sentences = input("Please enter a string: ")
# upper = 0
# lower = 0
# for i in sentences:
#     if i.isupper() == True:
#         upper += 1
#     if i.islower() == True:
#         lower += 1

# print("UPPER CASE", upper)
# print("LOWER CASE", lower)

