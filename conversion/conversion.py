#   "name": "Conversion Game",
#   "version": "2.2.1",
#   "description": "A conversion game to help you learn binary, hexadecimal and decimal",
#   "main": "conversion.py",
#   "repository": {
#     "type": "git",
#     "url": "git+https://github.com/Carbon16/L6-assingments.git"
#   },
#   "author": "Leo G. Skingley",
#   "license": "ISC"

import random
import os
import json
from time import sleep

def random_number():
    num = random.randint(0, 255)
    return num

def toDecimalFromHex(num):
    decimal = 0
    for digit in num:
        if digit == "A":
            digit = 10
        elif digit == "B":
            digit = 11
        elif digit == "C":
            digit = 12
        elif digit == "D":
            digit = 13
        elif digit == "E":
            digit = 14
        elif digit == "F":
            digit = 15
        else:
            digit = int(digit)
        decimal = decimal*16 + int(digit)
    return decimal

def toDecimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal

def toBin(num):
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    return binary

def toHex(num):
    hexadecimal = ""
    while num > 0:
        if num % 16 == 10:
            hexadecimal = "A" + hexadecimal
        elif num % 16 == 11:
            hexadecimal = "B" + hexadecimal
        elif num % 16 == 12:
            hexadecimal = "C" + hexadecimal
        elif num % 16 == 13:
            hexadecimal = "D" + hexadecimal
        elif num % 16 == 14:
            hexadecimal = "E" + hexadecimal
        elif num % 16 == 15:
            hexadecimal = "F" + hexadecimal
        else:
            hexadecimal = str(num % 16) + hexadecimal
        num = num // 16
    return hexadecimal

def open_score():
    try:
        file = open('data.json')
        score = json.load(file)
        return score
    except FileNotFoundError:
        print("File not found")
        score = {"score": 0}
        score["name"] = input("Enter name: ")
        return score

def save_score(score):
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(score, file, ensure_ascii=False, indent=4)

def binary_to_decimal():
    os.system("cls")
    print("----------------Binary to Decimal----------------")
    decimal = random_number()
    binary = toBin(decimal)
    print("Convert", binary, "to decimal")
    print(decimal)
    answer = int(input("Please enter the decimal value: "))
    if answer == decimal:
        print("Correct! [+50]")
        score["score"] += 50
        print("Your score is now: ", score["score"])
        save_score(score)
    else:
        print("Incorrect :( [-25]")
        score["score"] -= 25
        print("Your score is now: ", score["score"])
        save_score(score)

def decimal_to_binary():
    os.system("cls")
    print("----------------Binary to Decimal----------------")
    decimal = random_number()
    print("Convert", decimal, "to binary")
    binary = toBin(decimal)
    print(binary)
    answer = int(input("Please enter the binary value: "))
    if answer == binary:
        print("Correct! [+50]")
        score["score"] += 50
        print("Your score is now: ", score["score"])
        save_score(score)
    else:
        print("Incorrect :( [-25]")
        score["score"] -= 25
        print("Your score is now: ", score["score"])
        save_score(score)

def hexadecimal_to_decimal():
    os.system("cls")
    print("----------------Hexadecimal to Decimal----------------")
    num = random_number()
    hexadecimal = toHex(num)
    print("Convert", hexadecimal, "to decimal")
    decimal = int(hexadecimal, 16)
    print(decimal)
    answer = int(input("Please enter the decimal value: "))
    if answer == decimal:
        print("Correct! [+50]")
        score["score"] += 50
        print("Your score is now: ", score["score"])
        save_score(score)
    else:
        print("Incorrect :( [-25]")
        score["score"] -= 25
        print("Your score is now: ", score["score"])
        save_score(score)

def decimal_to_hexadecimal():
    os.system("cls")
    print("----------------Decimal to Hexadecimal----------------")
    decimal = random_number()
    print("Convert", decimal, "to hexadecimal")
    hexadecimal = toHex(decimal)
    print(hexadecimal)
    answer = input("Please enter the hexadecimal value: ")
    if answer == hexadecimal:
        print("Correct! [+50]")
        score["score"] += 50
        print("Your score is now: ", score["score"])
        save_score(score)
    else:
        print("Incorrect :( [-25]")
        score["score"] -= 25
        print("Your score is now: ", score["score"])
        save_score(score)

def binary_to_hexadecimal():
    os.system("cls")
    print("----------------Binary to Hexadecimal----------------")
    num = random_number()
    hexadecimal = toHex(num)
    binary = toBin(num)
    print("Convert", binary, "to hexadecimal")
    print(hexadecimal)
    answer = input("Please enter the hexadecimal value: ")
    if answer == hexadecimal:
        print("Correct! [+50]")
        score["score"] += 50
        print("Your score is now: ", score["score"])
        save_score(score)
    else:
        print("Incorrect :( [-25]")
        score["score"] -= 25
        print("Your score is now: ", score["score"])
        save_score(score)

def hexadecimal_to_binary():
    os.system("cls")
    print("----------------Hexadecimal to Binary----------------")
    num = random_number()
    hexadecimal = toHex(num)
    binary = toBin(num)
    print("Convert", hexadecimal, "to binary")
    print(binary)
    answer = int(input("Please enter the binary value: "))
    if answer == binary:
        print("Correct! [+50]")
        score["score"] += 50
        print("Your score is now: ", score["score"])
        save_score(score)
    else:
        print("Incorrect :( [-25]")
        score["score"] -= 25
        print("Your score is now: ", score["score"])
        save_score(score)
        

def menu():
    os.system("cls")
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")
    print("3. Hexadecimal to Decimal")
    print("4. Decimal to Hexadecimal")
    print("5. Binary to Hexadecimal")
    print("6. Hexadecimal to Binary")
    choice = int(input("Please choose a conversion type: "))
    if choice == 1:
        binary_to_decimal()
    elif choice == 2:
        decimal_to_binary()
    elif choice == 3:
        hexadecimal_to_decimal()
    elif choice == 4:
        decimal_to_hexadecimal()
    elif choice == 5:
        binary_to_hexadecimal()
    elif choice == 6:
        hexadecimal_to_binary()
    else:
        print("Invalid choice, please try again")
        menu()

ooop = input("Would you like to open your last saved score? (y/n): ")
if ooop == "y":
    score = open_score()
    print("Hello, ", score["name"], ", your last saved score is: ", score["score"])
    sleep(3)
else:
    score = {}
    score["score"] = 0
    score["name"] = input("Enter name: ")

print("Hello", score["name"], "Welcome to the Number Conversion Test")
while True:
    menu()
    choice = input("Do you want to exit? (y/n): ")
    if choice == "y":
        break
    else:
        os.system("cls")
