#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username.upper() == "ADMIN" and password == "12345"):
        return "Access granted"
    else:
        return "Access denied"
    pass

print(admin_login("sudo", "12345"))
print(admin_login("admin", "12345"))
print(admin_login("ADMIN", "12345"))


def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature > 40 and temperature < 65:
        return "It's a little chilly out there!"
    elif temperature > 85 :
        return  "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
    pass

print(hows_the_weather(33))
# "Brisk!"
print(hows_the_weather(99))
# "Too dang hot"
print(hows_the_weather(75))
# "Perfect!"

def fizzbuzz(num):
    # your code here
    if (num % 3 == 0  and num % 5 == 0):
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    pass

print(fizzbuzz(1))
# 1
print(fizzbuzz(2))
# 2
print(fizzbuzz(3))
# Fizz
print(fizzbuzz(4))
# 4
print(fizzbuzz(5))
# Buzz
print(fizzbuzz(15))
# FizzBuzz

def calculator(operation, num1, num2):
    # your code here
    dict_map = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2 
        # if num2 != 0 else "Cannot divide by zero"
    }

    if operation in dict_map:
        return dict_map[operation]
    else:
        print("Invalid operation!")
        return None
    pass

calculator("+", 1, 1)
# 2
calculator("-", 3, 1)
# 2
calculator("*", 3, 2)
# 6
calculator("/", 4, 2)
# 2
calculator("nope", 4, 2)
# "Invalid operation!"
# None