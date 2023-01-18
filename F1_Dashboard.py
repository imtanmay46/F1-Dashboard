from time import sleep
from PIL import Image
import pywhatkit

seas_2019=['australia','bahrain','china','azerbaijan','spain','monaco','canada','france','austria','great britain','germany','hungary','belgium','italy','singapore','russia','japan','mexico','united states','brazil','abu dhabi']
seas_2020=['austria','styria','hungary','great britain','70th anniversary','spain','belgium','italy','tuscany','russia','eifel','portugal','emilia romagna','turkey','bahrain','sakhir','abu dhabi']
seas_2021=['bahrain','emilia romagna','portugal','spain','monaco','azerbaijan','france','styria','austria','great britain','hungary','belgium','netherlands','italy','russia','turkey','united states','mexico','brazil','qatar','saudi arabia','abu dhabi']

print('\n')
print("Welcome, Formula 1 Enthusiasts!")
print("Here comes the application that many of you were longing for! Now, you can easily access F1 data from previous seasons just at your fingertips 🤩")
print("Excited to get started right? Let's go Racing...")
print('\n')
print('\n')

flag=True

while flag:
    race=str(input("Do you wish to continue Rrracing..... 💨? {(Yes/Y)/(No/N)}:")).lower()
    if race=='no' or race=='n':
        sleep(1)
        print('\n')
        print("We wished that you'll continue, anyways see ya next time 🥹 🌹")
        break
    elif race=='yes' or race=='y':
        season=str(input("Enter the F1 Season: "))
        print('\n')
        if season=='2019':
            print('\n')
            print("Get Info about:->")
            print('\n')
            print('    1. Race Calendar')
            print("    2. Driver's Grid")
            print('    3. Teams')
            print('    4. Race Details')
            print("    5. WDC(World Driver's Championship) Standings")
            print('    6. Constructor Standings')
            print('    7. Race Highlights')
            print('    8. Fastest Laps')
            print('\n')
            choose=str(input("What information would you like to have: ")).lower()
            if choose=='1' or choose=='race calendar':
                print('\n')
                with open('/Users/varul18/Desktop/F1/Season2019/Season_2019_Schedule.txt','r') as f:
                    data=f.read()
                print(data)
            elif choose=='2' or choose=="driver's grid":
                print('\n')
                with open('/Users/varul18/Desktop/F1/Season2019/DriverGrid_Seas2019.txt','r') as f:
                    driveData=f.read()
                print(driveData)
            elif choose=='3' or choose=='teams':
                print('\n')
                with open('/Users/varul18/Desktop/F1/Season2019/Teams_Seas2019.txt','r') as f:
                    teams=f.read()
                print(teams)
            elif choose=='4' or choose=='race details':
                print('\n')
                venue=str(input("Enter the Venue of Grand Prix: ")).lower()
                if venue not in seas_2019:
                    sleep(5)
                    print('\n')
                    print('Sorry! We were unable to process your request!')
                    print('Probably, No race was scheduled at this venue 🐶')
                    print('\n')
                else:
                    try:
                        if venue=='australia':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2019/Australia_Seas2019.png')
                            m1.show()
                        elif venue=='bahrain':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2019/Bahrain_Seas2019.png')
                            m1.show()
                        elif venue=='china':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2019/China_Seas2019.png')
                            m1.show()
                        elif venue=='azerbaijan':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2019/Azerbaijan_Seas2019.png')
                            m1.show()
                        elif venue=='spain':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2019/Spain_Seas2019.png')
                            m1.show()
                        elif venue=='monaco':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2019/Monaco_Seas2019.png')
                            m1.show()
                        elif venue=='canada':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2019/Canada_Seas2019.png')
                            m1.show()
                        elif venue=='france':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2019/France_Seas2019.png')
                            m1.show()
                        elif venue=='austria':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2019/Austria_Seas2019.png')
                            m1.show()
                        elif venue=='great britain':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2019/GreatBritain_Seas2019.png')
                            m1.show()
                        elif venue=='germany':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2019/Germany_Seas2019.png')
                            m1.show()
                        elif venue=='hungary':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2019/Hungary_Seas2019.png')
                            m1.show()
                        elif venue=='belgium':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2019/Belgium_Seas2019.png')
                            m1.show()
                        elif venue=='italy':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2019/Italy_Seas2019.png')
                            m1.show()
                        elif venue=='singapore':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2019/Singapore_Seas2019.png')
                            m1.show()
                        elif venue=='russia':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2019/Russia_Seas2019.png')
                            m1.show()
                        elif venue=='japan':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2019/Japan_Seas2019.png')
                            m1.show()
                        elif venue=='mexico':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2019/Mexico_Seas2019.png')
                            m1.show()
                        elif venue=='united states':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2019/UnitedStates_Seas2019.png')
                            m1.show()
                        elif venue=='brazil':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2019/Brazil_Seas2019.png')
                            m1.show()
                        elif venue=='abu dhabi':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2019/AbuDhabi_Seas2019.png')
                            m1.show()
                    except Exception:
                        sleep(5)
                        print('\n')
                        print("Oops! Race results went racing, we couldn't fetch 'em! Please try again later!!")
                        print('\n')
            elif choose=='5' or choose=='wdc standings' or choose=='driver standings':
                try:
                    wdc=Image.open(r'/Users/varul18/Desktop/F1/Season2019/WDCStandings_Seas2019.png')
                    wdc.show()
                except Exception:
                    sleep(5)
                    print('\n')
                    print("Sorry! We were unable to process your request 🐶")
                    print("Please try again later!!")
                    print('\n')
            elif choose=='6' or choose=='constructor standings':
                try:
                    const=Image.open(r'/Users/varul18/Desktop/F1/Season2019/ConstructorStandings_Seas2019.png')
                    const.show()
                except Exception:
                    sleep(5)
                    print('\n')
                    print("Sorry! We were unable to process your request 🐶")
                    print("Please try again later!!")
                    print('\n')
            elif choose=='7' or choose=='race highlights' or choose=='highlights' or choose=='race hghts':
                print('\n')
                venue=str(input("Enter the Venue of Grand Prix: ")).lower()
                if venue not in seas_2019:
                    sleep(5)
                    print('\n')
                    print('Sorry! We were unable to process your request!')
                    print('Probably, No race was scheduled at this venue 🐶')
                    print('\n')
                else:
                    try:
                        if venue=='australia':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/NdD8gEGj0to")
                            print("Here you go, F1 2019 Australian Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='bahrain':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/0VjWY--QdMA")
                            print("Here you go, F1 2019 Bahrain Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='china':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/zKfmiAYiC-M")
                            print("Here you go, F1 2019 Chinese Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='azerbaijan':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/8eE9bofwhhs")
                            print("Here you go, F1 2019 Azerbaijan Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='spain':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/xsWaxYlCbac")
                            print("Here you go, F1 2019 Spanish Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='monaco':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/wYUuF--OQs0")
                            print("Here you go, F1 2019 Monaco Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='canada':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/AACbmSCrXbI")
                            print("Here you go, F1 2019 Canadian Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='france':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/THK2lYEusLo")
                            print("Here you go, F1 2019 French Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='austria':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/Q3L7WzpAsjY")
                            print("Here you go, F1 2019 Austrian Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='great britain':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/TjiCXhGuLgw")
                            print("Here you go, F1 2019 British Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='germany':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/RYHQmBULhLc")
                            print("Here you go, F1 2019 German Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='hungary':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/jnz-lc9LYgo")
                            print("Here you go, F1 2019 Hungarian Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='belgium':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/7sIkMy-17hY")
                            print("Here you go, F1 2019 Belgian Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='italy':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/h-ce3gPMsGc")
                            print("Here you go, F1 2019 Italian Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='singapore':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/VhPw8gtfgv4")
                            print("Here you go, F1 2019 Singapore Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='russia':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/47Pn2bII_sg")
                            print("Here you go, F1 2019 Russian Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='japan':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/b0G4-Vp2TS0")
                            print("Here you go, F1 2019 Japanese Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='mexico':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/tzE4y1n08IA")
                            print("Here you go, F1 2019 Mexican Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='united states':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/QLx2WZWilBc")
                            print("Here you go, F1 2019 United States Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='brazil':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/3WZeoOkMf0Y")
                            print("Here you go, F1 2019 Brazilian Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='abu dhabi':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/VdDH0SzlVd4")
                            print("Here you go, F1 2019 Abu Dhabi Grand Prix Highlights 💨💨")
                            print('\n')
                    except Exception:
                        sleep(5)
                        print('\n')
                        print("Oops! Race results went racing, we couldn't fetch 'em! Please try again later!!")
                        print('\n')
            elif choose=='8' or choose=='fastest laps' or choose=='laps of the year':
                print('\n')
                try:
                    fastestLaps=Image.open(r'/Users/varul18/Desktop/F1/Season2019/FastestLaps_Seas2019.png')
                    fastestLaps.show()
                except Exception:
                    sleep(5)
                    print('\n')
                    print("Sorry! We were unable to process your request 🐶")
                    print("Please try again later!!")
                    print('\n')
            else:
                sleep(5)
                print('\n')
                print("Sorry! We were unable to process your request 🐶")
                print("Please try again later!!")
                print('\n')
        elif season=='2020':
            print('\n')
            print("Get Info about:->")
            print('\n')
            print('    1. Race Calendar')
            print("    2. Driver's Grid")
            print('    3. Teams')
            print('    4. Race Details')
            print("    5. WDC(World Driver's Championship) Standings")
            print('    6. Constructor Standings')
            print('    7. Race Highlights')
            print('    8. Fastest Laps')
            print('\n')
            choose=str(input("What information would you like to have: ")).lower()
            if choose=='1' or choose=='race calendar':
                print('\n')
                with open('/Users/varul18/Desktop/F1/Season2020/Season_2020_Schedule.txt','r') as f:
                    data=f.read()
                print(data)
            elif choose=='2' or choose=="driver's grid":
                print('\n')
                with open('/Users/varul18/Desktop/F1/Season2020/DriverGrid_Seas2020.txt','r') as f:
                    driveData=f.read()
                print(driveData)
            elif choose=='3' or choose=='teams':
                print('\n')
                with open('/Users/varul18/Desktop/F1/Season2020/Teams_Seas2020.txt','r') as f:
                    teams=f.read()
                print(teams)
            elif choose=='4' or choose=='race details':
                print('\n')
                venue=str(input("Enter the Venue of Grand Prix: ")).lower()
                if venue not in seas_2020:
                    sleep(5)
                    print('\n')
                    print('Sorry! We were unable to process your request!')
                    print('Probably, No race was scheduled at this venue 🐶')
                    print('\n')
                else:
                    try:
                        if venue=='austria':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2020/Austria_Seas2020.png')
                            m1.show()
                        elif venue=='styria':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2020/Styria_Seas2020.png')
                            m1.show()
                        elif venue=='hungary':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2020/Hungary_Seas2020.png')
                            m1.show()
                        elif venue=='great britain':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2020/GreatBritain_Seas2020.png')
                            m1.show()
                        elif venue=='70th anniversary':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2020/70ThAnniversary_Seas2020.png')
                            m1.show()
                        elif venue=='spain':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2020/Spain_Seas2020.png')
                            m1.show()
                        elif venue=='belgium':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2020/Belgium_Seas2020.png')
                            m1.show()
                        elif venue=='italy':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2020/Italy_Seas2020.png')
                            m1.show()
                        elif venue=='tuscany':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2020/Tuscany_Seas2020.png')
                            m1.show()
                        elif venue=='russia':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2020/Russia_Seas2020.png')
                            m1.show()
                        elif venue=='eifel':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2020/Eifel_Seas2020.png')
                            m1.show()
                        elif venue=='portugal':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2020/Portugal_Seas2020.png')
                            m1.show()
                        elif venue=='emilia romagna':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2020/EmiliaRomagna_Seas2020.png')
                            m1.show()
                        elif venue=='turkey':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2020/Turkey_Seas2020.png')
                            m1.show()
                        elif venue=='bahrain':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2020/Bahrain_Seas2020.png')
                            m1.show()
                        elif venue=='sakhir':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2020/Sakhir_Seas2020.png')
                            m1.show()
                        elif venue=='abu dhabi':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2020/AbuDhabi_Seas2020.png')
                            m1.show()
                    except Exception:
                        sleep(5)
                        print('\n')
                        print("Oops! Race results went racing, we couldn't fetch 'em! Please try again later!!")
                        print('\n')
            elif choose=='5' or choose=='wdc standings' or choose=='driver standings':
                try:
                    wdc=Image.open(r'/Users/varul18/Desktop/F1/Season2020/WDCStandings_Seas2020.png')
                    wdc.show()
                except Exception:
                    sleep(5)
                    print('\n')
                    print("Sorry! We were unable to process your request 🐶")
                    print("Please try again later!!")
                    print('\n')
            elif choose=='6' or choose=='constructor standings':
                try:
                    const=Image.open(r'/Users/varul18/Desktop/F1/Season2020/ConstructorStandings_Seas2020.png')
                    const.show()
                except Exception:
                    sleep(5)
                    print('\n')
                    print("Sorry! We were unable to process your request 🐶")
                    print("Please try again later!!")
                    print('\n')
            elif choose=='7' or choose=='race highlights' or choose=='highlights' or choose=='race hghts':
                print('\n')
                venue=str(input("Enter the Venue of Grand Prix: ")).lower()
                if venue not in seas_2020:
                    sleep(5)
                    print('\n')
                    print('Sorry! We were unable to process your request!')
                    print('Probably, No race was scheduled at this venue 🐶')
                    print('\n')
                else:
                    try:
                        if venue=='austria':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/1Q470aUwi3E")
                            print("Here you go, F1 2020 Austrian Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='styria':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/IEB3jc22izI")
                            print("Here you go, F1 2020 Styrian Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='hungary':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/8KhJUWlNnCk")
                            print("Here you go, F1 2020 Hungarian Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='great britain':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/HmEsqWosuS8")
                            print("Here you go, F1 2020 British Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='70th anniversary':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/ffonCbGgzt0")
                            print("Here you go, F1 2020 70th Anniversary Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='spain':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/-yHbZWfkBwU")
                            print("Here you go, F1 2020 Spanish Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='belgium':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/xOy63dhQmUg")
                            print("Here you go, F1 2020 Belgian Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='italy':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/TB5yhZdF8SI")
                            print("Here you go, F1 2020 Italian Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='tuscany':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/R-Yq1AlIwsc")
                            print("Here you go, F1 2020 Tuscan Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='russia':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/EmZtTd1YRmA")
                            print("Here you go, F1 2020 Russian Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='eifel':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/2femix89pTE")
                            print("Here you go, F1 2020 Eifel Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='portugal':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/nQ8du5ysxTI")
                            print("Here you go, F1 2020 Portuguese Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='emilia romagna':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/RL1oFTz-NvA")
                            print("Here you go, F1 2020 Emilia Romagna Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='turkey':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/bg3v8VKEtBc")
                            print("Here you go, F1 2020 Turkish Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='bahrain':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/HnfHMC02Mj4")
                            print("Here you go, F1 2020 Bahrain Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='sakhir':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/H0zwR2drgV4")
                            print("Here you go, F1 2020 Sakhir Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='abu dhabi':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/a92evkEC0qo")
                            print("Here you go, F1 2020 Abu Dhabi Grand Prix Highlights 💨💨")
                            print('\n')
                    except Exception:
                        sleep(5)
                        print('\n')
                        print("Oops! Race results went racing, we couldn't fetch 'em! Please try again later!!")
                        print('\n')
            elif choose=='8' or choose=='fastest laps' or choose=='laps of the year':
                print('\n')
                try:
                    fastestLaps=Image.open(r'/Users/varul18/Desktop/F1/Season2020/FastestLaps_Seas2020.png')
                    fastestLaps.show()
                except Exception:
                    sleep(5)
                    print('\n')
                    print("Sorry! We were unable to process your request 🐶")
                    print("Please try again later!!")
                    print('\n')
            else:
                sleep(5)
                print('\n')
                print("Sorry! We were unable to process your request 🐶")
                print("Please try again later!!")
                print('\n')
        elif season=='2021':
            print('\n')
            print("Get Info about:->")
            print('\n')
            print('    1. Race Calendar')
            print("    2. Driver's Grid")
            print('    3. Teams')
            print('    4. Race Details')
            print("    5. WDC(World Driver's Championship) Standings")
            print('    6. Constructor Standings')
            print('    7. Race Highlights')
            print('    8. Fastest Laps')
            print('\n')
            choose=str(input("What information would you like to have: ")).lower()
            if choose=='1' or choose=='race calendar':
                print('\n')
                with open('/Users/varul18/Desktop/F1/Season2021/Season_2021_Schedule.txt','r') as f:
                    data=f.read()
                print(data)
            elif choose=='2' or choose=="driver's grid":
                print('\n')
                with open('/Users/varul18/Desktop/F1/Season2021/DriverGrid_Seas2021.txt','r') as f:
                    driveData=f.read()
                print(driveData)
            elif choose=='3' or choose=='teams':
                print('\n')
                with open('/Users/varul18/Desktop/F1/Season2021/Teams_Seas2021.txt','r') as f:
                    teams=f.read()
                print(teams)
            elif choose=='4' or choose=='race details':
                print('\n')
                venue=str(input("Enter the Venue of Grand Prix: ")).lower()
                if venue not in seas_2021:
                    sleep(5)
                    print('\n')
                    print('Sorry! We were unable to process your request!')
                    print('Probably, No race was scheduled at this venue 🐶')
                    print('\n')
                else:
                    try:
                        if venue=='bahrain':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2021/Bahrain_Seas2021.png')
                            m1.show()
                        elif venue=='emilia romagna':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2021/EmiliaRomagna_Seas2021.png')
                            m1.show()
                        elif venue=='portugal':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2021/Portugal_Seas2021.png')
                            m1.show()
                        elif venue=='spain':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2021/Spain_Seas2021.png')
                            m1.show()
                        elif venue=='monaco':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2021/Monaco_Seas2021.png')
                            m1.show()
                        elif venue=='azerbaijan':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2021/Azerbaijan_Seas2021.png')
                            m1.show()
                        elif venue=='france':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2021/France_Seas2021.png')
                            m1.show()
                        elif venue=='styria':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2021/Styria_Seas2021.png')
                            m1.show()
                        elif venue=='austria':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2021/Austria_Seas2021.png')
                            m1.show()
                        elif venue=='great britain':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2021/GreatBritain_Seas2021.png')
                            m1.show()
                        elif venue=='hungary':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2021/Hungary_Seas2021.png')
                            m1.show()
                        elif venue=='belgium':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2021/Belgium_Seas2021.png')
                            m1.show()
                        elif venue=='netherlands':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2021/Netherlands_Seas2021.png')
                            m1.show()
                        elif venue=='italy':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2021/Italy_Seas2021.png')
                            m1.show()
                        elif venue=='russia':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2021/Russia_Seas2021.png')
                            m1.show()
                        elif venue=='turkey':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2021/Turkey_Seas2021.png')
                            m1.show()
                        elif venue=='united states':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2021/UnitedStates_Seas2021.png')
                            m1.show()
                        elif venue=='mexico':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2021/Mexico_Seas2021.png')
                            m1.show()
                        elif venue=='brazil':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2021/Brazil_Seas2021.png')
                            m1.show()
                        elif venue=='qatar':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2021/Qatar_Seas2021.png')
                            m1.show()
                        elif venue=='saudi arabia':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2021/SaudiArabia_Seas2021.png')
                            m1.show()
                        elif venue=='abu dhabi':
                            m1=Image.open(r'/Users/varul18/Desktop/F1/Season2021/AbuDhabi_Seas2021.png')
                            m1.show()
                    except Exception:
                        sleep(5)
                        print('\n')
                        print("Oops! Race results went racing, we couldn't fetch 'em! Please try again later!!")
                        print('\n')
            elif choose=='5' or choose=='wdc standings' or choose=='driver standings':
                try:
                    wdc=Image.open(r'/Users/varul18/Desktop/F1/Season2021/WDCStandings_Seas2021.png')
                    wdc.show()
                except Exception:
                    sleep(5)
                    print('\n')
                    print("Sorry! We were unable to process your request 🐶")
                    print("Please try again later!!")
                    print('\n')
            elif choose=='6' or choose=='constructor standings':
                try:
                    const=Image.open(r'/Users/varul18/Desktop/F1/Season2021/ConstructorStandings_Seas2021.png')
                    const.show()
                except Exception:
                    sleep(5)
                    print('\n')
                    print("Sorry! We were unable to process your request 🐶")
                    print("Please try again later!!")
                    print('\n')
            elif choose=='7' or choose=='race highlights' or choose=='highlights' or choose=='race hghts':
                print('\n')
                venue=str(input("Enter the Venue of Grand Prix: ")).lower()
                if venue not in seas_2021:
                    sleep(5)
                    print('\n')
                    print('Sorry! We were unable to process your request!')
                    print('Probably, No race was scheduled at this venue 🐶')
                    print('\n')
                else:
                    try:
                        if venue=='bahrain':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/QuBlV0dixMo")
                            print("Here you go, F1 2021 Bahrain Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='emilia romagna':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/ds0BC8RDJ5o")
                            print("Here you go, F1 2021 Emilia Romagna Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='portugal':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/-9-8gvYantk")
                            print("Here you go, F1 2021 Portuguese Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='spain':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/HuLdJLB6sBo")
                            print("Here you go, F1 2021 Spanish Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='monaco':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/GK5qm8AZ1dQ")
                            print("Here you go, F1 2021 Monaco Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='azerbaijan':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/suZHkUxPzjE")
                            print("Here you go, F1 2021 Azerbaijan Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='france':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/5hBwgJtMxLM")
                            print("Here you go, F1 2021 French Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='styria':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/tr4gf_iae20")
                            print("Here you go, F1 2021 Styrian Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='austria':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/LxLVqf5OtIE")
                            print("Here you go, F1 2021 Austrian Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='great britain':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/FRt8hXFb0Vg")
                            print("Here you go, F1 2021 British Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='hungary':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/a2kkuQS_gXk")
                            print("Here you go, F1 2021 Hungarian Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='belgium':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/MjmywbEfzk0")
                            print("Here you go, F1 2021 Belgian Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='netherlands':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/rXhGajRFLlY")
                            print("Here you go, F1 2021 Dutch Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='italy':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/1ZgniFQiTPA")
                            print("Here you go, F1 2021 Italian Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='russia':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/Jjw1x6xQo7s")
                            print("Here you go, F1 2021 Russian Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='turkey':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/ZGRpHy0qoN4")
                            print("Here you go, F1 2021 Turkish Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='united states':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/-Ee08uFurok")
                            print("Here you go, F1 2021 United States Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='mexico':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/2yYtH0HAL-U")
                            print("Here you go, F1 2021 Mexico City Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='brazil':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/icesjjvN6Sc")
                            print("Here you go, F1 2021 Brazilian Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='qatar':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/CZy-NZF8mEA")
                            print("Here you go, F1 2021 Qatar Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='saudi arabia':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/vRhhS6BnLSY")
                            print("Here you go, F1 2021 Saudi Arabian Grand Prix Highlights 💨💨")
                            print('\n')
                        elif venue=='abu dhabi':
                            print('\n')
                            pywhatkit.playonyt("https://youtu.be/7QJ-N-AQJYc")
                            print("Here you go, F1 2021 Abu Dhabi Grand Prix Highlights 💨💨")
                            print('\n')
                    except Exception:
                        sleep(5)
                        print('\n')
                        print("Oops! Race results went racing, we couldn't fetch 'em! Please try again later!!")
                        print('\n')
            elif choose=='8' or choose=='fastest laps' or choose=='laps of the year':
                print('\n')
                try:
                    fastestLaps=Image.open(r'/Users/varul18/Desktop/F1/Season2021/FastestLaps_Seas2021.png')
                    fastestLaps.show()
                except Exception:
                    sleep(5)
                    print('\n')
                    print("Sorry! We were unable to process your request 🐶")
                    print("Please try again later!!")
                    print('\n')
        else:
            sleep(5)
            print('\n')
            print('Sorry! We were unable to process your request on this season 🐶')
            print("Please try again later!!")
            print('\n')
    else:
        sleep(1)
        print('\n')
        print("There are better ways to say Goodbye 🫠")
        print('\n')
        break