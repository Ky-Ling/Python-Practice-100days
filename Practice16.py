'''
Date: 2021-04-16 15:52:54
LastEditors: GC
LastEditTime: 2021-04-22 10:24:56
FilePath: \Python Work\.vscode\Python Practice100\Practice16.py
'''
# Practice 16:
    # --> Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
    #      >Suppose the following input is supplied to the program:

    #     1,2,3,4,5,6,7,8,9
    #     Then, the output should be:

    #     1,9,25,49,81


# Solution 1:
# a = input("< ").split(", ")
# seq = []
# lst = [int(i) for i in a]
# for i in lst:
#     if i % 2 != 0:
#         i = i * i
#         seq.append(i)
# seq = [str(i) for i in seq]
# print(",".join(seq))


# Solution 2:
# lst = [str(int(i) ** 2) for i in input("< ").split(", ") if int(i) % 2]
# print(" ".join(lst))


# Solution 3:
seq = input().split(",")
lst = [int(i) for i in seq]
def flt(i):
    return i % 2 != 0

result = [str(i * i) for i in filter(flt, lst)]
print(",".join(result))
