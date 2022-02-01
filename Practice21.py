'''
Date: 2021-04-22 10:54:53
LastEditors: GC
LastEditTime: 2021-04-22 11:33:15
FilePath: \Python Work\.vscode\Python Practice100\Practice21.py
'''
# Practice 21:
    # --> A robot moves in a plane starting from the original point (0,0).
    #     The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

    #     UP 5
    #     DOWN 3
    #     LEFT 3
    #     RIGHT 2

    #     The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. 
    #     If the distance is a float, then just print the nearest integer. 
    #     Example: If the following tuples are given as input to the program:

    #     UP 5
    #     DOWN 3
    #     LEFT 3
    #     RIGHT 2

    #     Then, the output of the program should be:

    #     2


# Solution 1:
# import math
# pos = [0, 0]
# while True:
#     s = input()
#     if not s:
#         break
#     movement = s.split(" ")
#     direction = movement[0]
#     steps = int(movement[1])

#     if direction == "UP":
#         pos[0] += steps
#     elif direction == "DOWN":
#         pos[0] -= steps
#     elif direction == "LEFT":
#         pos[1] -= steps 
#     elif direction == "RIGHT":
#         pos[1] += steps
#     else:
#         pass

# print(int(round(math.sqrt(pos[1] ** 2 + pos[0] ** 2))))


# Solution 2:
# import math
# x, y = 0, 0
# while True:
#     s = input().split()
#     if not s:
#         break
#     if s[0] == "UP":
#         x -= int(s[1])
#     if s[0] == "DOWN":
#         x += int(s[1])
#     if s[0] == "LEFT":
#         y -= int(s[1])
#     if s[0] == "RIGHT":
#         y += int(s[1])

# print(int(round(math.sqrt(x ** 2 + y ** 2))))
        


# Solution 3:
from math import sqrt
lst = []
position = [0, 0]
while True:
    a = input()
    if not a:
        break
    lst.append(a)
for i in lst:
    if "UP" in i:
        position[0] -= int(i.strip("UP "))
    if "DOWN" in i:
        position[0] += int(i.strip("DOWN "))
    if "LEFT" in i:
        position[0] -+ int(i.strip("LEFT "))
    if "RIGHT" in i:
        position[0] += int(i.strip("RIGHT "))
print(round(sqrt(position[1] ** 2 + position[0] ** 2)))