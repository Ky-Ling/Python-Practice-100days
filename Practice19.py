'''
Date: 2021-04-19 14:54:23
LastEditors: GC
LastEditTime: 2021-04-20 19:22:16
FilePath: \Python Work\.vscode\Python Practice100\Python19.py
'''
# Practice 19:
    # --> You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers.;
    #     The tuples are input by console. 
    #     The sort criteria is:

    #     1: Sort based on name
    #     2: Then sort based on age
    #     3: Then sort by score
    #     The priority is that name > age > score.

    #     If the following tuples are given as input to the program:

    #     Tom,19,80
    #     John,20,90
    #     Jony,17,91
    #     Jony,17,93
    #     Json,21,85
    #     Then, the output of the program should be:

    #     [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]


# Solution 1:
# from operator import itemgetter, attrgetter

# l = []
# while True:
#     s = input()
#     if not s:
#         break
#     l.append(tuple(s.split(",")))

# print(sorted(l, key=itemgetter(0,1,2)))


# Solution 2:
lst = []
while True:
    s = input().split(",")
    if not s[0]:
        break                                           # breaks for blank input
    lst.append(tuple(s))

lst.sort(key= lambda x:(x[0], int(x[1], int(x[2]))))    # here key is defined by lambda and the data is sorted by element priority 0>1>2 in accending order
print(lst)