'''
Date: 2021-04-25 19:51:18
LastEditors: GC
LastEditTime: 2021-04-25 20:20:00
FilePath: \Python Work\.vscode\Python Practice100\Practice25.py
'''
# Practice 25:
    # --> Define a class, which have a class parameter and have a same instance parameter
        # Define an instance parameter, need add it in __init__ method.
        # You can init an object with construct parameter or set the value later


# Solution 1:
# class Person:
#     # Define the class parameter "name"
#     name = "Person"

#     def __init__(self, name = None):
#         # self.name is the instance parameter
#         self.name = name
        
# John = Person("John")
# print("%s name is %s" % (Person.name, John.name))

# nico = Person()
# nico.name = "Nico"
# print("%s name is %s" % (Person.name, nico.name))


# Solution 2
class Car:
    name = "Car"

    def __init__(self, name = None):
        self.name = name
    
honda = Car("Honda")
print("%s name is %s" % (Car.name, honda.name))

toyota = Car()
toyota.name = "Toyota"
print("%s name is %s" % (Car.name, toyota.name))