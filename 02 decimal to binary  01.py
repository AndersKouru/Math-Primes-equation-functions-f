# Decimal to binary
# converts decimal numbers to binary!
# Anders Kouru     11 september 2015


import math

def inputFunction(dd):
    print('Which decimal do you want in binary? ' )
    dd = input('Zero ends!                       ')
    dd = int(dd)
    return(dd)             

def decimal_to_binary(dd):
    decimal = 1.0
    decimal = dd
    binary = []
    ftal  = 1.0
    rest  = 1.0
    j= int(1)
    while dd >= 1:         # decimal to binary conversion
        dd   /= 2.0
        ftal = floor(dd)
        rest  = dd - ftal
        dd    = ftal       # after the division, the rest must be discarded

        if rest == 0:
            binary.append(0)
        else:
            binary.append(1)
    binary.reverse()
    print("decimal = ",decimal," in binary = ",end= " ")
    
    # Now comes printing out the binary list!
    for a in binary:                    
           print("{:2}".format(a*j),end='')
    print("")
    return (0)
    
def floor(num):                         # floor(25.3) returns     25.0
    tal = float(num)
    ital = int(num)
    numrest = tal - ital
    tal -= numrest
    return tal

def main():
    dd = int(1)
    decimal = int(1)
    forts = 1               # continue = 1
    while forts != 0:
        dd = inputFunction(dd)
        if dd == 0:
            break 
        decimal_to_binary(dd)
        print("")
    return(0)
       
main()       

