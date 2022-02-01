'''
Date: 2021-04-22 19:55:01
LastEditors: GC
LastEditTime: 2021-05-14 18:42:39
FilePath: \Python Work\.vscode\Python Practice100\Practice22.py
'''
# Practice 22:
    # --> Write a program to compute the frequency of the words from the input. 
    #     The output should output after sorting the key alphanumerically.

    #     Suppose the following input is supplied to the program:

    #     New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
    #     Then, the output should be:

    #     2:2
    #     3.:1
    #     3?:1
    #     New:1
    #     Python:5
    #     Read:1
    #     and:1
    #     between:1
    #     choosing:1
    #     or:2
    #     to:1


# Solution 1:
freq = {}
line = input()
for word in line.split():
    freq[word] = freq.get(word, 0) + 1
words = freq.keys()
words.sort()

for w in words:
    print("%s:%d" % (w, freq[w]))


# Solution 2:
#  

# Solution 3:
# s = input().split()
# dict = {}

# for i in s:
#     i = dict.setdefault(i, s.count(i))          # setdefault() function takes key & value to set it as dictionary.
# dict = sorted(dict.items())                     # items() function returns both key & value of dictionary as a list
#                                                 # and then sorted. The sort by default occurs in order of 1st -> 2nd key

# for i in dict:
#     print("%s:%d" % (i[0], i[1]))


# Solution 4:
# s = input().split()
# dict = {i:s.count(i) for i in s}        # sets dictionary as i-> split word & ss.count(i) -> total occurrence of i in ss
# dict = sorted(dict.items())             # items() function returns both key & value of dictionary as a list
#                                         # and then sorted. The sort by default occurs in order of 1st -> 2nd key

# for i in dict:
#     print("%s:%d" % (i[0], i[1]))


# Solution 5:
# from collections import Counter
# s = input().split()
# s = Counter(s)          # returns key & frequency as a dictionary
# s = sorted(s.items())   # returns as a tuple list

# for i in s:
#     print("%s:%d" % (i[0], i[1]))


# Solution 6:
# from pprint import pprint
# p = input().split()
# pprint({i:p.count(i) for i in p})