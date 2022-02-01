'''
Date: 2021-04-06 16:45:19
LastEditors: GC
LastEditTime: 2021-07-16 17:40:58
FilePath: \Python Practice100\Practice10.py
'''
# Practice 10:
    # --> Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
    #     Suppose the following input is supplied to the program:
        
    #     hello world and practice makes perfect and hello world again
        
    #     Then, the output should be:
        
    #     again and hello makes perfect practice world
    


# Solution 1:
# s = input().split()
# for i in s:
#     if s.count(i) > 1:  #count function returns total repeatation of an element that is send as argument
#         s.remove(i)     # removes exactly one element per call
# s.sort()
# print(" ".join(s))


# Solution 2:
# s = input()
# words = [word for word in s.split(" ")]
# print(" ".join(sorted(list(set(words)))))


# Solution 3:
# words = input().split()
# [words.remove(i) for i in words if words.count(i) > 1]
# words.sort()
# print(" ".join(words))


# Solution 4:
# word = sorted(list(set(input().split())))
# print(" ".join(word))


# Solution 5:
# s = input().split()
# lst = []
# for i in s:
#     if i not in lst:
#         lst.append(i)
# print(" ".join(sorted(lst)))