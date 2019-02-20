# Makes a Nice Multiplication table up to 19 times 19 !
# This table is nice for "shy" mathematicians, people who are "intimidated" by the "ordinary" times table!
# Anders Kouru   30 January 2019

import math

MIN_ROW     = int(10)
MAX_COLUMNS = int(19)

multi_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
save_list  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
            
def introFunction():
    print("")
    print("Makes a Multiplication table up to 19 times 19")
    return 0

def print_a_row(number):
    c     = int(1)
    if number < MIN_ROW:
        minimum_rows = MIN_ROW + 1
    else:
        minimum_rows = number + 1
    print("A Nice Multiplication table for     ",number)
    c     = 0
    multi_list = save_list[0:number]             # Number of columns!
    j  = int(1)
    for i in range(1,minimum_rows,1):            # number of rows is determined in the outer loop!
        print("{:5}".format(i*j),end=' ')        # print("{:5}".format(a*j),end=' ')
        if  i == number:                         # if (c+1) == number or (a == j):
            c = 0
            break
    return 0

def make_the_table(number):
    c     = int(1)
    if number < MIN_ROW:
        minimum_rows = MIN_ROW
    else:
        minimum_rows = number
    c     = 0
    multi_list = save_list[0:number]             # Number of columns!
    j  = int(1)
    for i in range(0,minimum_rows,1):            # number of rows is determined in the outer loop!
        print("")
        for a in multi_list:                     # the inner loop writes out the rows in the multiplication table
           print("{:5}".format(a*j),end=' ')
           if (a == j):                          # if (c+1) == number or (a == j):
               c = 0
               break
           c += 1                                # inner loop ends!
        j   += 1                                 # outer loop ends!
    print("")
    print("")
    return 0

def main():
    number = int(5)
    forts  = int(1)                   
    introFunction()
    while forts != 0:
        while number >= 1 and number <= MAX_COLUMNS:
            print("Input Number, should be between 1 and ",MAX_COLUMNS,"Zero ends!          ",end= ' ')
            number = input("")
            number = int(number)
            print('')
            if number == 0:
                forts = int(0)
                break
            if number >= 1  and number <= MAX_COLUMNS:
                print_a_row(number)                        #Här också!
                make_the_table(number) 
            else:
                print("Input Number, should be between 1 and   ",MAX_COLUMNS,"Zero ends!            ")
                number = input("")
                number = int(number)
            if number == 0:
                forts = int(0)
                break
    return 0

main()

