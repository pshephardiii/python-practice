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

# Lab 4: RGB Color Class

# class RGBColor:
#     def __init__(self, red, green, blue):
#         self.red = red
#         self.green = green
#         self.blue = blue

#     def invert(self):
#         self.red = 255 - self.red
#         self.green = 255 - self.green
#         self.blue = 255 - self.blue

# 2D Lists

# Lab 5: return target index

# def search_element(list_2D, target):
#     if not list_2D:
#         return -1, -1
#     rows = len(list_2D)
#     cols = len(list_2D[0])
    
#     for i in range(rows):
#         cols = len(list_2D[i])
#         for j in range(cols):
#             if list_2D[i][j] == target:
#                 return i, j
#     return -1, -1

# Lab 6: find sum of each row

# def sum_of_rows(list_2D):
#     sum_list = []
#     sum = 0
#     rows = len(list_2D)
#     cols = 0
    
#     for i in range(rows):
#         cols = len(list_2D[i])
#         for j in range(cols):
#             sum += list_2D[i][j]
#         sum_list.append(sum)
#         sum = 0
#     return sum_list

# Lab 7: Add two matrices of same size

# def add_matrices(matrix1, matrix2):
#     if not matrix1 or not matrix2:
#         return []
        
#     sum_list_2D = []
#     rows = len(matrix1)
    
#     for i in range(rows):
#         cols = len(matrix1[i])
#         sum_list = []
#         for j in range(cols):
#             sum = matrix1[i][j] + matrix2[i][j]
#             sum_list.append(sum)
#         sum_list_2D.append(sum_list)
#     return sum_list_2D

# LISTS OF STRINGS

# Lab 8 : rotate list of strings

# def rotate_strings(strings, n):
#     if not strings or n <= 0:
#         return strings
    
#     rounds = 0
#     while n > rounds:
#         last = strings[len(strings) - 1]
#         for i in range(len(strings) - 1, -1, -1):
#             if strings[i] == last:
#                 continue
#             else:
#                 strings[i + 1] = strings[i]
#         strings[0] = last
#         rounds += 1
#     return strings

# Lab 9: Encode List of Strings

# def encode_strings(strings):
#     if not strings:
#         return []
    
#     new_strings = []

#     for string in strings:
       
#         new_string = ''   

#         for char in string:
            
#             if char == 'z':
#                 char = 'a'
#             elif char == 'Z':
#                 char = 'A'
#             else:
#                 first_val = ord(char)
#                 second_val = first_val + 1
#                 char = chr(second_val)

#             new_string += char
                
#         new_strings.append(new_string)
            
#     return new_strings

# Lab 10: alternate merge two lists

# def alternate_merge(list1, list2):
#     merge_list = []
    
#     i = 0

## alternately add items from lists as long as the index is less than both lengths
#     while i < len(list1) and i < len(list2):
#         merge_list.append(list1[i])
#         merge_list.append(list2[i])
#         i += 1

## this while loop will trigger if list1 is longer than list2   
#     while i < len(list1):
#         merge_list.append(list1[i])
#         i += 1

## this while loop will trigger if list2 is longer than list1
#     while i < len(list2):
#         merge_list.append(list2[i])
#         i += 1
    
#     return merge_list

# Lab 11: anagram checker using list

# import string

# def is_anagram(str1, str2):
#     if len(str1) != len(str2):
#         return False
    
#     list1 = [0] * 26
    
#     list2 = [0] * 26
    
#     for char in str1:
#         i = string.ascii_lowercase.index(char)
#         list1[i] += 1
    
#     for char in str2:
#         i = string.ascii_lowercase.index(char)
#         list2[i] += 1
    
#     if list1 == list2:
#         return True
#     else:
#         return False

# Lab 12: Multiple Inheritance

# class Engine:
#     def start_engine(self):
#         return "Engine started"

# class Wheels:
#     def number_of_wheels(self):
#         return 4

# class Car(Engine, Wheels): 
#     def drive(self):
#         return "Car is driving"