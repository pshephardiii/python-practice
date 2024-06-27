# f-strings: examples

# for i in range(1, 11):
#     print(f"9 / {i} = {9 / i}")

# a = 20

# for i in range(1, 9):
#     print(f"The sum of {a} and {i} is {a + i}")

# Coding Exercise: Print Sum of Squares Of First 10 Numbers

# sum_of_squares = 0
# for i in range(1, 11):
#     sum_of_squares += (i * i)
    
# print(sum_of_squares)

# Coding Exercise: Print Sum of Cubes of First 10 Numbers

# sum_of_cubes = 0
# for i in range(1, 11):
#     sum_of_cubes += (i ** 3)
    
# print(sum_of_cubes)

# Coding Exercise: Print Factorial of 6

# factorial = 1
# for i in range(1, 7):
#     factorial *= i
    
# print(factorial)

# Coding Exercise: Print a Square Pattern with Nested For Loops

# n = 5

# for i in range(n): 
#     for j in range(n):

## prints an * and ends with a space rather than a new line
#         print("*", end = '')
## moves to new line on each iteration
#     print()

# Coding Exercise: Print Right-Angled Triangle with nested For Loops

# n = 1

# for i in range(0, 5):
#     for j in range(n):
#         print('*', end = '')
#     n += 1   
#     print()

# Coding Exercise: Return cube of number

# def cube_of_number(n):
#     return n ** 3

# Coding Exercise: Return product of four numbers

# def product_of_four_numbers(a, b, c, d):
#     product = a * b * c * d
#     return product

# Coding Exercise: Return average of five numbers

# def average_of_five_numbers(a, b, c, d, e):
#     sum = a + b + c + d + e
#     avg = sum / 5
#     return avg

# Coding Exercise: calculate third angle of triangle

# def calculate_third_angle(first, second):
#     third = 180 - (first + second)
#     return third

# Coding Exercise: sum of squares of first n even numbers

# def sum_of_squares(n):
#     sum = 0
#     for i in range(2, (n * 2) + 1, 2):
#         sum = sum + (i ** 2)
#     return sum

# Coding Exercise: calculate factorial of input

# def calculate_factorial(n):
#     product = 1
#     for i in range(1, n + 1):
#         print(i)
#         product *= i
#     return product

# DATA TYPE EXERCISES

# Coding Exercise: Calculate Simple Interest

# def calculate_simple_interest(principal, interest, duration):
#     total = principal + (principal * interest * .01 * duration)
#     return total

# Coding Exercise: can access library 18+

# def can_access_library(age):
#     return age >= 18

# Coding Exercise: can race only if speed exactly 200

# def is_eligible_for_race(max_speed):
#     return max_speed == 200

# Coding Exercise: check for valid triangle

# def is_valid_triangle(angle1, angle2, angle3):
#     if angle1 <= 0:
#         return False
#     if angle2 <= 0:
#         return False
#     if angle3 <= 0:
#         return False
#     if (angle1 + angle2 + angle3) == 180:
#         return True
#     else:
#         return False

# Coding Exercise: calculate sum of divisors

# def calculate_sum_of_divisors(n):
#     sum = 0
#     if n <= 0:
#         return sum
    
#     for i in range(1, n + 1):
#         if n % i == 0:
#             sum += i
#     return sum

# Coding Exercise: check if perfect number

# def is_perfect_number(n):
#     if n <= 0:
#         return False
#     sum = 0
    
#     for i in range(1, n):
#         if n % i == 0:
#             sum += i
    
#     if sum == n:
#         return True
#     else:
#         return False

# Coding Exercise: find last digit of number

# def get_last_digit(n):
#     return n % 10

# Coding Exercise: are both numbers even

# def are_both_even(i, j):
#     return i % 2 == 0 and j % 2 == 0

# Coding Exercise: check if leap year

# def is_leap_year(year):
#     div_by_4 = year % 4 == 0
#     div_by_100 = year % 100 == 0
#     div_by_400 = year % 400 == 0    
    
#     return (div_by_4 and not div_by_100) or (div_by_4 and div_by_100 and div_by_400)

# Coding Exercise: is it a right angled triangle

# def is_right_angled_triangle(side1, side2, side3):
#     if side1 < 0 or side2 < 0 or side3 < 0:
#         return False
    
#     squared1 = side1 ** 2
#     squared2 = side2 ** 2
#     squared3 = side3 ** 2
    
#     return (squared1 + squared2 == squared3) or (squared1 + squared3 == squared2) or (squared2 + squared3 == squared1)
    
# Coding Exercise: assigning grades

# def assign_grade(marks):
#     if (marks >= 90):
#         return 'A'
#     elif (marks >= 80):
#         return 'B'
#     elif (marks >= 70):
#         return 'C'
#     elif (marks >= 60):
#         return 'D'
#     elif (marks >= 50):
#         return 'E'
#     else:
#         return 'F'

# Practice Exercise: Weather Advisor

# def provide_weather_advisory(temp):
#     if temp < 0:
#         return "It's freezing! Wear a heavy coat."
#     elif temp <= 10:
#         return "It's cold! Bundle up."
#     elif temp <= 20:
#         return "It's cool! A light jacket will do."
#     else:
#         return "It's warm! Enjoy the day."

# For Loop vs. While Loop Exercises

# Practice Exercise: is prime

# def is_prime(n):
#     if n < 2:
#         return False
        
#     for i in range(2, n):
#         if n % i == 0:
#             return False
    
#     return True

#  Practice Exercise: sum of squares up to limit

# def sum_of_squares_upto_limit(lim):
#     sum = 0
#     i = 1
#     while i ** 2 <= lim:
#         sum += i ** 2
#         i += 1
#     return sum

# Practice Exercise: sum of cubes up to limit

# def sum_of_cubes_upto_limit(lim):
#     sum = 0
#     i = 1
#     while i ** 3 <= lim:
#         sum += i ** 3
#         i += 1
#     return sum

# Practice Exercise: number of digits

# def get_number_of_digits(n):
#     if n == 0:
#         return 1
        
#     if n < 0:
#         return -1
        
#     digits = 0
    
#     while n > 0:
#         print(n)
#         n //= 10
#         digits += 1
    
#     return digits

# Practice Exercise: next fibonacci number past limit

# def next_fibonacci(lim):
#     num1 = 0
#     num2 = 1
#     temp = 0
    
#     while num2 <= lim:
#         temp = num1
#         num1 = num2
#         num2 += temp
#     return num2

# Practice Exercise: is it a vowel

# def is_vowel(char):
#     if char.lower() in 'aeiou':
#         return True
#     return False

# Practice Exercise: count uppercase letters

# def count_uppercase_letters(str):
#     upper_letters = 0
#     for char in str:
#         if char.isupper():
#             upper_letters += 1
    
#     return upper_letters