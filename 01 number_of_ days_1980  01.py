# Antal dagar
# Computes the number of days since 1980.0 for Astronomy
# Anders Kouru     22 september 2015

import math
Start_year = 1980.0


def inputFunction(yr,mth,dd,hr,mn):
    yr = input('Which year ?                      ')
    yr = int(yr)
    print("Which month ? between 1 and 12           ")
    mth = input('Which month                        ')
    mth = int(mth)
    while     (mth < 1) or (mth > 12):
        mth = input('Which month? between 1 annd 12     ')
        mth = int(mth)
    print("Which day ? between 1 and 31            ")
    dd   = input('Which day                          ')
    dd   = int(dd)
    while     (dd < 1) or (dd > 31):
        dd  = input('Which day? between 1 annd 31       ')
        dd  = int(dd)
    print("Which hour ? between 0 and 24           ")
    hr  = input('Which hour                         ')
    hr  = int(hr)
    while     (hr < 0) or (hr > 24):
        hr  = input('Which hour? between 0 annd 24      ')
        hr  = int(hr)
    print("Which minute ? between 0 and 60         ")
    mn  = input('Which minute?                      ')
    mn  = int(mn)
    while     (mn < 0) or (mn > 60):
        mn  = input('Which minute? between 0 annd 60    ')
        mn  = int(mn)
    return yr,mth,dd,hr,mn             


def number_of_days(yr,mth,dd,hr,mn):
    f_yr      = 1.0
    days      = 1.0
    farb_tal  = 1.0
    ftal      = 1.0
    ftal2     = 1.0
    ftal3     = 1.0
    start     = 1.0
    rest      = 1.0
    test100   = 1.0
    test400   = 1.0
    skott     = 1.0
    fday      = 1.0
    ftid      = 1.0
    fday      = dd
    ftal      = 0
    start     = yr
    if yr > Start_year:
        start = Start_year
        while start < yr:
            test4 = start/4.0    # test if year is a leap year
            rest  = floor(test4)
            if test4  != rest:
                ftal  += 365
                skott = 0
            else:
                test100 = start/100
                rest    = floor(test100)
                if test100  != rest:
                    ftal    += 366
                    skott   =  1.0
                else:
                    test400 = start/ 400     # all century years are not leap years
                    rest    = floor(test400)
                    if test400 != rest:
                        ftal  += 365
                        skott  = 0
                    else:
                        ftal  += 366         # can also be a leap year i century year is divided by 400
                        skott  = 1.0
            start  += 1.0
    if yr < Start_year:
        start = Start_year - 1.0    # we begin at 1979
        while start >= yr:
            test4 = start/4.0       # test if year is a leap year
            rest  = floor(test4)
            if test4  != rest:
                ftal  -= 365
                skott  = 0
            else:
                test100 = start/100
                rest    = floor(test100)
                if test100  != rest:
                    ftal    -= 366
                    skott   =  1.0
                else:
                    test400 = start/ 400     # all century years are not leap years
                    rest    = floor(test400)
                    if test400 != rest:
                        ftal  -= 365
                        skott  = 0
                    else:
                        ftal  -= 366         # can also be a leap year i century year is divided by 400
                        skott  = 1.0
            start  -= 1.0
    if mth == 1:                             # adding days in the months gone!
        ftal  += 0
    if mth == 2:
        ftal  += 31
    if mth == 3:
        ftal  += 59
    if mth == 4:
        ftal  += 90
    if mth == 5:
        ftal  += 120
    if mth == 6:
        ftal  += 151
    if mth == 7:
        ftal  += 181
    if mth == 8:
        ftal  += 212
    if mth == 9:
        ftal  += 243
    if mth == 10:
        ftal  += 273
    if mth == 11:
        ftal  += 304
    if mth == 12:
        ftal  += 334
    f_yr = yr            # testing to see if this year is a leap year
    test4 = f_yr/4.0
    rest = floor(test4)
    if test4 != rest:
        skott = 0
    else:
        test100 = f_yr/100
        rest    = floor(test100)
        if test100 != rest:
            skott = 1.0  # if the year is not a century year it is a leap year
        else:
            test400 = f_yr/400
            rest = floor(test400)
            if test400 != rest:
                skott = 0
            else:
                skott = 1.0
    if (mth >= 3) and (skott == 1.0):
        ftal += 1.0
    #print("skott = ",skott)
    ftal2 = hr              # adding number of hours!
    ftal3 = ftal2/24.0
    ftal += ftal3
    ftal2 = mn              # adding number of minutes!
    ftal3 = ftal2/1440.0
    ftal += ftal3           
    ftal += dd              # add number of days in the month
    days = ftal
    return days


def floor(num):                         # floor(25.3) returns   25.0
    tal = float(num)
    ital = int(num)
    numrest = tal - ital
    tal -= numrest
    return tal


def main():
    yr   = int(1)
    mth  = int(1)
    dd   = int(1)
    hr   = int(1)
    mn   = int(1)
    days = 1.0
    keep_on_going = 1               # continue = 1
    while keep_on_going != 0:
        yr,mth,dd,hr,mn = inputFunction(yr,mth,dd,hr,mn)
        print("year = ",yr, "month = ",mth, "day = ",dd, "hour = ",hr, " minute = ",mn)
        days = number_of_days(yr,mth,dd,hr,mn)
        print("Number of days =                 ",days)
        keep_on_going = input("Keep on going = 1 end = 0          ")
        keep_on_going = int(keep_on_going)
        if keep_on_going == 0:
            break
        print("")
    return(0)
       
main()       

