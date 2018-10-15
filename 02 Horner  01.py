# Horners method Solves equations up to the fifth degree!
# Anders Kouru    2 july 2014

import math

MAX_EQUATION = int(5)
MAX_TRIES    = int(100000)              # int(300) old value
STARTVALUE   = float(0.01)

ekv        = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0, 0.0, 0.0, 0.0, 0.0]
ekv_save   = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0, 0.0, 0.0, 0.0, 0.0]
copy       = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0, 0.0, 0.0, 0.0, 0.0]

new_start  = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0, 0.0, 0.0, 0.0, 0.0]

ekv_z      = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0, 0.0, 0.0, 0.0, 0.0]
z_save     = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0, 0.0, 0.0, 0.0, 0.0]

num_0  = float(0)
num_1  = float(0)
num_2  = float(0)
num_3  = float(0)
num_4  = float(0)
num_5  = float(0)
num_6  = float(0)
num_7  = float(0)
num_8  = float(0)
num_9  = float(0)
num_10 = float(0)
num_11 = float(0)

def introFunction():
    print("This program solves equations using Horners Method!")
    return 0

def inputCoeff(degree):     # We input coefficients of the Equation!
    c = int(1)
    c    = degree
    coeff = float(1)
    for i in range(degree,-1,-1):
        print("")
        print("input coefficient for x",i)
        coeff = input("                            ")
        coeff = float(coeff)
        print("      ",coeff,end='')
        print(" x",i,end='')
        ekv[i]    = coeff
        copy[i]   = coeff
        ekv_z     = coeff
        z_save[i] = coeff
        print("")
    return 0

def printEkv(degree):
    c = degree                    
    for i in range(degree,-1,-1):               
        print(ekv[i],"x",c,"   + ",end='')
        c    -= 1 
        if c < 0:
            print(" =     0 ")
            print("")
            break   
    return 0

def StartValue(start_value):
    num = float(1)
    num = input("Which start value to use, to search for a solution?  ")
    print("")
    num = float(num)
    start = num
    return start 

def find_start(ekv_z,degree,start2,y_noll):
    h_noll = float(0.1)
    h_noll = y_noll
    h_noll = float(h_noll)
    y_ett  = float(0.1)
    z_noll = float(1.0)
    z_prim = float(1.0)                  
    new_start = ekv_z[:]
    c  = int(0)
    ftal   = float(1)
    ftal   = start2
    ftal   = float(ftal)
    ftal2  = float(0)
    ftal3  = float(0)
    if degree == 2 or degree == 3 or degree == 4 or degree == 5:
        num_0 = new_start[0]
        num_0 = float(num_0)
        num_1 = new_start[1]
        num_1 = float(num_1)
        num_2 = new_start[2]
        num_2 = float(num_2)
        if degree == 2:
            num_1 += ftal    # first degree term
            ftal2  = num_1 * ftal
            num_2 += ftal2   # constant term
            num_1 += ftal    
            z_noll = num_2
            z_prim = num_1
            h_noll = -(z_noll/z_prim)
            h_noll *= 0.75     #  Here you can change the sensitivity of the algorithm!
                               # h_noll should actually be = 1.0
            y_ett  = h_noll + y_noll
            y_noll = y_ett

        if degree == 3:
            num_3 = new_start[3]
            num_3 = float(num_3)
            num_1 += ftal    # working on the second degree term
            ftal2  = num_1 * ftal
            num_2 += ftal2   # working on the first degree term
            num_1 += ftal
            ftal3 = num_2 * ftal
            num_3 += ftal3   # constant term!
            ftal3 = num_1 * ftal
            num_2 += ftal3   # first degree term is done!
            num_1 += ftal    # second degree term is done!   
            z_noll = num_3
            z_prim = num_2
            h_noll = -(z_noll/z_prim)
            h_noll *= 0.75     #  Here you can change the sensitivity of the algorithm!
                               # h_noll should actually be = 1.0
            y_ett  = h_noll + y_noll
            y_noll = y_ett

        if degree == 4:
            num_3 = new_start[3] # förstagrads termen
            num_3 = float(num_3)
            num_4 = new_start[4] # konstant termen
            num_4 = float(num_4)
            num_1  += ftal    # tredje grads termen
            ftal2  = num_1 * ftal
            num_2  += ftal2   # andra grads termen
            num_1  += ftal
            ftal3  = num_2 * ftal
            num_3  += ftal3   # första grads termen 
            ftal2  = num_3 * ftal
            num_4  += ftal2   # konstant termen är färdig! = z_noll
            ftal3  = num_1 * ftal
            num_2  += ftal3   # andra grads termen 
            ftal2  = num_2 * ftal
            num_3  += ftal2   # the first degree term = z_prim
            num_1  += ftal    # third degree term!
            z_noll = num_4
            z_prim = num_3
            h_noll = -(z_noll/z_prim) #h_noll = -(z_noll/z_prim)
            h_noll *= 0.001     #  Here you change the sensitivity of the algoritm!
                                # h_noll should be = 1.0 (0.75)
            y_ett  = h_noll + y_noll
            y_noll = y_ett

        if degree == 5:
            num_3 = new_start[3] # second degree term
            num_3 = float(num_3)
            num_4 = new_start[4] # first degree term
            num_4 = float(num_4)
            num_5 = new_start[5] # constant term
            num_5 = float(num_5)
            num_1  += ftal    # forth degree term
            ftal2  = num_1 * ftal
            num_2  += ftal2   # third degree term
            num_1  += ftal
            ftal3  = num_2 * ftal
            num_3  += ftal3   # working on the second degree term!
            ftal2  = num_3 * ftal
            num_4  += ftal2   # working on the first degree termen!
            ftal2  = num_4 * ftal
            num_5  += ftal2   # constant term will be placed in = z_noll
            ftal3  = num_1 * ftal
            num_2  += ftal3   # second degree term!
            ftal2  = num_2 * ftal
            num_3  += ftal2   # third degree termen!
            num_1  += ftal    # forth degree term!
            z_noll = num_5
            z_prim = num_4
            h_noll = -(z_noll/z_prim) #h_noll = -(z_noll/z_prim)
            h_noll *= 0.2     #  Here the sensitivity of the algorithm can be changed!
                              # h_noll should actually be = 1.0
            y_ett  = h_noll + y_noll
            y_noll = y_ett
    return y_noll
  
def find_z(ekv_z,copy,degree,start):   # transforms the oringinal equation to an equation in z for best performance!
    c  = int(0)
    ftal   = float(1)
    ftal   = start
    ftal   = float(ftal)
    ftal2  = float(0)
    ftal3  = float(0)
    num_3  = float(0)
    num_4  = float(0)
    if degree == 2 or degree == 3 or degree == 4 or degree == 5:
        num_0 = ekv_z[0]
        num_0 = float(num_0)
        num_1 = ekv_z[1]
        num_1 = float(num_1)
        num_2 = ekv_z[2]
        num_2 = float(num_2)
        if degree == 2:
            num_1 += ftal    # first degree term
            ftal2  = num_1 * ftal
            num_2 += ftal2   # second degree term
            num_1 += ftal
            ekv_z[0]  = num_0
            ekv_z[1]  = num_1
            ekv_z[2]  = num_2        
            
        if degree == 3:
            num_3 = ekv_z[3]
            num_3 = float(num_3)
            num_1 += ftal   
            ftal2  = num_1 * ftal
            num_2 += ftal2  
            num_1 += ftal
            ftal3 = num_2 * ftal
            num_3 += ftal3  
            ftal3 = num_1 * ftal
            num_2 += ftal3   
            num_1 += ftal   
            ekv_z[0]  = num_0   # 3:d degree term
            ekv_z[1]  = num_1   # 2 = second degree term
            ekv_z[2]  = num_2   # 1 = first degree term
            ekv_z[3]  = num_3   # 0 = constant term

        if degree == 4:
            num_3 = ekv_z[3]
            num_3 = float(num_3)
            num_4 = ekv_z[4]
            num_4 = float(num_4)
            num_1 += ftal  
            ftal2  = num_1 * ftal
            num_2 += ftal2  
            num_1  += ftal
            ftal3  = num_2 * ftal
            num_3  += ftal3   
            ftal3  = num_3 * ftal
            num_4  += ftal3  
            ftal3  = num_1 * ftal
            num_2  += ftal3  
            ftal2  = num_2 * ftal
            num_3  += ftal2  
            num_1  += ftal   
            ftal2  = num_1 * ftal
            num_2  += ftal2   
            num_1  += ftal    
            ekv_z[0]  = num_0   # 4:th degree term
            ekv_z[1]  = num_1   # 3:d degree term
            ekv_z[2]  = num_2   # 2 = second degree term
            ekv_z[3]  = num_3   # 1 = first degree term
            ekv_z[4]  = num_4   # 0 = constant term

        if degree == 5:
            num_3 = ekv_z[3]
            num_3 = float(num_3)
            num_4 = ekv_z[4]
            num_4 = float(num_4)
            num_5 = ekv_z[5]
            num_5 = float(num_5)
            num_1 += ftal    
            ftal2  = num_1 * ftal
            num_2 += ftal2  

            num_1  += ftal
            ftal3  = num_2 * ftal
            num_3  += ftal3
            ftal3  = num_3 * ftal
            num_4  += ftal3        
            ftal3  = num_4 * ftal
            num_5  += ftal3        
            ftal3  = num_1 * ftal
            num_2  += ftal3         
            ftal3  = num_2  * ftal
            num_3  += ftal3           
            ftal3  = num_3 * ftal
            num_4  += ftal3          

            num_1  += ftal
            ftal3  = num_1 * ftal
            num_2  += ftal3   
            ftal3  = num_2 * ftal
            num_3  += ftal3
            num_1  += ftal   
            ftal2  = num_1 * ftal
            num_2  += ftal2  
            num_1  += ftal             
            ekv_z[0]  = num_0   # 5:te grads termen
            ekv_z[1]  = num_1   # 4:th degree term
            ekv_z[2]  = num_2   # 3:d degree term
            ekv_z[3]  = num_3   # 2 = second degree term
            ekv_z[4]  = num_4   # 1 = first degree term
            ekv_z[5]  = num_5   # 0 = constant term
    ekv_z.reverse()     # reversing the terms for a nice print out!
    print("The equation in z = ",ekv_z,end=' ')              
    ekv_z.reverse()     # reversing the terms!
    return ekv_z

def hornersMethod(copy,degree):    # Here we use Horners Method!
    x1     = float(1)
    start  = float(1)
    start2 = STARTVALUE
    ftal2   = float(1)
    y_noll = float(0.1)
    keep_on_going = float(1)
    copy = ekv[0:degree+1]
    copy.reverse()
    while keep_on_going != 0:
        print("The equation      = ",copy)  
        ekv_z = copy[:]
        print("")
        start = StartValue(start)
        find_z(ekv_z,copy,degree,start)
        for i in range(0,MAX_TRIES,1):
            y_noll = find_start(ekv_z,degree,start2,y_noll)
            ftal2 = start2
            start2 = y_noll
        start  = float(start)
        start2 = float(start2)
        x1     = start + start2
        print("")
        print("x                 = ",x1)
        print("")
        keep_on_going = input("Choose new start value? keep on going? Zero ends!  ")
        keep_on_going = float(keep_on_going)
        if keep_on_going == 0:
            break                        # Här är jag!
    return 0

pp = '2'
def inputFunction():
    ekv        = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0, 0.0, 0.0, 0.0, 0.0]
    ekv_save   = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0, 0.0, 0.0, 0.0, 0.0]
    copy = ekv[:]           #copy = slice ekv[]
    degree = int(12)
    ekv = ekv_save       # resetting ekv to default size
    copy= ekv_save
    print(" Max_degree = ",MAX_EQUATION)
    print("Which Degree of the equation to be solved? 2...5          ")
    while degree < 2 or degree > MAX_EQUATION:
        print("degree should be between 2 and ",MAX_EQUATION,end='              ')
        degree = input()
        degree = int(degree)
    inputCoeff(degree)
    print("")
    printEkv(degree)
    hornersMethod(copy,degree)
    return 0

def main():
    forts = float(1)
    while forts != 0:
        introFunction()
        inputFunction()
        print("")
        print("")
        forts = input("continue = 1,  end = 0                         ")
        if forts == '0':
                break
        forts = float(forts)

main()

