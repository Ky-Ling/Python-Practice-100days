'''
Date: 2021-05-06 10:45:38
LastEditors: GC
LastEditTime: 2021-05-06 11:53:48
FilePath: \Python Work\.vscode\Python Practice100\Practice29.py
'''
# Practice 29(1):
    # --> Define a class named American which has a static method called printNationality.
    #     Use @staticmethod decorator to define class static method.


# Solution 1:
# class American(object):
#     @staticmethod
#     def printNationality():
#         print("American")
    
# anAmerican = American()
# anAmerican.printNationality()
# American.printNationality()


# Solution 2:
# class American:
#     @staticmethod
#     def printNationality():
#         print("I am American")

# american = American()
# american.printNationality()     # this will not run if @staticmethod does not decorates the function.
#                                 # Because the class has no instance.
                                
# American.printNationality()     # this will run even though the @staticmethod
#                                 # does not decorate printNationality()



# Practice 29(2):
    # --> Define a class named American and its subclass NewYorker.
    #     Use class Subclass(ParentClass) to define a subclass.*  


# Solution 1:

# class American(object):
#     print("I am American")

# class NewYorker(American):
#     print("I am NewYorker")

# amAmerican = American()
# amNewYorker = NewYorker()

# print(amAmerican)
# print(amNewYorker)


# Practice 29(3):
    # --> Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
    #     Use def methodName(self) to define a method


# Solution 1:
# class Circle(object):
#     def __init__(self, r):
#         self.radius = r
#     def area(self):
#         return self.radius ** 2 * 3.14

# aCircle = Circle(2)
# print(aCircle.area())



# Practice 29(4):
    # --> Define a class named Rectangle which can be constructed by a length and width. 
    #     The Rectangle class has a method which can compute the area.

# Solution 1:
# class Rectangle(object):
#     def __init__(self, l, w):
#         self.length = l
#         self.width = w
    
#     def area(self):
#         return self.length * self.width

# aRectangle = Rectangle(2, 10)
# print(aRectangle.area())


#Practice 29(5):
    # --> Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
    #     Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
    #     To override a method in super class, we can define a method with the same name in the super class.



# Solution 1:
# class Shape(object):
#     def __init__(self):
#         pass
#     def area(self):
#         return 0

# class Square(Shape):
#     def __init__(self, l):
#         Shape.__init__(self)
#         self.length = l
#     def area(self):
#         return self.length * self.length

# aSquare = Square(2)
# print(aSquare.area())


# Solution 2:
# class Shape():
#     def __init__(self):
#         pass

#     def area(self):
#         return 0

# class Square(Shape):
#     def __init__(self,length = 0):
#         Shape.__init__(self)
#         self.length = length

#     def area(self):
#         return self.length * self.length

# Asqr = Square(5)
# print(Asqr.area())      # prints 25 as given argument

# print(Square().area())  # prints zero as default area


