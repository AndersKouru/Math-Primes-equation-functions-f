# Factors numbers into Primes!
# Anders Kouru 30 juni 2014, last modified 19 dec 2018


import math

def introFunction():
    print("This function Factors numbers into Primes!")
    return 0
        
def prime_Factor(prime_numb):
    divisor = 2.0
    prime_save = prime_numb
    end = pow(prime_save,0.5)
    end_save = 1
    end_save = int(end)
    prime_save = float(prime_save)
    prime = 1                # Vi assume that the number is Prime!
    numb_div = 0
    rest  = 1.0
    test  = 1.0
    potens = 1.0
    potens = 0
    print("factorizing !         ")
    print("")
    print("Number ",prime_save," is factorized! ")
    prime_numb = prime_save
    while divisor <= prime_numb and prime_numb > 2: 
        rest = prime_numb/divisor
        test = math.floor(rest)             
        while rest == test and prime_numb >= divisor: 
            prime_numb = rest
            rest = (prime_numb/divisor) # We shall see how many times
            test = math.floor(rest)     # we can divide with divisor     
            potens += 1
            prime += 1
        if potens > 0:
            print(divisor, end='')
            if potens > 1:
                numb_div += 1
                print(" ^",potens, end='')
            potens = 0
            if prime_numb > divisor:              #här
                print("   *  ", end='')
        divisor += 1
    if prime == 1 or prime == 2 and numb_div <= 1:
        print(" is prime!  ")          
    return 0

def main():
    forts = 1
    while forts != 0:
        introFunction()
        inputFunction()
        print("")
        print("")
        forts = input("continue = 1,  end = 0                       ")
        if forts == '0':
                break
    return 0

def inputFunction():
    print("inputFunction ")     
    print("Which number should be factored?                    ")
    prime_numb = input("It should be 2 or larger.                    ")
    prime_numb = int(prime_numb)
    while prime_numb < 2:
        print("      ")
        prime_numb = input("It should be 2 or larger.                    ")
        prime_numb = int(prime_numb)
    prime_Factor(prime_numb)
    return 0

main()


