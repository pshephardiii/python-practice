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
