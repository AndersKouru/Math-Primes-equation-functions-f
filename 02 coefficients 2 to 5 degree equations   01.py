#Computes coefficients for fifth degree equations
#Anders Kouru   25 July 2014


import math

degree = float(1)
def introFunction():
    degree = float(1)
    while degree != 0 or degree > 5.0:
        print("")
        print("Computes coefficients of second to fifth degree equations!")
        print("Input degree 2, to 5:th degree to find coefficients  =      ")
        degree = input("zero ends!                                                    ")
        degree = float(degree)
        inputFunction(degree)
        return degree

def main():
    forts = 1
    while forts != 0:
        introFunction()
        #inputFunction(degree)
        print("")
        forts = input("continue = 1,  end = 0                                        ")
        if forts == '0':
                break
        #forts = int(forts)


pp = '2'
def inputFunction(degree):
    r1 = float(1)
    r2 = float(1)
    r3 = float(1)
    r4 = float(1)
    r5 = float(1)

    if degree == 2:
        p  = float(1)   # första gradskoefficienten      px
        q  = float(1)   # konstant termen                q
        print("Input 2 roots for a second degree equation    ")
        r1 = input("Input the first root for a second degree equation r1 = ?      ")
        r1 = float(r1)
        r2 = input("Input second root for a second degree equation    r2 = ?      ")
        r2 = float(r2)
        print("")
        print("        r1 =  ",r1,"      r2 =  ",r2)
        print("")
        p  = (r1 + r2)
        p  *= -1.0
        q  = (r1*r2)
        print("x2  +    p   x    +  q       =  0       ")
        #print("")
        print("x2  +  ",p,"x    +",q,"     =  0   ")
        print("")
        print("har rötterna x1 = ",r1,"    x2 = ",r2)
        print("")
        print("p = ",p)
        print("q = ",q)          


    if degree == 3:
        r1 = float(1)
        r2 = float(1)
        r3 = float(1)
        p  = float(1)   # andra gradskoefficienten      px2
        q  = float(1)   # första gradskoefficienten     qx
        r  = float(1)   # kontant termen                r
        print("Input 3 roots for a third degree equation    ")
        r1 = input("Input the first root for a third degree equation r1 = ?       ")
        r1 = float(r1)
        r2 = input("Input second root for a third degree equation    r2 = ?       ")
        r2 = float(r2)
        r3 = input("Input third root for a third degree equation     r3 = ?       ")
        r3 = float(r3)
        print("")
        print("        r1 =  ",r1,"     r2 = ",r2,"     r3 = ",r3)
        print("")
        p  = (r1 + r2 + r3)
        p  *= -1.0

        q  = ((r1*r3) + (r2*r3) + (r1*r2))

        r  = (r1*r2*r3)
        r  *= -1.0

        print("x3  +    p   x2   +  q   x   +    r     =  0   ")
        #print("")
        print("x3  +  ",p,"x2   +",q,"x   +  ",r,"  =  0   ")
        print("")
        print("har rötterna x1 = ",r1,"    x2 = ",r2,"   x3 = ",r3)
        print("")
        print("p = ",p)
        print("q = ",q)
        print("r = ",r)           

    if degree == 4:
        p  = float(1)   # tredje gradskoefficienten      px3
        q  = float(1)   # andra  gradskoefficienten      qx2
        r  = float(1)   # första gradskoefficienten      rx
        s  = float(1)   # kontant termen                 s
        print("Input 4 roots for a fourth degree equation    ")
        r1 = input("Input the first root for a fourth degree equation r1  = ?     ")
        r1 = float(r1)   
        r2 = input("Input second root for a fourth degree equation    r2  = ?     ")
        r2 = float(r2)
        r3 = input("Input third root for a fourth degree equation     r3  = ?     ")
        r3 = float(r3)
        r4 = input("Input fourth root for a fourth degree equation    r4  = ?     ")
        r4 = float(r4)
        print("")
        print("     r1 = ",r1,"     r2 = ",r2,"     r3 = ",r3,"     r4 = ",r4)
        print("")
        p  = (r1 + r2 + r3 +r4)
        p  *= -1.0
        q  = ((r1*r2) + (r1*r3) + (r1*r4) +(r2*r3) + (r2*r4) + (r3*r4))
        r  = ((r1*r2*r3) +(r1*r2*r4) + (r1*r3*r4) + (r2*r3*r4))
        r  *= -1.0
        s  = (r1*r2*r3*r4)
        print("x4  +    p      x3   +   q    x2  +      r   x     +    s    =  0   ")
        #print("")
        print("x4  +  ",p,"  x3   + ",q," x2  +  ",r," x     + ",s,"  =  0   ")
        print("")
        print("har rötterna x1 = ",r1,"    x2 = ",r2,"   x3 = ",r3,"  x4 = ",r4)
        print("")
        print("p = ",p)
        print("q = ",q)
        print("r = ",r)
        print("s = ",s)

    if degree == 5:
        p  = float(1)   # fjärde gradskoefficienten      px4
        q  = float(1)   # tredje gradskoefficienten      qx3
        r  = float(1)   # andra  gradskoefficienten      rx2
        s  = float(1)   # första gradskoefficienten      sx
        t  = float(1)   # konstant term                  t
        print("Input 5 roots for a fifth degree equation    ")
        r1 = input("Input the first root for a fifth degree equation r1  = ?      ")
        r1 = float(r1)
        r2 = input("Input second root for a fifth degree equation    r2  = ?      ")
        r2 = float(r2)
        r3 = input("Input third root for a fifth degree equation     r3  = ?      ")
        r3 = float(r3)
        r4 = input("Input fourth root for a fiftth degree equation   r4  = ?      ")
        r4 = float(r4)
        r5 = input("Input fifth root for a fiftth degree equation    r5  = ?      ")
        r5 = float(r5)
        print("")
        print("  r1 = ",r1,"     r2 = ",r2,"     r3 = ",r3,"     r4 = ",r4,"     r5 =",r5)
        print("")
        p  = (r1 + r2 + r3 +r4 + r5)
        p  *= -1.0
        q  = ((r1*r2) + (r1*r3) + (r1*r4) + (r1*r5) + (r2*r3) + (r2*r4) + (r2*r5) +(r3*r4) +(r3*r5) + (r4 * r5) )
        r  = ((r1*r2*r3) +(r1*r2*r4) + (r1*r2*r5) + (r1*r3*r4) +(r1*r3*r5)+ (r1*r4*r5)+ (r2*r3*r4) + (r2*r3*r5) +(r2*r4*r5)+(r3*r4*r5))
        r  *= -1.0
        s  = (r1*r2*r3*r4) + (r1*r2*r3*r5) + (r1*r2*r4*r5) + (r1*r3*r4*r5) + (r2*r3*r4*r5)
        t  = (r1*r2*r3*r4*r5)
        t  *= -1.0
        print("x5  +     p    x4   +   q    x3   +     r     x2     +    s   x   +    t     =  0 ")
        #print("")
        print("x5  +  ",p," x4   + ",q," x3   +  ",r," x2     + ",s,"x   + " ,t,"     =  0   ")
        print("")
        print("har rötterna x1 = ",r1,"   x2 = ",r2,"   x3 = ",r3,"    x4 = ",r4,"  x5 = ",r5," =  0 ")
        print("")
        print("p = ",p)
        print("q = ",q)
        print("r = ",r)
        print("s = ",s)
        print("t = ",t)
        
    return 0

main()

