# Object Classes and Constructors

# Lab 1 - inches should be converted to feet and inches.

# class Dimension:

#     def __init__(self, inches): 
#         self.feet = inches // 12
#         self.inches = inches % 12
#         if inches < 0:
#             self.feet = -1
#             self.inches = -1

# Lab 2 - square class

# class Square:
#     def __init__(self, side): 
#         if side <= 0:
#             self.side = -1
#         else:
#             self.side = side

#     def calculate_area(self):
#         if self.side == -1:
#             self.area = -1
#         else: 
#             self.area = self.side ** 2
#         return self.area
#     def calculate_perimeter(self):
#         if self.side == -1:
#             self.perimeter = -1
#         else:
#             self.perimeter = self.side * 4
#         return self.perimeter

# Lab 3 - 2d Point class

# import math

# class Point:

#     def __init__(self, x, y): 
#         self.x = x
#         self.y = y

#     def move(self, dx, dy):
#         self.x += dx
#         self.y += dy

#     def distance_to(self, other):
#         return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)