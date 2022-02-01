'''
Date: 2021-05-06 16:13:54
LastEditors: GC
LastEditTime: 2021-05-06 16:40:26
FilePath: \Python Work\.vscode\Python Practice100\Practice31.py
'''
# Practice 31(1):
    # --> Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
    #     Example: If the following words is given as input to the program:

    #     2 cats and 3 dogs.
        
    #     Then, the output of the program should be:
    #     ['2', '3']
    #     In case of input data being supplied to the question, it should be assumed to be a console input.
    
    #     Use re.findall() to find all substring using regex.

# Solution 1:
# import re
# s = input()
# print(re.findall("\d+", s))


# Solution 2:
# import re
# s = input()
# pattern = "\d+"
# ans = re.findall(pattern, s)
# print(ans)


# Solution 3；
# email = input().split()
# ans = []
# for word in email:
#     if word.isdigit():      # can also use isnumeric() / isdecimal() function instead
#         ans.append(word)
# print(ans)


# Solution 4:
# email = input().split()
# ans = [word for word in email if word.isdigit()]
# print(ans)



# Practice 31(2):
    # --> Print a unicode string "hello world".
    #     Use u'strings' format to define unicode string.
        

# Solution 1:
# unicodeString = u"hello world"
# print(unicodeString) 


# Practice 31(3):
    # --> Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
    #     Use unicode()/encode() function to convert.
        

# Solution 1:
# s = input()
# a = unicode(s, "utf-8")
# print(a)


# Solution 2:
# s = input()
# a = s.encode("utf-8")
# print(a)




# Practice 31(4):
    # --> Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
    #     Example: If the following n is given as input to the program:
    #     5
    #     Then, the output of the program should be:
    #     3.55
    #     In case of input data being supplied to the question, it should be assumed to be a console input.

    # Use float() to convert an integer to a float.
    # Even if not converted it wont cause a problem because python by default understands the data type of a value
# Solution 1:
# n = int(input())
# sum = 0.0
# for i in range(1, n + 1):
#     sum += float(float(i) / (i + 1))
# print(sum)


# Solution 2:
# s = int(input())
# sum = 0
# for i in range(1, s + 1):
#     sum += i / (i + 1)

# print(round(sum, 2))   # rounded to 2 decimal point


# Solution 3:
def question(n):
    print(round(sum(map(lambda x: x / (x + 1), range(1, n +1))), 2))

question(5)