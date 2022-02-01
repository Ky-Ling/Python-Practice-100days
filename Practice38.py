'''
Date: 2021-05-11 18:46:48
LastEditors: GC
LastEditTime: 2021-05-11 19:12:29
FilePath: \Python Work\.vscode\Python Practice100\Practice38.py
'''
# Practice 38(1):
        # Given the participants'score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

        # If the following string is given as input to the program:

        # 5
        # 2 3 6 6 5
        # Then, the output of the program should be:
        # 5

        # Make the scores unique and then find 2nd best number


# Solution 1:
# n = int(input())
# arr = map(int, input().split())
# arr = list(set(arr))
# arr = sorted(arr)
# print(arr[-2])


# Solution 2:
# num = int(input("Enter num: "))
# L = []

# while True:
#     L.append(num)
#     num = int(input("Enter another: "))
#     if num == 0:
#         break

# L1 = list(set(L[:]))
# L2 = sorted(L1)
# print(L2)

# print(f'The runner up is {L2[-2]}')



# Solution 3:
# num = int(input())
# scores = list(map(int, input().split(' ')))
# winner = max(scores)
# lst = []

# if len(scores) != num:
#     print('length of score is greater than input given')
# else:
#     for score in scores:
#         if winner > score:
#             lst.append(score)

# runnerup = max(lst)
# print(runnerup)



# Practice 38(2):
    # --> You are given a string S and width W. Your task is to wrap the string into a paragraph of width.

    #     If the following string is given as input to the program:

    #     ABCDEFGHIJKLIMNOQRSTUVWXYZ
    #     4
    #     Then, the output of the program should be:
    #     ABCD
    #     EFGH
    #     IJKL
    #     IMNO
    #     QRST
    #     UVWX
    #     YZ

    #     Use wrap function of textwrap module



# Solution 1:
# import textwrap

# def wrap(string, max_width):
#     string = textwrap.wrap(string,max_width)
#     string = "\n".join(string)
#     return string

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)



# Solution 2:
# import textwrap
# string = input()
# width = int(input())
# print(textwrap.fill(string, width))



# Solution 3:
# from textwrap import wrap
# x = str(input(': '))
# w = int(input())
# z = list(wrap(x, w))
# for i in z:
#     print(i)



# Solution 3:
# import textwrap
# string = input('')
# print('\n'.join(textwrap.wrap(string, width= int(input('')))))


# Solution 4:
# import itertools
# string = input("> ")
# width_length = int(input("What is the width of the groupings? "))

# def grouper(string, width):
#     iters = [iter(string)] * width
#     return itertools.zip_longest(*iters, fillvalue='')

# def displayer(groups):
#     for x in groups:
#         if x == '':
#             continue
#         else:
#             print(''.join(x))

# displayer(grouper(string, width_length))



# Practice 38(3):
    # --> You are given an integer, N. Your task is to print an alphabet rangoli of size N. 
    #     (Rangoli is a form of Indian folk art based on creation of patterns.)
    #     Different sizes of alphabet rangoli are shown below:

    #     #size 3

    #     ----c----
    #     --c-b-c--
    #     c-b-a-b-c
    #     --c-b-c--
    #     ----c----

    #     #size 5

    #     --------e--------
    #     ------e-d-e------
    #     ----e-d-c-d-e----
    #     --e-d-c-b-c-d-e--
    #     e-d-c-b-a-b-c-d-e
    #     --e-d-c-b-c-d-e--
    #     ----e-d-c-d-e----
    #     ------e-d-e------
    #     --------e--------
        
        # First print the half of the Rangoli in the given way and save each line in a list. 
        # Then print the list in reverse order to get the rest.

# Solution 1:
# import string
# def print_rangoli(size):
#     n = size
#     alph = string.ascii_lowercase
#     width = 4 * n - 3

#     ans = []
#     for i in range(n):
#         left = '-'.join(alph[n - i - 1:n])
#         mid = left[-1:0:-1] + left
#         final = mid.center(width, '-')
#         ans.append(final)

#     if len(ans) > 1:
#         for i in ans[n - 2::-1]:
#             ans.append(i)
#     ans = '\n'.join(ans)
#     print(ans)


# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)


# Solution 2:
# def rangoli(n):
#     # your code goes here
#     l1=list(map(chr,range(97,123)))
#     x=l1[n-1::-1]+l1[1:n]
#     mid=len('-'.join(x))
#     for i in range(1,n):
#         print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(mid,'-'))
#     for i in range(n,0,-1):
#         print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(mid,'-')) 
# rangoli(5)


# Practice 38(4):
    # --> You are given a date. Your task is to find what the day is on that date.

    #     Input
    #     A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

    #     08 05 2015

    #     Output
    #     Output the correct day in capital letters.

    #     WEDNESDAY

    #     Use weekday function of calender module

# Solution 1:
# import calendar

# month, day, year = map(int, input().split())

# dayId = calendar.weekday(year, month, day)
# print(calendar.day_name[dayId].upper())



# Practice 38(5):
    # --> Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

    #     Input
    #     The first line of input contains an integer, M.The second line contains M space-separated integers.The third line contains an integer, N.The fourth line contains N space-separated integers.

    #     4
    #     2 4 5 9
    #     4
    #     2 4 11 12

    #     Output
    #     Output the symmetric difference integers in ascending order, one per line.

    #     5
    #     9
    #     11
    #     12


    #     Use '^' to make symmetric difference operation.



# Solution 1:
# if __name__ == '__main__':
#     n = int(input())
#     set1 = set(map(int,input().split()))

#     m = int(input())
#     set2 = set(map(int, input().split()))

#     ans = list(set1 ^ set2)
#     ans.sort()
#     for i in ans:
#         print(i)


