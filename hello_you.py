#!/usr/bin/env python3
# hello_you.py

def hello_name(Name):
    if not Name :
        print("Hello, you!")
    else:
        print("Hello," + Name + "!")
if __name__=="__main__":
    Name = ''
    print(hello_name(Name))





