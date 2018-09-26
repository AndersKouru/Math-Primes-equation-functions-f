# Emulates Maria Thuns sowing Calander, calulates the Moons position in respect to the astronomical zodiac!
# 3 may 2016

# Computes the Moons position, Credits to "Med miniräknaren i rymden", Peter Duffet-Smith
# Variabel names are "UnPythonic", in order to easier follow the books varable names!
# Anders Kouru 7 october 2015


import math
import antaldagar

def degree_adjust(ftal2):
    num = 1.0
    num = ftal2
    ftal = 1.0
    while (num < 0 ) or (num > 360):
        if (num < 0):
            ftal = num + 360.0
            num   = ftal
        if (num > 360):
            ftal = num - 360.0
            num   = ftal
    return num

def sun_position(days):
    ftal   = 1.0
    ftal2  = 1.0
    ftal3  = 1.0
    ftal4  = 1.0
    ftal5  = 1.0
    ftal   = days
    N      = 1.0   
    M      = 1.0   
    radM   = 1.0
    Ec     = 1.0   
    ban_e  = 0.016718
    eg_eklipt_long_epok = 278.833540
    wg_eklipt_long_perigeum = 282.596403
    sol_eklipt_long   = 1.0
    sol_Medel_anomali = 1.0
    ftal2 = (360.0 * ftal)/(365.2422)
    N     = degree_adjust(ftal2)
    ftal3  = N + eg_eklipt_long_epok - wg_eklipt_long_perigeum  
    
    M     = degree_adjust(ftal3)
    sol_Medel_anomali = M
    radM   = math.radians(M)
    ftal4  = math.sin(radM)
    
    Ec     = (360.0 * ban_e * ftal4)/(math.pi)
    ftal5  = N + Ec + eg_eklipt_long_epok
    sol_eklipt_long = degree_adjust(ftal5)
    return sol_eklipt_long, sol_Medel_anomali
    
def moon_position(days):
    sol_eklipt_long = 1.0
    sol_Medel_anomali  = 1.0
    ftal   = 1.0
    ftal2  = 1.0
    ftal3  = 1.0
    ftal4  = 1.0
    ftal5  = 1.0
    ftal6  = 1.0
    ftal7  = 1.0
    ftal8  = 1.0
    ftal9  = 1.0
    ftal10 = 1.0
    ftal   = days
    nn     = 1.0
    mm     = 1.0
    radM   = 1.0
    eC     = 1.0
    l_moon = 1.0
    Mm     = 1.0  
    N      = 1.0  
    cc     = 1.0
    Ev     = 1.0
    Ae     = 1.0
    A3     = 1.0
    MmPrim = 1.0
    Ec     = 1.0
    A4     = 1.0
    lprim  = 1.0
    V      = 1.0
    l_2prim = 1.0
    Nprim  = 1.0
    i_moon = 5.145396
    y      = 1.0
    x      = 1.0
    tan    = 1.0
    atan   = 1.0
    moon_long = 1.0
    moon_lat = 1.0

    lmoon_long_epok = 64.975464
    pmoon_long_perigeum = 349.383063
    nodens_medel_long   = 151.950429
    sol_Medel_anomali = 1.0
    sol_eklipt_long, sol_Medel_anomali = sun_position(days)
    
    ftal2 = (13.1763966 * ftal) + lmoon_long_epok
    l_moon     = degree_adjust(ftal2)
    ftal3   = l_moon - (0.1114041 * ftal) - pmoon_long_perigeum
    Mm  = degree_adjust(ftal3)
    ftal4 = nodens_medel_long -(0.0529539 * ftal)
    N = degree_adjust(ftal4)
    cc = l_moon - sol_eklipt_long
    ftal5 = (2.0 * cc) - Mm
    radMoon   = math.radians(ftal5)
    ftal6  = math.sin(radMoon)
    Ev     = 1.2739 * ftal6
    ftal7 = math.radians(sol_Medel_anomali)
    ftal8 = math.sin(ftal7)
    Ae  = 0.1858 * ftal8
    A3  = 0.37 * ftal8
    MmPrim = Mm + Ev -Ae -A3        # reusing variables ftal2 to ftal 10
    ftal2 = math.radians(MmPrim)
    ftal3 = math.sin(ftal2)
    Ec    = 6.2886 * ftal3
    ftal4 = 2 * ftal3
    A4    = 0.214 * math.sin(ftal4)
    lprim = l_moon + Ev + Ec - Ae + A4
    ftal5 = 2.0 * (lprim - sol_eklipt_long)
    ftal6 = math.radians(ftal5)
    V     = 0.6583 * math.sin(ftal6)
    l_2prim = lprim + V
    Nprim = N - (0.16 * ftal8)

    ftal7 = math.radians(i_moon)
    ftal9 = math.radians(l_2prim - Nprim)
    y     = math.sin(ftal9) * math.cos(ftal7)
    x     = math.cos(ftal9)
    tan   = math.atan2(y,x)
    atan  = math.degrees(tan)
    moon_long = atan + Nprim
    ftal10 = math.sin(ftal9) * math.sin(ftal7)
    ftal2  = math.asin(ftal10)
    moon_lat = math.degrees(ftal2)
    return moon_long, moon_lat
    

def to_rect(long,lat):
    ftal1 = 1.0
    ftal2 = 1.0
    ftal3 = 1.0
    rect  = 1.0
    dec   = 1.0
    e     = 23.441884   # lutningen på ekliptikan
    sind  = 1.0
    d     = 1.0
    y     = 1.0
    x     = 1.0
    atan  = 1.0
    a     = 1.0
    ftal1 = math.radians(long)
    ftal2 = math.radians(lat)
    ftal3 = math.radians(e)
    sind  = (math.sin(ftal2) * math.cos(ftal3)) + (math.cos(ftal2) * math.sin(ftal3) * math.sin(ftal1))
    d     = math.degrees(sind)
    y     = (math.sin(ftal1) * math.cos(ftal3)) - (math.tan(ftal2) * math.sin(ftal3))
    x     = math.cos(ftal1)
    atan  = math.atan2(y,x)
    a     = math.degrees(atan)
    rect  = a/15.0
    if (rect < 0):
        rect = rect + 24.0
    dec = d
    return rect,dec


def more_days(rect_start,moon_rect,rect_end):
    ftal1 = 1.0
    ftal2 = 1.0
    ftal3 = int(1.0)
    ftal4 = int(1.0)
    days  = 0.0
    days_to = 0.0
    to_start = 1.0
    to_end   = 1.0
    per_hour = 0.549016525  # the moons average distance per hour in degrees!
    to_start = moon_rect - rect_start
    ftal1    = (to_start * 15.0)/ per_hour
    days     = 0.0
    while ftal1 >= 24.0:
        ftal1  = ftal1 -24.0
        days   += 1.0
    ftal3 = round(ftal1,0)      # round instead of int
    to_end   = rect_end  - moon_rect
    ftal2    = (to_end * 15.0)/ per_hour
    days_to = 0.0
    while ftal2 >= 24.0:
        ftal2    = ftal2 -24.0
        days_to  += 1.0
    ftal4 = round(ftal2,0)
    print("to_start = ",days,"days",ftal3,"hours  to_end = ",days_to," days",ftal4,"hours")
    return None

    
def harvest_days(moon_rect):   # Computes the time from the Moons lowest to the highest point in her orbit!
    rect_start = 1.0
    rect_end   = 1.0
    mr = 1.0
    mr = moon_rect   # save some printing!
    if(mr < 24.0) and (mr > 18.0):
        rect_start = mr - 18.0          # find rect hours to the start. We have a change from 24 to 0 hours
        rect_end   = 6.0 + (24.0 - mr)  #                               to take care of! 
        print("This harvesting opportunity has started!")
        
    if(mr < 6.0) and (mr > 0.0):
        rect_start = 6.0 + mr            # find rect hours to the start. We have a change from 24 to 0 hours
        rect_end   = 6.0 - mr            #                              to take care of!
        print("This harvesting opportunity is soon ending!")    
    ftal1 = 1.0
    ftal2 = 1.0
    ftal3 = int(1.0)
    ftal4 = int(1.0)
    days  = 0.0
    days_to = 0.0
    to_start = 1.0
    to_end   = 1.0
    per_hour = 0.549016525  # the moons average distance per hour in degrees!
    to_start = rect_start
    ftal1    = (to_start * 15.0)/ per_hour
    days     = 0.0
    while ftal1 >= 24.0:
        ftal1  = ftal1 -24.0
        days   += 1.0
    ftal3 = round(ftal1,0)      # round instead of int
    to_end   = rect_end
    ftal2    = (to_end * 15.0)/ per_hour
    days_to = 0.0
    while ftal2 >= 24.0:
        ftal2    = ftal2 -24.0
        days_to  += 1.0
    ftal4 = round(ftal2,0)
    print("Harvesting has already started",days,"days",ftal3,"hours ago! Harvest ends in",days_to,"days",ftal4,"hours!")
    return None


def sow_calender(yr,mth,dd,hr,mn,moon_rect,skott):
    rect_start = 1.0
    rect_end   = 1.0
    mr = 1.0
    mr = moon_rect   # save some printning!
    print("")
    print("sow_calender year ",yr,"    month =",mth,"   day =",dd,"   hour =",hr)

    if (mr >= 17.9) and (mr < 20.0):
        rect_start = 17.9
        rect_end   = 20.0
        more_days(rect_start,moon_rect,rect_end)
        print("Sagittaurius, fire, fruit! harvest!")
        
    if (mr >= 20.0) and (mr < 21.9):
        rect_start = 20.0
        rect_end   = 21.9
        more_days(rect_start,moon_rect,rect_end)
        print("Capricorn, earth, roots! harvest!")
        
    if (mr >= 21.9) and (mr < 23.5):
        rect_start = 21.9
        rect_end   = 23.5
        more_days(rect_start,moon_rect,rect_end)
        print("Aquarius, air and flowers! harvest!")
        
    if (mr >= 23.5) and (mr <= 24.0):
        rect_start = 23.5
        rect_end   = 25.90                # the real ending is 24.0 + 1.90
        more_days(rect_start,moon_rect,rect_end)
        print("Pisces, water, leaves! harvest!")
        
    if (mr >= 0.0) and (mr < 1.90):
        rect_start = -0.50                # rect_start = 0.0 - 0.5 timmar!
        rect_end   = 1.90
        more_days(rect_start,moon_rect,rect_end)
        print("Pisces, water, leaves! harvest!")
        
    if (mr >= 1.90) and (mr < 3.5):
        rect_start = 1.90
        rect_end   = 3.5
        more_days(rect_start,moon_rect,rect_end)
        print("Aries, fire, fruit! harvest!")
        
    if (mr >= 3.5) and (mr < 6.0):
        rect_start = 3.5
        rect_end   = 6.0
        more_days(rect_start,moon_rect,rect_end)
        print("Taurus, earth, roots! harvest!")

    if (mr >= 6.0) and (mr < 8.0):
        rect_start = 6.0
        rect_end   = 8.0
        more_days(rect_start,moon_rect,rect_end)
        print("Gemini, air, Planting starts, flowers!")
        
    if (mr >= 8.0) and (mr < 9.37):
        rect_start = 8.0
        rect_end   = 9.37
        more_days(rect_start,moon_rect,rect_end)
        print("Cancer, water, planting leaves!")
        
    if (mr >= 9.37) and (mr < 11.6):
        rect_start = 9.37
        rect_end   = 11.6
        more_days(rect_start,moon_rect,rect_end)
        print("Leo, fire, planting fruit!")
        
    if (mr >= 11.6) and (mr < 14.6):
        rect_start = 11.6
        rect_end   = 14.6
        more_days(rect_start,moon_rect,rect_end)
        print("Virgo, earth, planting roots!")
        
    if (mr >= 14.6) and (mr < 15.8):
        rect_start = 14.6
        rect_end   = 15.8
        more_days(rect_start,moon_rect,rect_end)
        print("Libra, air, planting flowers!")
        
    if (mr >= 15.8) and (mr < 17.9):
        rect_start = 15.8
        rect_end   = 17.9
        more_days(rect_start,moon_rect,rect_end)
        print("Scorpio, water, planting leaves!")

    if(mr >= 6.0) and (mr < 17.9):
        rect_start = 6.0
        rect_end   = 17.9
        print("Length of this planting opportunity!")
        more_days(rect_start,moon_rect,rect_end)

    if(mr < 24.0) and (mr > 18.0):   # calculate harvesting times
        harvest_days(moon_rect)  
    if(mr < 6.0) and (mr > 0.0):
        harvest_days(moon_rect)
    return None


def main2():
    long = 1.0
    lat  = 1.0
    rect = 1.0
    dec  = 1.0
    sun_long = 1.0
    sun_lat  = 0.0
    sun_medel_anomali = 1.0
    sun_rect = 1.0
    sun_dec  = 1.0
    moon_long = 1.0
    moon_lat  = 1.0
    moon_rect = 1.0
    moon_dec  = 1.0
    skott     = 2.0
    yr   = int(1)
    mth  = int(1)
    dd   = int(1)
    hr   = int(1)
    mn   = int(1)
    days = 1.0
    forts = 1               # continue = 1
    while forts != 0:
        yr,mth,dd,hr,mn = antaldagar.inputFunction(yr,mth,dd,hr,mn)
        print("year = ",yr, "month = ",mth, "day = ",dd, "hour = ",hr, " minute = ",mn)
        days, skott = antaldagar.number_of_days(yr,mth,dd,hr,mn)
        print("Number of days =                 ",days, "skott =",skott)
        sun_long, sun_medel_anomali   = sun_position(days)
        #print("Sun_long        = ",sun_long," Sun_medel_anomali = ",sun_medel_anomali)
        
        moon_long, moon_lat = moon_position(days)
        #print("Moon_long       = ",moon_long, " moon_lat           = ",moon_lat)

        sun_rect, sun_dec = to_rect(sun_long,sun_lat)
        print("sun_long = ",sun_long,"sun_lat =",sun_lat)
        print("sun_rect = ",sun_rect,"sun_dec = ",sun_dec)

        moon_rect, moon_dec = to_rect(moon_long,moon_lat)
        print("moon_long = ",moon_long,"moon_lat =",moon_lat)
        print("moon_rect = ",moon_rect,"moon_dec = ",moon_dec)

        sow_calender(yr,mth,dd,hr,mn,moon_rect,skott)

        forts = input("Continue = 1 End = 0               ")
        forts = int(forts)
        if forts == 0:
            break
        print("")
    return(0)
       
main2()       


    
