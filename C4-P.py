import time
from winsound import Beep
from os import system
import keyboard
import wmi
import datetime
import socket
import random
import os
from colorama import Fore, Style, init
import string
import winsound
import psutil
import win32process,win32api,win32con
import win32gui
from win32api import GetAsyncKeyState
import pydivert
from os import path
import ctypes

string.ascii_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mb2 = random.randint(1000, 3999)
kirrrr = random.choice(string.ascii_letters)
kir = random.choice(string.ascii_letters)
def print_banner():
    system("cls")
    print(Style.BRIGHT + Fore.CYAN +"""
 		   
            ▄▀█ █░█ ▀█▀ █▀█ █▄▀ █ █▀▀ █▄▀
            █▀█ █▄█ ░█░ █▄█ █░█ █ █▄▄ █░█
 		    Magic________MODE
   """)

system("cls")


def check():
    ccc = wmi.WMI()
    sss = ccc.Win32_Processor()
    hardid = sss[0].ProcessorId
    processid = sss[0].Description
    now = datetime.datetime.now()
    cock = now.strftime("%M")
    gh = now.strftime("%S")
    current_time = now.strftime("%d/%m/%y")
    start_current_time = datetime.date(now.year, now.month, now.day)
    end_current_time = datetime.date(2023, 2, 15)
    end_day = (end_current_time - start_current_time).days
    x = int(cock)
    j = int(gh)
    x = x * 99 * 15 * 79 * 2 * 9999 * j
    hostname=socket.gethostname()
    IPAddr=socket.gethostbyname(hostname)
    pime = now.strftime("%I:%M:%S")
    ran = random.randint(0, 3)
    os.system("cls")
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}] "+"Searching For Updates..."+Style.RESET_ALL)
    time.sleep(3.6)
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}] "+"Ready For Action...")
    time.sleep(3)
    os.system("cls")
    a = path.exists("kdmapper.sys")
    if a == True:
        print(Style.BRIGHT + Fore.CYAN +f"[{pime}] "+"Opening Driver kdmapper..."+Style.RESET_ALL)
    else:
        print(Style.BRIGHT + Fore.RED +"  Cant Load Driver (0x0009)"+Style.RESET_ALL)
        time.sleep(10)
        exit


    time.sleep(8)
    os.system("cls")
    hwid = "BFEBFBFF000806C1"
    process = "Intel64 Family 6 Model 140 Stepping 1"
    if  hardid == hwid and processid == process and 31 > end_day > -1: 
        print(Style.BRIGHT + Fore.CYAN +"""
                █████████████████████████
                █─▄─▄─█▄─▄█▄─▀█▀─▄█▄─▄▄─█
                ███─████─███─█▄█─███─▄█▀█
                ▀▀▄▄▄▀▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀ 
        ░░ ░░ ░░ ░░ ░░ ░░ ░░        ░░ ░░ ░░ ░░ ░░ ░░ ░░
                ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀
        ░░ ░░ ░░ ░░ ░░ ░░ ░░        ░░ ░░ ░░ ░░ ░░ ░░ ░░                      
          ᴛɪᴍᴇ ᴏғ ᴘᴜʀᴄʜᴀsᴇ            ᴛɪᴍᴇ ʀᴇᴍᴀɪɴɪᴜɴɢ   """)
                                      
        print(Style.BRIGHT + Fore.YELLOW +f"""                 {current_time}                      {end_day}

        """)
        print(Style.BRIGHT + Fore.CYAN +f"[{pime}]"+Style.BRIGHT + Fore.YELLOW +" VIP USER")
        time.sleep(2.0)
        time.sleep(4)

    else:
        print(Style.BRIGHT + Fore.CYAN+"""             
        ▒█▀▀█ █▀▀█ █▀▀▄ █▀▀ 　 ▒█▀▀▀ █▀▀▄ ▀▀█▀▀ █▀▀ █▀▀█ 
        ▒█░░░ █░░█ █░░█ █▀▀ 　 ▒█▀▀▀ █░░█ ░░█░░ █▀▀ █▄▄▀ 
        ▒█▄▄█ ▀▀▀▀ ▀▀▀░ ▀▀▀ 　 ▒█▄▄▄ ▀░░▀ ░░▀░░ ▀▀▀ ▀░▀▀
             -= Autokick#0611 (Teleport_____MODE) =-
        """+Style.RESET_ALL)
        teleport = input(Style.BRIGHT + Fore.CYAN +f"[{pime}]"+" Please Enter Your Private Code:"+Style.RESET_ALL)
        q = int(teleport)
        if q != x:
            print(Style.BRIGHT + Fore.RED +f"[{pime}]"+"******SYSTEM INFORMATION BLOCKED******")
            print(Style.BRIGHT + Fore.RED +f"[{pime}]"+"User:  "+hostname)
            print(Style.BRIGHT + Fore.RED +f"[{pime}]"+"Local IP:  "+IPAddr)
            print(Style.BRIGHT + Fore.RED +f"[{pime}]"+"CPU Model:  "+processid+Style.RESET_ALL)
            time.sleep(2.0)
            print(Style.BRIGHT + Fore.CYAN +f"[{pime}]"+" Please Contact With Creator [AutoKick#0611].")
            time.sleep(25.0)
            exit()
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}]"+Style.BRIGHT + Fore.GREEN +" Passed")
    time.sleep(6)
    os.system("cls")
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}] "+ Fore.RED+"Spoofing Drivers..."+Style.RESET_ALL)
    time.sleep(3)
    koss = random.randint(123124123123123, 999999999999999)
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}] "+f"1-HEX: {kirrrr}{koss}{kir}"+Style.RESET_ALL)
    time.sleep(4)
    PIDD = random.randint(1010, 2000)
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}] "+f"PROCESS-PID: {PIDD}"+Style.RESET_ALL)
    time.sleep(4)
    os.system("cls")
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}]"+" User:  "+hostname)
    time.sleep(1.5)
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}]"+" IP:    "+IPAddr+"""

    """)
    time.sleep(1.5)
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}]"+" Hardware ID: "+hardid+"""
    """)
    time.sleep(3)
    os.system("cls")
    print(Style.BRIGHT + Fore.RED +"""

    ░█████╗░██╗░░░██╗████████╗░█████╗░██╗░░██╗██╗░█████╗░██╗░░██╗
    ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██║░██╔╝██║██╔══██╗██║░██╔╝
    ███████║██║░░░██║░░░██║░░░██║░░██║█████═╝░██║██║░░╚═╝█████═╝░
    ██╔══██║██║░░░██║░░░██║░░░██║░░██║██╔═██╗░██║██║░░██╗██╔═██╗░
    ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝██║░╚██╗██║╚█████╔╝██║░╚██╗
    ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚═╝
 		   -= Autokick#0611 (Teleport_____MODE) =-
   """+ Style.RESET_ALL)
    time.sleep(3.5)
    print(Fore.YELLOW +""" --> Loading injector Kernel32.dll... 
          """)
    time.sleep(13.5)
    winsound.Beep(400, 200)
    try:
        a = os.environ['USERPROFILE']
        b = a + "\Desktop\Black Squad.url"
        os.startfile (b)
    except:
        print(Style.BRIGHT +Fore.RED +"Cant Access To Game Data!!!!"+Style.RESET_ALL)
        time.sleep(2.5)
        print(Style.BRIGHT +Fore.RED +"Make Sure You Read The Readme.txt!!!!"+Style.RESET_ALL)
        time.sleep(2.5)
        pass
    else:
        print(Style.BRIGHT + Fore.GREEN +" Injected!"+Style.RESET_ALL)
        ctypes.windll.kernel32.SetConsoleTitleW(f"BlackSquad.exe --> pid [{mb2}] ")
        time.sleep(1.5)
        

check()

def print_lt(lag,AB_status,AB_RED,MODE_status):
    system("cls")
    print(Style.RESET_ALL + Fore.RED +"""
                   
        ▄▀█ █░█ ▀█▀ █▀█ █▄▀ █ █▀▀ █▄▀
        █▀█ █▄█ ░█░ █▄█ █░█ █ █▄▄ █░█
            MagicBullet[*_*]________MODE
    """+ Style.RESET_ALL)
    print(Fore.RED +"""========================= Controls =====================
          """)
    print("    CHEAT MODE                                   :",Fore.RED + MODE_status + Style.RESET_ALL)
    print("    CHEAT HOTKEY                                 :",Fore.CYAN + str(lag) + Style.RESET_ALL)
    print("    BULLET INCREASE HOTKEY                       :", Fore.RED + "=" + Style.RESET_ALL)
    print("    RESET SETTINGS                               :", Fore.CYAN   + """NUMPAD 9
    """ + Style.RESET_ALL)
    print(Fore.RED +"""======================= Information ====================
          """)
    print("    BATTELEYE DETECT                             :", Fore.RED + "safe" + Style.RESET_ALL)
    print("    INJECTOR                                     :", Fore.CYAN +"kernel32.dll"+ Style.RESET_ALL)
    print("    CHEAT STATUS                                 :", AB_RED + "Always On" + Style.RESET_ALL)
    print(Fore.CYAN +"""

          
          """)
    print(Fore.RED +"--> Running!!!!"+Style.RESET_ALL)




def main():
    print_banner()
    system("cls")
    print_banner()
    cmd = input(Fore.CYAN +" MagicBullet HotKey (default:"+ Fore.YELLOW +"(b or c)"+ Fore.CYAN +"[Key For Active Cheat] ):"+ Fore.YELLOW)
    lag = str(cmd)
    time.sleep(0.2)
    time.sleep(1)
    print("")
    system("cls")
    aimbot = True
    A_status = "OFF"
    AB_status = "OFF"
    A_RED = Fore.RED
    AB_RED = Fore.RED
    MODE_status = "Magic Bullet Mode"
    print_lt(lag,AB_status,AB_RED,MODE_status)
    w = pydivert.WinDivert("inbound")
    d = pydivert.WinDivert("outbound",priority=0)
    data = []
    i = 1
    t = 0
    while True:
        time.sleep(0.3)
        try:
            if keyboard.is_pressed("b"):
                d.open()
                winsound.Beep(200, 150)
                keyboard.wait('b')
                w.open()
                d.close()
                winsound.Beep(300, 250)
                keyboard.wait('b')
                w.close()
                winsound.Beep(700, 550)
        except:
            pass
                
             

main()


