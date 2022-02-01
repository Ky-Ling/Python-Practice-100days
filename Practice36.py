'''
Date: 2021-05-10 15:46:19
LastEditors: GC
LastEditTime: 2021-05-10 16:15:22
FilePath: \Python Work\.vscode\Python Practice100\Practice36.py
'''
# Practice 36(1):
    # --> With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], 
    #     write a program to make a list whose elements are intersection of the above given lists.
    #     Use set() and "&=" to do set intersection operation.


# Solution 1:
# list1 = [1,3,6,78,35,55]
# list2 = [12,24,35,24,88,120,155]
# set1 = set(list1)
# set2 = set(list2)
# intersection = set1 & set2
# print(intersection)


# Solution 2:
# list1 = [1,3,6,78,35,55]
# list2 = [12,24,35,24,88,120,155]
# set1 = set(list1)
# set2 = set(list2)
# intersection = set.intersection(set1, set2)
# print(intersection)



# Practice 36(2):
    # --> With a given list [12,24,35,24,88,120,155,88,120,155], 
    #     write a program to print this list after removing all duplicate values with original order reserved.
    #     Use set() to store a number of values without duplicate.
    

# Solution 1:
# def remove_Duplicate(li):
#     newli = ()
#     seen = set()
#     for i in li:
#         if i not in seen:
#             seen.add(i)
#             newli.append(i)

# li=[12,24,35,24,88,120,155,88,120,155]
# print(removeDuplicate(li))
    


# Solution 2:
# li=[12,24,35,24,88,120,155,88,120,155]
# for i in li:
#     if li.count(i) > 1:
#         li.remove(i)

# print(li)


# Solution 3:
# def remove_Duplicate(li):
#     seen = {}   #dictionary
#     for i in li:
#         if i not in seen:
#             seen[i] = True
#             yield i

# li=[12,24,35,24,88,120,155,88,120,155]
# print(list(remove_Duplicate(li)))




# Practice 36(3):
    # --> Define a class Person and its two child classes: Male and Female. 
    #     All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

    #     Use Subclass(Parentclass) to define a child class.


# Solution 1:
# class Person(object):
#     def getGender(self):
#         print("Unknown")

# class Male(Person):
#     def getGender(self):
#         print("Male") 

# class Female(Person):
#     def getGender(self):
#         print("Female")

# aMale = Male()
# aFemale = Female()

# print(aMale.getGender())
# print(aFemale.getGender())


# Solution 2:
class Person(object):
    def __init__(self):
        self.gender = "unknown"
    def getGender(self):
        print(self.gender)
    
class Male(Person):
    def __init__(self):
        self.gender = "Male"

class Female(Person):
    def __init__(self):
        self.gender = "Female"

aaa = Female()
bbb = Male()
aaa.getGender()
bbb.getGender()