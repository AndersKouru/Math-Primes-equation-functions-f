# Horners method Solves equations
# Anders Kouru    2 july 2014
# some tidying up dec 25 2018

import math

MAX_EQUATION = int(5)
MAX_TRIES    = int(400)
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
    print("This program solves ekvations using Horners Method!")


def inputCoeff(degree):
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
    c = degree                      #Prints the equation!
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
    start = num
    return start


def find_start(ekv_z,degree,start2,y_noll):
    h_noll = float(0.1)
    h_noll = y_noll
    h_noll = float(h_noll)
    y_ett  = float(0.1)
    z_noll = float(1.0)
    z_prim = float(1.0)
    #ekv_z.reverse()
    #print("ekv_z =          ",ekv_z)
    new_start = ekv_z[:]
    #print("new_start =      ",new_start)
    c  = int(0)
    ftal   = float(1)
    ftal   = start2
    ftal   = float(ftal)
    ftal2  = float(0)
    ftal3  = float(0)
    #print("ekv_z =          ",ekv_z)
    if degree == 2 or degree == 3 or degree == 4 or degree == 5:
        num_0 = new_start[0]
        num_0 = float(num_0)
        num_1 = new_start[1]
        num_1 = float(num_1)
        num_2 = new_start[2]
        num_2 = float(num_2)
        #print("")
        if degree == 2:
            #print("num_0, 1..num 2 =   ",num_0," ",num_1," ",num_2)
            num_1 += ftal    # första grads termen
            ftal2  = num_1 * ftal
            num_2 += ftal2   # konstant termen
            num_1 += ftal    
            #print("num_0, 1..num 2 =   ",num_0," ",num_1," ",num_2)
            z_noll = num_2
            z_prim = num_1
            h_noll = -(z_noll/z_prim)
            h_noll *= 0.75     #  Här kan man ändra känsligheten av algoritmen!
                              # h_noll ska egentligen vara lika med 1.0
            #print("h_noll= -(z_noll/z_prim)= ",h_noll,"=  -",z_noll,"/",z_prim)
            y_ett  = h_noll + y_noll
            y_noll = y_ett
            #print("y_noll = ",y_noll)

        if degree == 3:
            num_3 = new_start[3]
            num_3 = float(num_3)
            #print("num_0, 1..num 3 =   ",num_0," ",num_1," ",num_2," ",num_3)
            num_1 += ftal    # andra grads termen
            ftal2  = num_1 * ftal
            num_2 += ftal2   # första grads termen
            num_1 += ftal
            ftal3 = num_2 * ftal
            num_3 += ftal3   # konstant termen är färdig!
            ftal3 = num_1 * ftal
            num_2 += ftal3   # första grads termen är färdig!
            #print("num_0, 1..num 3 =   ",num_0," ",num_1," ",num_2," ",num_3)
            num_1 += ftal    # andra grads termen är färdig!
            #print("num_0, 1..num 3 =   ",num_0," ",num_1," ",num_2," ",num_3)
            
            #print("num_0, 1..num 3 =   ",num_0," ",num_1," ",num_2," ",num_3)

            z_noll = num_3
            z_prim = num_2
            h_noll = -(z_noll/z_prim)
            h_noll *= 0.75     #  Här kan man ändra känsligheten av algoritmen!
                              # h_noll ska egentligen vara lika med 1.0
            #print("h_noll= -(z_noll/z_prim)= ",h_noll,"=  -",z_noll,"/",z_prim)
            y_ett  = h_noll + y_noll
            y_noll = y_ett
            #print("y_noll = ",y_noll)

        if degree == 4:
            num_3 = new_start[3] # förstagrads termen
            num_3 = float(num_3)
            num_4 = new_start[4] # konstant termen
            num_4 = float(num_4)
            #print("num_0, 1..num 3 =   ",num_0," ",num_1," ",num_2," ",num_3," ",num_4)

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
            num_3  += ftal2   # första gradstermen borde vara färdig = z_prim

            num_1  += ftal    # tredje grads termen borde vara färdig!
            #print("num_0, 1..num 3 =   ",num_0," ",num_1," ",num_2," ",num_3," ",num_4)
            z_noll = num_4
            z_prim = num_3
            h_noll = -(z_noll/z_prim) #h_noll = -(z_noll/z_prim)
            
            h_noll *= 0.75    #  Här kan man ändra känsligheten av algoritmen!
                              # h_noll ska egentligen vara lika med 1.0
            
            #print("h_noll= -(z_noll/z_prim)= ",h_noll,"=  -",z_noll,"/",z_prim)
            y_ett  = h_noll + y_noll
            y_noll = y_ett
            #print("y_noll = ",y_noll)

        if degree == 5:
            num_3 = new_start[3] # andragrads termen
            num_3 = float(num_3)
            num_4 = new_start[4] # förstagrads termen
            num_4 = float(num_4)
            num_5 = new_start[5] # konstant termen
            num_5 = float(num_5)
            #print("num_0, 1..num 5 =  ",num_0," ",num_1," ",num_2," ",num_3," ",num_4," ",num_5)
            

            num_1  += ftal    # fjärde grads termen
            ftal2  = num_1 * ftal
            num_2  += ftal2   # tredje grads termen
            #print("num_0, 1..num 5 =   ",num_0," ",num_1," ",num_2," ",num_3," ",num_4," ",num_5)
    
            num_1  += ftal
            ftal3  = num_2 * ftal
            num_3  += ftal3   # andra grads termen borde snart vara färdig!

            ftal2  = num_3 * ftal
            num_4  += ftal2   # första grads termen borde snart vara färdig!
            ftal2  = num_4 * ftal
            num_5  += ftal2   # konstant termen borde vara färdig! Här är jag nu! = z_noll

            
            #print("num_0, 1..num 5 =   ",num_0," ",num_1," ",num_2," ",num_3," ",num_4," ",num_5)
            ftal3  = num_1 * ftal
            num_2  += ftal3   # andra grads termen borde vara färdig!
            ftal2  = num_2 * ftal
            num_3  += ftal2   # andra gradstermen borde vara färdig
            #print("num_0, 1..num 5 =   ",num_0," ",num_1," ",num_2," ",num_3," ",num_4," ",num_5)

            num_1  += ftal    # fjärde grads termen borde snart vara färdig!
            #print("num_0, 1..num 5 =  ",num_0," ",num_1," ",num_2," ",num_3," ",num_4," ",num_5)

            z_noll = num_5
            z_prim = num_4
            h_noll = -(z_noll/z_prim) #h_noll = -(z_noll/z_prim)
            
            h_noll *= 0.2     #  Här kan man ändra känsligheten av algoritmen!
                              # h_noll ska egentligen vara lika med 1.0
            
            #print("h_noll= -(z_noll/z_prim)= ",h_noll,"=  -",z_noll,"/",z_prim)
            y_ett  = h_noll + y_noll
            y_noll = y_ett
            #print("y_noll = ",y_noll)
    return y_noll
  
    

def find_z(ekv_z,copy,degree,start):
    c  = int(0)
    ftal   = float(1)
    ftal   = start
    ftal   = float(ftal)
    ftal2  = float(0)
    ftal3  = float(0)
    num_3  = float(0)
    num_4  = float(0)
    #print("ekv copy =          ",copy)
    #print("ekv_z    =          ",ekv_z)
    if degree == 2 or degree == 3 or degree == 4 or degree == 5:
        num_0 = ekv_z[0]
        num_0 = float(num_0)
        num_1 = ekv_z[1]
        num_1 = float(num_1)
        num_2 = ekv_z[2]
        num_2 = float(num_2)
        if degree == 2:
            #print("num_0, 1..num 2 =   ",num_0," ",num_1," ",num_2)
            num_1 += ftal    # första grads termen
            ftal2  = num_1 * ftal
            num_2 += ftal2   # andra grads termen
            num_1 += ftal
            #print("num_0, 1..num 2 =   ",num_0," ",num_1," ",num_2)
            ekv_z[0]  = num_0
            ekv_z[1]  = num_1
            ekv_z[2]  = num_2
            #ekv_z.reverse()     # vänder termerna för bra utskrift!
            
        if degree == 3:
            num_3 = ekv_z[3]
            num_3 = float(num_3)
            #print("num_0, 1..num 3 =   ",num_0," ",num_1," ",num_2," ",num_3)
            num_1 += ftal    # första grads termen
            ftal2  = num_1 * ftal
            num_2 += ftal2   # andra grads termen

            num_1 += ftal
            ftal3 = num_2 * ftal
            num_3 += ftal3   # första grads termen borde vara färdig!
            
            ftal3 = num_1 * ftal
            num_2 += ftal3   # andra grads termen 

            num_1 += ftal    # första grads termen borde vara färdig!
            #print("num_0, 1..num 3 =   ",num_0," ",num_1," ",num_2," ",num_3)
            
            ekv_z[0]  = num_0   # 3:de grads termen
            ekv_z[1]  = num_1   # 2 = andra grads termen
            ekv_z[2]  = num_2   # 1 = första grads termen
            ekv_z[3]  = num_3   # 0 = konstant termen
            
            #ekv_z.reverse()     # vänder termerna för bra utskrift!
            #print("ekv_z = ",ekv_z,end=' ')

        if degree == 4:
            num_3 = ekv_z[3]
            num_3 = float(num_3)
            num_4 = ekv_z[4]
            num_4 = float(num_4)
            #print("num_0, 1..num 4 =   ",num_0," ",num_1," ",num_2," ",num_3," ",num_4)
            num_1 += ftal    # tredje grads termen
            ftal2  = num_1 * ftal
            num_2 += ftal2   # andra grads termen

            num_1  += ftal
            ftal3  = num_2 * ftal
            num_3  += ftal3   

            ftal3  = num_3 * ftal
            num_4  += ftal3   # konstant termen är färdig!
            ftal3  = num_1 * ftal
            num_2  += ftal3   # andra grads termen borde  snart vara färdig!
            ftal2  = num_2 * ftal
            num_3  += ftal2   # första gradstemen är färdig! 

            num_1  += ftal    # tredje grads termen borde snart vara färdig!
            ftal2  = num_1 * ftal
            num_2  += ftal2   # andra grads termen är färdig! 

            num_1  += ftal    # tredje grads termen är färdig! 
            
            #print("num_0, 1..num 4 =   ",num_0," ",num_1," ",num_2," ",num_3," ",num_4)
            
            ekv_z[0]  = num_0   # 4:de grads termen
            ekv_z[1]  = num_1   # 3:de grads termen
            ekv_z[2]  = num_2   # 2 = andra grads termen
            ekv_z[3]  = num_3   # 1 = första grads termen
            ekv_z[4]  = num_4   # 0 = konstant termen

        if degree == 5:
            num_3 = ekv_z[3]
            num_3 = float(num_3)
            num_4 = ekv_z[4]
            num_4 = float(num_4)
            num_5 = ekv_z[5]
            num_5 = float(num_5)
            #print("num_0, 1..num 5 =   ",num_0," ",num_1," ",num_2," ",num_3," ",num_4," ",num_5)
            num_1 += ftal    # fjärde grads termen
            ftal2  = num_1 * ftal
            num_2 += ftal2   # tredje grads termen
            #print("num_0, 1..num 5 =   ",num_0," ",num_1," ",num_2," ",num_3," ",num_4," ",num_5)

            num_1  += ftal
            ftal3  = num_2 * ftal
            num_3  += ftal3
            ftal3  = num_3 * ftal
            num_4  += ftal3          # förstagrads termen är snart färdig!
            
            ftal3  = num_4 * ftal
            num_5  += ftal3          # kontant termen är färdig!
            #print("num_0, 1..num 5 =   ",num_0," ",num_1," ",num_2," ",num_3," ",num_4," ",num_5)

            ftal3  = num_1 * ftal
            num_2  += ftal3         
            ftal3  = num_2  * ftal
            num_3  += ftal3           
            ftal3  = num_3 * ftal
            num_4  += ftal3           # förstagrads termen är färdig!

            #print("num_0, 1..num 5 =   ",num_0," ",num_1," ",num_2," ",num_3," ",num_4," ",num_5)
            num_1  += ftal
            ftal3  = num_1 * ftal
            num_2  += ftal3   # tredje grads termen borde  snart vara färdig!   Här är jag!
            ftal3  = num_2 * ftal
            num_3  += ftal3
            #print("num_0, 1..num 5 =   ",num_0," ",num_1," ",num_2," ",num_3," ",num_4," ",num_5)
            num_1  += ftal    # fjärde grads termen borde snart vara färdig!
            ftal2  = num_1 * ftal
            num_2  += ftal2   # tredje grads termen är snart färdig!
            #print("num_0, 1..num 5 =   ",num_0," ",num_1," ",num_2," ",num_3," ",num_4," ",num_5)

            num_1  += ftal    # fjärde grads termen är snart färdig!
            #print("num_0, 1..num 5 =   ",num_0," ",num_1," ",num_2," ",num_3," ",num_4," ",num_5)           
            
            ekv_z[0]  = num_0   # 5:te grads termen
            ekv_z[1]  = num_1   # 4:de grads termen
            ekv_z[2]  = num_2   # 3:de grads termen
            ekv_z[3]  = num_3   # 2 = andra grads termen
            ekv_z[4]  = num_4   # 1 = första grads termen
            ekv_z[5]  = num_5   # 0 = konstant termen
    return ekv_z
    

def hornersMethod(copy,degree):
    x1     = float(1)
    start  = float(1)
    start2 = STARTVALUE
    ftal2   = float(1)
    y_noll = float(0.1)
    keep_on_going = float(1)
    #print("")
    #print("degree HornersMethod =  ",degree)
    copy = ekv[0:degree+1]
    #print("")
    #print("copy = ekv[0:degree] =  ",copy,end='  ')
    #print("")
    copy.reverse()
    #print("")
    #print("copy reverse         =  ",copy)

    while keep_on_going != 0:
        print("ekv copy i Horner = ",copy)    # Här är jag!
        ekv_z = copy[:]
        #print("")
        print("ekv_z             = ",ekv_z)
        print("")
        start = StartValue(start)
        #print("start = ",start)
        find_z(ekv_z,copy,degree,start)
        for i in range(0,MAX_TRIES,1):
            y_noll = find_start(ekv_z,degree,start2,y_noll)
            ftal2 = start2
            start2 = y_noll
            #print("ftal2 = start = ",ftal2,"y_noll = ",y_noll)
        start  = float(start)
        start2 = float(start2)
        x1     = start + start2
        print("")
        print("x1 = ",x1)
        print("")
        keep_on_going = input("Choose new start value? keep on going? Zero ends!  ")
        keep_on_going = float(keep_on_going)
    return 0


pp = '2'
def inputFunction():
    ekv        = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0, 0.0, 0.0, 0.0, 0.0]
    ekv_save   = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0, 0.0, 0.0, 0.0, 0.0]
    copy = ekv[:]           #copy = slice ekv[]
    #print("copy = ",copy,end='  ')
    #print("")
 
    degree = int(12)
    ekv = ekv_save       # återställer ekv till default storlek
    #print("ekv   = ",ekv,end='   ')
    #print("")
    copy= ekv_save
    print(" Max_degree = ",MAX_EQUATION)
    print("Which Degree of the equation to be solved? 2...5          ")
    while degree < 2 or degree > MAX_EQUATION:
        print("degree should be between 2 and ",MAX_EQUATION,end='              ')
        degree = input()
        degree = int(degree)
        #print("degree i inputFunction =                      ",degree)
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















