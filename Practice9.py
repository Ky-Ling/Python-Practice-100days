'''
Date: 2021-04-06 16:10:40
LastEditors: GC
LastEditTime: 2021-07-16 17:36:40
FilePath: \Python Practice100\Practice9.py
'''
# Practice 9:
    # --> Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
    #     Suppose the following input is supplied to the program:
        
    #     Hello world
    #     Practice makes perfect
        
    #     Then, the output should be:
        
    #     HELLO WORLD
    #     PRACTICE MAKES PERFECT


# Solution 1:
# lines = []
# while True:
#     s = input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break
# for sentences in lines:
#     print(sentences)

# Solution 2:
# lst = []
# while True:
#     s = input()
#     if len(s) == 0:
#         break
#     lst.append(s.upper())
# for sentences in lst:
#     print(sentences)


# Solution 3:
# def user_input():
#     while True:
#         s = input()
#         if not s:
#             return
#         yield 
        

# for line in map(str.upper, user_input()):
#     print(line)


# Solution 4:
# def inputs():
#     while True:
#         string = input()
#         if not string:
#             return
#         yield string

# print(*(line.upper() for line in inputs()),sep='\n')
