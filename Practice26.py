'''
Date: 2021-04-25 20:22:16
LastEditors: GC
LastEditTime: 2021-04-25 20:37:20
FilePath: \Python Work\.vscode\Python Practice100\Practice26.py
'''
# Practice 26:
    # --> Define a function that can accept two strings as input and print the string with maximum length in console.
    #     If two strings have the same length, then the function should print all strings line by line.


# Solution 1:
# def printValue(length1, length2):
#     len1 = len(length1)
#     len2 = len(length2)

#     if len1 > len2:
#         print(length1)
#     elif len1 < len2:
#         print(length2)
#     else:
#         print(length1)
#         print(length2)
# printValue("One", "Three")


# Solution 2:
# def printValue(s1, s2):
#     len1 = len(s1)
#     len2 = len(s2)
    
#     if len1 > len2:
#         print(s1)
#     elif len1 < len2:
#         print(s2)
#     else:
#         print(s1)
#         print(s2)
# s1, s2 = input().split()
# printValue(s1, s2)
        
    

# Solution 3:
func = lambda a, b : print(max((a, b), key = len)) if len(a) != len(b) else print(a + '\n' + b)