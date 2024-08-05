#!/usr/bin/env python3
import ipdb

def admin_login(username, password):
    if username == "admin" and password == "12345":
        return "Access granted"
    elif username == "ADMIN" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"


def hows_the_weather(temperature):
    msg = "It's perfect out there!"
    if temperature < 40:
        msg = "It's brisk out there!"
    elif temperature > 40 and temperature < 65:
        msg = "It's a little chilly out there!"
    elif temperature > 85:
        msg = "It's too dang hot out there!" 
    return msg

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else:
        return num
    
def calculator(operation, num1, num2):
    if operation == "+":
        return  num1 + num2
    elif operation == "-":
        return  num1 - num2
    elif operation ==  "*":
        return  num1 * num2
    elif operation == "/":
        return  num1 / num2
    else:
        print("Invalid operation!") 
        return None
