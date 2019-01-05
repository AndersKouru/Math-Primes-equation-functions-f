# Prime list 
# makes a list of Primes!
# Anders Kouru  29 juni 2014

import math
width = int(1)
width = 5
count = int(0)

def intro_function():
    print("This function makes a list of Prime numbers!")
    return 0
        
def do_the_job(start,num):
    count_prime = int(-1)
    prime = int(2)
    prime = start
    work = num
    is_prime = int(1)
    maximum = 0         
    count   = 0
    while (maximum < work):
        for a in range(1,num):
            
            is_prime = prime_function(prime,is_prime) 
            if is_prime == 1:
                count_prime += 1
                if count_prime %10 == 0:
                    print("")                     
                print(" {:12}".format(prime),end='')
                maximum += 1
                prime   += 2
                count   += 1
            else:
                prime += 1
            if count == num:
                break
    print("")
    return 0

def main():
    start = int(2)
    num   = int(1)
    forts = 1
    prime = start
    intro_function()
    while forts != 0:
        start = input_function(start)
        num = input('How many Primes, at least one ?                 ')
        num = int(num)
        if num <= 0:
                num = int(1)
        do_the_job(start,num)
        print("")
        forts = input("continue = 1,  end = 0                     ")
        print(forts)
        forts = int(forts)
               
def input_function(start):
        print('Where do we look for the lowest Prime?' )
        start = input('It should be 2 or higher.                         ')
        start = int(start)
        print("start = ",start)
        while int(start) < 2:
            start = input('The number should be 2 or higher.                ')
            start = int(start)
        return start            

def prime_function(prime,is_prime):
    primecopy = float(prime)
    end  = primecopy
    prime = int(2)
    is_prime = 1
    divisor = 2.0
    numb_div = 1.0
    rest = 1.0
    test = 1.0
    while(divisor*divisor <= end and numb_div < 2): 
        rest = primecopy/divisor
        test = math.floor(rest)                 
        divisor += 1.0
        if rest == test:
            numb_div += 1
            is_prime = 0
            is_prime = int(is_prime)
        if (prime == 2 or numb_div == 1):        # 2 is an unusual prime
            is_prime = 1
        if (numb_div > 1):
           is_prime = 0
    return is_prime

main()       


