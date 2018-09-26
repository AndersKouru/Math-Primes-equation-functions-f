# Solves second degree equations!
# Anders Kouru 3 july 2014

# The equation x^2 -x -2 = 0, have the solutions x1 = -1, x2 = -2

import math

def introFunction():
    print("This function Solves Second degree equations!")

def secondDegreeEquation(p,q):
    #print("p = ",p)
    #print("q = ",q)
    deskriminant = 1.0
    num = 1.0
    x1  = 1.0
    x2  = 1.0
    rot = 1.0
    deskriminant = ((p*p)/4.0) -q
    #print("deskriminant = ",deskriminant)
    num = deskriminant/2.0
    num = -(p/2.0)
    #print("num = ",num)
    if deskriminant >= 0:
        rot = pow(deskriminant,0.5)
        x1  = num - rot
        x2  = num + rot
        print("")
        print("The ekvation   x2 ",end="")
        if p >= 0:
            print(" +",p,"x ",end="")
        else:
            print(" ",p,"x ",end="")

        if q >= 0:
            print("  +",q," = 0")
        else:
            print("  ",q," = 0")
        print("have as solutions")
        print("")
        print("x1 = ",x1)
        print("x2 = ",x2)
    else:
        print("The equation has imaginary roots ")
        print(" Re = ",num," IM = +/- ",deskriminant)
    return 0
        
def main():
    forts = 1
    while forts != 0:
        introFunction()
        inputFunction()
        print("")
        forts = input("continue = 1,  end = 0                           ")
        if forts == '0':
                break
    return 0

def inputFunction():    
    print("Write the Second degree function in the form    ")
    print("")
    p = input(" x^2 + Ax + B = 0,  Input A                      ")
    p = float(p)                                                      # p = B
    q = input("Input B, the constant term                       ")    # q = C
    q = float(q)
    secondDegreeEquation(p,q)
    return 0

main()
