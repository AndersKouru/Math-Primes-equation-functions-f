# Roman Numerals!
# Credit: Paul M. Winkler, from Python Cookbook First Edition
# Anders Kouru 25 sept 2015


import math
import string

def introFunction(choice):
    choice = int(5)
    print("This function converts integers to Roman Numerals or the other way around!")
    print("Integer to Roman = 1      ")
    choice = input("Roman to Integer = 2           ")
    choice = int(choice)
    while (choice < 1) or (choice > 2):
        print("Integer to Roman = 1      ")
        choice = input("Roman to Integer = 2                     ")
        choice = int(choice)
    return choice
        

def inputFunction():
    num = int(1)
    num = input("Convert an integer to a Roman numeral, from 1 to 3999           ")
    num = int(num)
    while (num < 1) or (num > 3999):
        num = input("an integer to a Roman numeral, from 1 to 3999           ")
        num = int(num)
    return num


def int_to_roman(num):
    j= int(1)
    ital = int(num)
    result = []
    print("num           =                       ",num)
    ints   = (1000, 900, 500, 400, 100, 90,  50,  40, 10,  9,   5,  4, 1)
    nums   = ("M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I")
    for i in range(len(ints)):
        count = int(ital/ints[i])
        result.append(nums[i] * count)
        ital -= ints[i] * count
    print("Roman numeral =                        ",end="")
    for a in result:                     # writes out the list, result[]
        print("{:}".format(a*j),end='')
    print("")        
    return None


def roman_to_int():
    sum = int(0)
    roman = ""
    print("Roman to integer  ")
    roman = input("Input Roman numeral=                   ")
    roman = roman.upper()
    print("Roman numeral =                       ",roman, end= "")
    nums = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    sum = int(0)
    for i in range(len(roman)):
        try:
            value = nums[roman[i]]
            # If the next place holds a larger number, this value is negativ
            if i +1 < len(roman) and nums[roman[i+1]] > value:
                sum -= value
            else:
                sum += value
        except KeyError:
            raise ValueError("Input is not a valid Roman numeral:   ",roman)
    print("")
    int_to_roman(sum) # easiest test for validity!
    print("roman ",roman,"= ",sum)
    return None


def main():
    forts  = int(1)
    sum    = int(0)
    choice = int(5)
    choice = introFunction(choice)
    result = ()
    num = int(1)
    while forts != 0:
        if choice == 1:
            num = inputFunction()
            int_to_roman(num)
            
        if choice == 2:
            roman_to_int()
        print("")
        forts = input("continue = 1,  end = 0                           ")
        if forts == '0':
            break
        #forts = int(forts)
    return None


main()
