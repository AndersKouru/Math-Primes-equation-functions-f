
# Faktoriserar tal
# Anders Kouru 30 juni 2014


import math


def introFunction():
        print("This function Factors numbers into Primes!")


def floor(num):
        tal = float(num)
        ital = int(num)
        numrest = tal - ital
        tal -= numrest
        return tal


def primeFactor(prim_tal):
        divisor = 2.0
        prim_spar = prim_tal
        end = pow(prim_spar,0.5)
        end_spar = 1
        end_spar = int(end)
        #print("end = ",end_spar," skulle kunna spara tid!")
        prim_spar = float(prim_spar)
        prim = 1                # Vi antar att talet är prim!
        antal_div = 0
        rest  = 1.0
        test  = 1.0
        potens = 1.0
        potens = 0
        print("factorizing !         ")
        print("")
        print("Talet ",prim_spar," faktoriseras! ")
        prim_tal = prim_spar
        while divisor <= prim_tal and prim_tal > 2:  # pröva med end istället för prim_tal
            rest = prim_tal/divisor
            test = floor(rest)
            while rest == test and prim_tal >= divisor:# pröva med end istället för divisor
                prim_tal = rest
                rest = (prim_tal/divisor) # Vi ska se hur många gånger
                test = floor(rest)        # det går att dividera med divisor
                potens += 1
                prim += 1
            if potens > 0:
                print(divisor, end='')
                if potens > 1:
                    antal_div += 1
                    #print("   ")
                    print(" exp",potens, end='')
                potens = 0
                if prim_tal > divisor:
                    print("   *  ", end='')
            divisor += 1
        if prim == 1 or prim == 2 and antal_div <= 1:
            print(" is Prime!  ") # print(prim_spar, " is Prime!  ")           
        return 0


#prim_spar = 2
prim_tal  = 2
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
        #forts = int(forts)


pp = '2'
def inputFunction():
    print("inputFunction ")     
    print("Which number should be factored?                    ")
    prim_tal = input("It should be 2 or larger.                    ")
    prim_tal = int(prim_tal)
    #print("prim_tal i inputFunction = ",prim_tal)
    while prim_tal < 2:
        print("      ")
        prim_tal = input("It should be 2 or larger.                    ")
        prim_tal = int(prim_tal)
        print("prim_tal i inputFunction = ",prim_tal)
    primeFactor(prim_tal)
    

main()


