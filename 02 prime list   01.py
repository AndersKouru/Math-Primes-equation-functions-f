# Prime list 
# makes a list of Primes!
# Anders Kouru  29 juni 2014

import math
width = int(1)
width = 5
count = int(0)

def introFunction():
    print("This function makes a list of Prime numbers!")

def doTheJob(start,num):
    prim = start
    arbnum = num
    is_prime = int(1)
    maximum = 0                 # maximun = 1
    count   = 0
    while (maximum < arbnum):   
        for a in range(1,num):
            is_prime = prime(prim,is_prime)   
            if is_prime == 1:
                print(" {:8}".format(prim),end='   ')
                maximum += 1
                prim    += 2
                count   += 1
            else:
                prim += 1
            if count == num:
                break
    print("")
    return 0

def main():
    start = int(2)
    num   = int(1)
    forts = 1
    prim = start
    is_prime = int(1)
    while forts != 0:
        introFunction()
        start = inputFunction(start)
        num = input('How many Primes, at least one ?                 ')
        num = int(num)
        if num <= 0:
                num = int(1)
        prim  = start
        doTheJob(start,num)
        print("")
        forts = input("continue = 1,  end = 0                     ")
        print(forts)
        forts = int(forts)
               
def inputFunction(start):
        print('Where do we look for the lowest Prime?' )
        start = input('It should be 2 or higher.                         ')
        start = int(start)
        print("start = ",start)
        while int(start) < 2:
            start = input('The number should be 2 or higher.                ')
            start = int(start)
        return start            

def floor(num):
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
    while(divisor*divisor <= end and antal_div < 2): # save some work if number is not a prime!
        rest = primkopia/divisor
        test = floor(rest)
        divisor += 1.0
        if rest == test:
            antal_div += 1
            is_prime = 0
            is_prime = int(is_prime)
        if (prim == 2 or antal_div == 1): # 2 is an unusual prime
            is_prime = 1
        if (antal_div > 1):
           is_prime = 0
    return is_prime

main()       




