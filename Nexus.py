import time
import configparser
import os
import sqlite3
from Placeholders import file_path,Referral, auto_update, NetworkError,CN,Version
from Placeholders import UUID
from Placeholders import NexusPB
from Placeholders import check_os
from Main import SelectMenu
from urllib import request


class system_loading:
    def load(self):
        print("Nex 4.01")
            print("Nexus > System successfully loaded | Running ... ")
            os.system('cls' if os.name == 'nt' else 'clear')
            SelectMenu().MainMenu()

    def check_update(self):
        try:
            print("[#] Nexus > Checking for Updates ...")
            time.sleep(4)
            send_request = request.urlopen(auto_update)
            read_request = str(send_request.read(), 'utf-8').split("\n")

            if Version == read_request[0]:
                os.system('cls' if os.name == 'nt' else 'clear')
                UID = config.get('Information', 'UUID')
                print(f"[#] No updates found. System is Running v{Version}")
                print(f"[#] Session UUID: {UUID}")
                print(f"[*] System UUID: {UID}")
                time.sleep(3)
                system_loading().load()

            elif Version != read_request[0]:
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"Running: [{Version}] | Update Available: [{read_request[0]}]")
                    print("[!] Update Found | Get the update below.")
                    print("[#] https://github.com/DJNovaTech/Nexus-Phone-bot")
                    user = input("\nWould you like to start without updating?\n[Y] - Start System\n[N] - Update\n> ").lower()
                    if user == 'y':
                        print("Nexus > System starting ...")
                        system_loading().load()
                    elif user == 'n':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        system_loading().check_update()
                    else:
                        print("Nexus > Not and Option")

                os.system('cls' if 'nt' == os.name else 'clear')
                print(f"Nexus > System version Modified ? | {Version}")
                print("[!] System version did not meet requirements !")
                print("[!] Please Re-download Nexus from the link below.")
                print("[#] https://github.com/DJNovaTech/Nexus-Phone-bot")
        except Exception as e:
            if str(e) in NetworkError:
                print("\n")
                print("        ([X] WARNING [X] | No Internet connection)")
                print("Your System is not connected to internet | Please connect now")
                print("            To use the full system.")
            else:
                print(e)

class create:
    def files(file):
        print("Please wait creating files")
        if file == 'config.ini':
            try:
                print(file + "INSIDE OF CONFIG RUN")
                print("Note - This Program requires a Twilio Account !")
                print("Create one here | " + Referral)
                conf = configparser.ConfigParser()
                num = ''
                num = CN(num)
                Account_SID = input("Enter Twilio SID: ")
                Auth_Token = input("Enter Twilio Auth Token: ")
                Voice_Link = input("Enter a Voice Link: ")
                Music_Link = input("Enter a Music Link: ")

                conf['Information'] = {
                    'UUID': UUID,
                    'System-OS': check_os, }
                conf['Settings'] = {
                    'Bot-Number': "+1" + str(num),
                    'Account-SID': Account_SID,
                    'Auth-Token': Auth_Token,
                    'Simple-Mode': 'False',
                    'Lock-Mode': 'False',
                    'Auto-Update': 'False',
                    'Database': 'False',
                    'Local-Database': 'True',
                    'Log-Path': 'C:/NovaOS/Modules/NexusPhoneBot/Logs',
                    'Voice-Link': Voice_Link,
                    'Music-Link': Music_Link, }
                conf['Database'] = {
                    'db-Host': 'LocalHost',
                    'db-Port': 80,
                    'db-Fallback-Port': 89,
                    'db-Username': 'NovaOS',
                    'db-Password': 'Password1234'}
                with open(file_path[1], 'w') as configfile:
                    conf.write(configfile)
                    print("Config File has been created.")
            except IOError as e:
                print(e)
        elif file == 'System.db':
            try:
                connect = sqlite3.connect(file_path[2])
                disconnect = connect.cursor()

                with sqlite3.connect(file_path[2]) as db:
                    cursor = db.cursor()
                    cursor.execute('\n'
                                   'CREATE TABLE IF NOT EXISTS User(\n'
                                   'UUID PRIMARY KEY,\n'
                                   'Username VARCHAR(20) NOT NULL,\n'
                                   'Password VARCHAR(20) NOT NULL,\n'
                                   'Admin TEXT (1) NOT NULL ,\n'
                                   'Pin INTEGER (6) NOT NULL);\n''')
                    disconnect.close()
                print("System Database created !!")
            except sqlite3.Error:
                print("Error")

class files:
    def checkFiles(file_path):
        try:
            if os.path.exists(file_path):
                print(f"[#] File Has been found |  {file_path}")
            elif 'config.ini' == os.path.split(file_path)[1]:
                print("Nexus > Creating Files | Config File")
                file = os.path.split(file_path)[1]
                create.files(file)

            elif 'System.db' == os.path.split(file_path)[1]:
                print("Nexus > Creating Files | System Database")
                file = os.path.split(file_path)[1]
                create.files(file)
            else:
                os.makedirs(file_path)
                print(f"Nexus > File Created | {file_path}")
        except IOError as e:
            print(e)



if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read("C:/NovaOS/Modules/NexusPhoneBot/config.ini")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(NexusPB)
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[#] Nexus > System is initializing ..")
    time.sleep(4)
    for i in range(0,3):
        files.checkFiles(file_path[i])
        i+=1
    print("\nNexus > All files found !")
    system_loading().check_update()
