'''
Date: 2021-05-10 16:18:20
LastEditors: GC
LastEditTime: 2021-05-11 18:46:17
FilePath: \Python Work\.vscode\Python Practice100\Practice37.py
'''
# Practice37(1):
    # --> Please write a program which count and print the numbers of each character in a string input by console.

    #     Example: If the following string is given as input to the program:

    #     abcdefgabc
    #     Then, the output of the program should be:
    #     a,2
    #     c,2
    #     b,2
    #     e,1
    #     d,1
    #     g,1
    #     f,1

    #     Use dict to store key/value pairs. Use dict.get() method to lookup a key with default value.


# Solution 1:
# import string

# s = input()
# for letter in string.ascii_lowercase:
#     cnt = s.count(letter)
#     if cnt > 0:
#         print("{} {}".format(letter, cnt))



# Solution 2:
# s = input()
# for letter in range(ord("a"), ord("z") + 1):
#     letter = chr(letter)
#     cnt = s.count(letter)
#     if cnt > 0:
#         print("{} {}".format(letter, cnt))



# Solution 3:
# s = 'abcdefgabc'
# for i in sorted(set(s)):
#     print(f"{i} {s.count(i)}")



# Solution 4:
# def character_counter(text):
# 	characters_list = list(text)
# 	char_count = {}
# 	for x in characters_list:
# 		if x in char_count.keys():
# 			char_count[x] += 1
# 		else:
# 			char_count[x] = 1
# 	return char_count


# def dict_viewer(dictionary):
# 	for x, y in dictionary.items():
# 		print(f"{x},{y}")


# text = input("> ")
# dict_viewer(character_counter(text))




# Practice37(2):
    # --> Please write a program which accepts a string from console and print it in reverse order.

    #     Example: If the following string is given as input to the program:*

    #     rise to vote sir
    #     Then, the output of the program should be:
    #     ris etov ot esir

    #     Use list[::-1] to iterate a list in a reverse order.



# Solution 1:
# s = input()
# print(s[::-1])



# Solution 2:
# s = input()
# print("".join(reversed(s)))




# Practice37(3):
    # --> Please write a program which accepts a string from console and print the characters that have even indexes.

    #     Example: If the following string is given as input to the program:

    #     H1e2l3l4o5w6o7r8l9d
    #     Then, the output of the program should be:
    #     Helloworld
        
    #     Use list[::2] to iterate a list by step 2.


# Solution 1：
# s = input()
# print(s[::2])



# Solution 2：
# s = "H1e2l3l4o5w6o7r8l9d"
# s = [s[i] for i in range(len(s)) if i % 2 == 0]
# print(s)



# Solution 3:
# s = "H1e2l3l4o5w6o7r8l9d"
# a = []
# for i in range(len(s)):
#     if i % 2 == 0:
#         a += s[i]

# print(a)




# Practice37(4):
    # --> Please write a program which prints all permutations of [1,2,3]
    #     Use itertools.permutations() to get permutations of list.


# Solution 1:
# import itertools
# print(list(itertools.permutations([1, 2, 3])))



# Solution 2:
# from itertools import permutations

# def permuation_generator(iterable):
#     p = permutations(iterable)
#     for i in p:
#         print(i)


# x = [1,2,3]
# permuation_generator(x)



# Practice37(5):
    # --> Write a program to solve a classic ancient Chinese puzzle: 
    #     We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

    #     Use for loop to iterate all possible solutions.


# Solution 1:
# def solve(numheads, numlegs):
#     ns='No solutions!'
#     for i in range(numheads + 1):
#         j = numheads - i
#         if 2 * i + 4 * j == numlegs:
#             return i, j
#     return ns, ns

# numheads = 35
# numlegs = 94
# solutions = solve(numheads, numlegs)
# print(solutions)



# Solution 2:
import itertools

def animal_counter(lst):
    chickens = 0	
    rabbits = 0
    for i in lst:
        if i == 2:
            chickens += 1
        elif i == 4:
            rabbits += 1
    print(f"Number of chickens is {chickens}\nNumber of rabbits is {rabbits}")


def animal_calculator(total_legs, total_heads, legs_of_each_species):
    combinations = itertools.combinations_with_replacement(legs_of_each_species, total_heads)
    correct_combos = []
    for i in list(combinations):
        if sum(i) == total_legs:
            correct_combos.append(i)
    print(correct_combos)
    for i in correct_combos:
        animal_counter(i)

animal_calculator(94, 35, legs_of_each_species=[2,4])