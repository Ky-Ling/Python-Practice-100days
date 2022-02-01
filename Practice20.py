'''
Date: 2021-04-22 10:38:14
LastEditors: GC
LastEditTime: 2021-04-22 10:51:21
FilePath: \Python Work\.vscode\Python Practice100\Practice20.py
'''
# Practice 20:
    # --> Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

    #     Suppose the following input is supplied to the program:

    #     7
    #     Then, the output should be:

    #     0
    #     7
    #     14

# Solution 1:
# class MyGen():
#     def by_seven(self, n):
#         for i in range(0, int(n / 7) + 1):
#             yield i * 7
# for i in MyGen().by_seven(int(input())):
#     print(i)


# Solution 2:
class Divisible:
    def by_seven(self, n):
        for number in range(1, n + 1):
            if number % 7 == 0:
                yield number

divisible = Divisible()
generator = divisible.by_seven(int(input()))
for number in generator:
    print(number)