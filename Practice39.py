'''
Date: 2021-05-11 19:13:52
LastEditors: GC
LastEditTime: 2021-05-14 18:32:38
FilePath: \Python Work\.vscode\Python Practice100\Practice39.py
'''
# Practice 39(1):
    # --> You are given words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

    #     If the following string is given as input to the program:

    #     4
    #     bcdef
    #     abcdefg
    #     bcde
    #     bcdef
    #     Then, the output of the program should be:

    #     3
    #     2 1 1

    #     Make a list to get the input order and a dictionary to count the word frequency


# Solution 1:
# n = int(input())

# word_list = []
# word_dict = {}

# for i in range(n):
#     word = input()
#     if word not in word_dict:
#         word_list.append(word)
#     word_dict[word] = word_dict.get(word, 0) + 1

# print(len(word_list))
# for word in word_list:
#     print(word_dict[word], end=' ')




# Practice 39(2):
    # --> You are given a string.Your task is to count the frequency of letters of the string and print the letters in descending order of frequency.

    #     If the following string is given as input to the program:

    #     aabbbccde
    #     Then, the output of the program should be:

    #     b 3
    #     a 2
    #     c 2
    #     d 1
    #     e 1

    #     Count frequency with dictionary and sort by Value from dictionary Items



# Solution 1:
# word = input()
# dct = {}
# for i in word:
#     dct[i] = dct.get(i,0) + 1

# dct = sorted(dct.items(), key=lambda x: (-x[1],x[0]))
# for i in dct:
#     print(i[0],i[1])


# Solution 2:
# X = input()
# my_set = set(X)
# arr = []
# for item in my_set:
#     arr.append([item,X.count(item)])
# tmp = sorted(arr,key = lambda x: (-x[1],x[0]))

# for i in tmp:
#     print(i[0]+' '+str(i[1]))


# Solution 3:
# s = list(input())

# dict_count_ = {k:s.count(k) for k in s}
# list_of_tuples = [(k,v) for k,v in dict_count_.items()]
# list_of_tuples.sort(key = lambda x: x[1], reverse = True)

# for item in list_of_tuples:
#   print(item[0], item[1])



# Practice 39(3):
    # --> Write a Python program that accepts a string and calculate the number of digits and letters.

    #     Input

    #     Hello321Bye360

    #     Output

    #     Digit - 6
    #     Letter - 8

    #     Use isdigit() and isalpha() function


# Solution 1:
# word = input()
# digit,letter = 0,0
# for char in word:
#     digit+=char.isdigit()
#     letter+=char.isalpha()

# print('Digit -',digit)
# print('Letter -',letter)




# Practice 39(4):
    # --> Given a number N.Find Sum of 1 to N Using Recursion

    #     Input

    #     5

    #     Output

    #     15
      
    #     Make a recursive function to get the sum


# Solution 1:
# def rec(n):
#     if n == 0:
#         return n
#     return rec(n-1) + n


# n = int(input())
# sum = rec(n)
# print(sum)



# Solution 2:
# def summer(counter, n, current):
#     if n == 0:
#         return 0
#     if counter == n:
#         return current+n
#     else:
#         current = current + counter
#         counter += 1
#         return summer(counter, n, current)


# N = int(input("> "))
# print(summer(1, N, 0))






 
