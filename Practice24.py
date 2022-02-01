'''
Date: 2021-04-25 19:38:14
LastEditors: GC
LastEditTime: 2021-04-25 19:50:22
FilePath: \Python Work\.vscode\Python Practice100\Practice24.py
'''
# Practice 23:
    # --> Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. 
    #     But Python has a built-in document function for every built-in functions.
    #     Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
    #     And add document for your own function


# Solution 1:
# print(abs.__doc__)
# print(int.__doc__)
# print(input.__doc__)

# def square(num):
#     """
#         Return the square value of the input number.
#         The input number must be integer.
#     """
#     return num ** 2


# print(square(2))
# print(square.__doc__)



# Solution 2:
print(str.__doc__)
print(sorted.__doc__)

def pow(n, p):
    """
        param n: This is any integet number
        param p: This is power over n
        return: n to the power of p = n ^ p
    """
    return n ** p

print(pow(3, 4))
print(pow.__doc__)