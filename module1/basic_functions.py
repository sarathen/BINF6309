#!/usr/bin/env python3
# basic_functions.py

def multiply (num1, num2):
    return num1 * num2

x = multiply(5,10)

print ("The value of x is {}".format(x))


def hello_name(name):
    if not name :
        print("Hello, you!")
    else:
        print("Hello," + name + "!")

hello_name("")
hello_name("Akbar")


numbers = [1, 5, 81, 10, 8, 2, 102]
for x in numbers:
    if x < 10:
        print(x)

    

   
