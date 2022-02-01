'''
Date: 2021-05-06 11:19:03
LastEditors: GC
LastEditTime: 2021-05-06 11:51:14
FilePath: \Python Work\.vscode\Python Practice100\Practice30.py
'''
# Practice 30(1):
    # -->  Write a function to compute 5/0 and use try/except to catch the exceptions.


# Solution 1:
# def throws():
#     return 5 / 0

# try:
#     throws()
# except ZeroDivisionError:
#     print("division by zero !!!")
# except Exception as err:
#     print("Catch an exception !!!")
# finally:
#     print("In finally block for cleanup")


# Solution 2:
# def divide():
#     return 5 / 0

# try:
#     divide()
# except ZeroDivisionError as ze:
#     print("Why on earth you are dividing a numeber by ZERO !!!!")
# except:
#     print("Any other exception")



# # Practice 30(2):
#     --> Define a custom exception class which takes a string message as attribute.
#         To define a custom exception, we need to define a class inherited from Exception.


# Solution 1:
# class MyError(Exception):
#     """My own exception class
    
#     Attributes:
#         msg  -- explanation of the error

#     """

#     def __init__(self, msg):
#         self.msg = msg

# num = int(input())

# try:
#     if num < 10:
#         raise MyError("Input is less than 10")
#     elif num > 10:
#         raise MyError("Input is greater than 10")

# except MyError as me:
#     print("The error raised: " + me.msg)


# Practice 30(3):
    # --> Assuming that we have some email addresses in the "username@companyname.com" format, 
    #     please write program to print the user name of a given email address.
    #     Both user names and company names are composed of letters only.

    #     Example: If the following email address is given as input to the program:

    #     john@google.com

    #     Then, the output of the program should be:

    #     john
    #     In case of input data being supplied to the question, it should be assumed to be a console input.
    
    #     Use \w to match letters.



# Solution 1:
# import re
# emailAddress = input()
# pat2 = "(\w + ) @ ((\w + \.) + (com))"
# r2 = re.match(pat2, emailAddress)
# print(r2.group(1))


# Solution 2：
# email = "john@google.com"
# email = email.split("@")
# print(email[0])


# Solution 3:
import re

email = "john@google.com elise@python.com"
pattern = "(\w + ) @ \w + .com"
ans = re.findall(pattern, email)
print(ans)