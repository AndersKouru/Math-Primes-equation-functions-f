# Solves third degree equations!
# Anders Kouru 9 july 2014

# The ekvation x3 -6x2 +11x -6 = 0, has solutions  x1 = 1, x2 = 2, x3 = 3

import math

def introFunction():
    print("This function Solves Third degree equations!")

def thirdDegreeEquation(p,q,r):
    print("")
    print("X^3 + ",p,"X^2 +",q,"X +",r," = 0")
    print(" (has the solution/solutions) ")
    test = float(1)
    m_720 = float(720.0)
    m_1440 = float(1440.0)
    m_720 = math.radians(m_720)
    m_1440 = math.radians(m_1440)
    a1 = float(p)
    a2 = float(q)
    a3 = float(r)
    Q  = float(1)
    R  = float(1)
    R2_Q3 = float(1)
    theta = float(1)
    x1    = float(1)
    x2    = float(1)
    x3    = float(1)
    num   = float(1)
    num2  = float(1)
    num3  = float(1)
    num4  = float(1)
    num5  = float(1)
    num6  = float(1)
    num6  = a1/3.0                  
    num7  = float(1)
    num8  = float(1)
    num9  = float(1)
    num10 = float(1)
    num11 = float(1)
    num12 = float(1)
    num13 = float(1)
    num14 = float(1)
    Q = ((a1*a1) -(3.0 *a2))/9.0
    R  = ((2.0 *a1*a1*a1)-(9.0 *a1*a2) +(27.0*a3))/54.0
    R2_Q3 = (R*R) - (Q*Q*Q)
    if R2_Q3 <= 0: #if R2_Q3 <= 0      # the number of solutions = 3
        num  = math.sqrt(Q*Q*Q)
        if num == 0:
            num += 0.00000000000000000001
        num2 = R/num
        num3 = math.radians(num2)
        theta = math.acos(num3)     
        num = -2.0 * math.sqrt(Q)
        num13 = math.cos(theta/3.0)
        x1  = num * math.cos(theta/3.0) - a1/3.0
        print("")
        print("x1 = ",x1)                           #x1
        
        num4  = math.degrees(m_720)
        num5  = (theta + m_720)/3.0
        num7 = math.cos(num5)
        num8 = math.degrees(num8)
        num9 = (num * num7)
        x2 = num9 -num6
        print("")
        print("x2 = ",x2)                           #x2
        
        num4  = math.degrees(m_1440)
        num5  = (theta + m_1440)/3.0
        num7 = math.cos(num5)
        num8 = math.degrees(num7)
        num9 = (num * num7)
        x3 = num9 -num6
        print("")
        print("x3 = ",x3)                           #x3
    else:                       #The number of solutions = 1
        print("")
        num4  = math.sqrt(R2_Q3)
        num5  = math.fabs(R)
        num7 = num4 + num5
        num8 = math.pow(num7,1/3.0)
        
        num9 = num8 + (Q/num8)
        if R < 0:
            num10 = num9 * 1.0
        else:
            num10 = num9 * (-1.0)
        x1 = num10 - num6
        print("")
        print("x1 = ",x1)
    return 0    

def main():
    forts = 1
    while forts != 0:
        introFunction()
        inputFunction()
        print("")
        print("")
        forts = input("continue = 1,  end = 0                           ")
        if forts == '0':
                break
    return 0

def inputFunction():    
    print("Write the Third degree function in the form    ")
    print("")
    print("Ax3 + Bx2 + Cx + D = 0, Let A = 1, Input B            ")
    p = input("the coefficient for x2                            ")
    p = float(p)                                                      # p = B
    q = input("Input C the coefficient for x                     ")   # q = C
    q = float(q)
    r = input("Input D, the constant term                        ")   # r = D
    r = float(r)
    thirdDegreeEquation(p,q,r)
    return 0

main()
