# Prime 01
# decides if a number is Prime!
# Anders Kouru     29 june 2014

import math

def inputFunction(pp):
    print('Which number can be prime?' )
    pp = input('It should be 2 or higher.                ')
    pp = int(pp)
    #print(pp)
    while int(pp) < 2:
        pp = input('The number should be 2 or higher.        ')
        pp = int(pp)
    return(pp)             

def floor(num):                 # floor(25.3) returnerar    25.0
    tal = float(num)
    ital = int(num)
    numrest = tal - ital
    tal -= numrest
    return tal

def prime(prim,is_prime):
    primkopia = float(prim)
    tal  = float(prim)
    end  = primkopia
    prim = int(prim)
    is_prime = 1
    divisor = 2.0
    antal_div = 1.0
    rest = 1.0
    test = 1.0
    a = int(2)
    while(divisor*divisor <= end and antal_div < 2): # save work if not prime
        rest = primkopia/divisor
        test = floor(rest)
        divisor += 1.0
        if rest == test:
            antal_div += 1
            is_prime = 0
            is_prime = int(is_prime)
        if (prim == 2.0 or antal_div == 1): # 2 is an unusual prime
            is_prime = 1
        if (antal_div > 1):
           is_prime = 0
    return is_prime

def main():
    forts = 1                 # continue = 1
    prim  = 1                 # prime    = 1
    prim = int(prim)
    is_prime = 1
    while forts != 0:
        prim = inputFunction(prim)
        is_prime = prime(prim,is_prime)
        if is_prime == 1:
                print("number ",prim," is prime!             ")
        else:
                print("number ",prim," not prime             ")
        print("")
        forts = input("continue = 1,  end = 0                   ")
        print(forts)
        forts = int(forts)
        
main()       



