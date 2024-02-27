# 1. Write a Python program to get the Python version you are using.


# 2. Write a Python program to display the current date and time.

# import datetime
# x = datetime.datetime.now()
# print(x)

# 3. Write a Python program which accepts the radius of a circle from the user and compute the area.

# import math
# radius = int(input("Nhap ban kinh:")) 
# print(radius*radius*math.pi)

# 4. Write a Python program which accepts the user's first and last name and 
#print them in reverse order with a space between them.

# firstName = str(input("Nhap first name:"))
# lastName = str(input("Nhap last name:"))
# print(lastName + ' ' + firstName)

# 5. Write a Python program to get the difference between a given number and 17, 
# if the number is greater than 17 return double the absolute difference.

# import math
# number = int(input('Nhap so:'))
# diff = abs(number - 17)
# if(number > 17):
#     print(diff * 2)

# 6. Write a Python program to test whether a number is within 100 of 1000 or 2000

# number = int(input("Nhap so n:"))
# if(900 <= number <= 1100 or 1900 <= number <= 2100):
#     print("So " + str(number) + " nam trong khoang 100 cua 1000 hay 2000")
# else:
#     print("So " + str(number) + " khong nam trong khoang 100 cua 1000 hay 2000")

# 7. Write a Python program to calculate the sum of three given numbers, 
# if the values are equal then return three times of their sum.

# a = int(input("Nhập số a: "))
# b = int(input("Nhập số b: "))
# c = int(input("Nhập số c: "))
# sum = a + b + c
# if(a == b == c):
#     sum *= 3
# print("Kết quẻ = " + str(sum))

# 8. Write a Python program to find whether a given number 
# (accept from the user) is even or odd, print out an appropriate 
# message to the user.

# def oddOrEven(number):
#     if(number % 2 == 0):
#         print('So chan')
#     else:
#         print("So le")

# num = int(input("Nhap so n:"))
# oddOrEven(num)

# 9. Write a Python program to guess a number between 1 to 9.

# import random
# def ranNum1to9():
#     num = random.randint(1,9)
#     return num

# num = int(input("Doan so de:"))
# if(num == ranNum1to9()):
#     print("Got u beach")

# 10. Write a Python program to get the Fibonacci series between 0 to 50.

# def fibonaccu(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return fibonaccu(num - 1) + fibonaccu(num - 2)

# series = []
# index = 0
# while fibonaccu(index) < 50:
#     series.append(fibonaccu(index))
#     index += 1
# print(series)



