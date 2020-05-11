import time
import configparser
import os
import sqlite3
from Placeholders import system_path
from Placeholders import file_path, conf_path, database_path, database_file_path, img_path, Referral, auto_update, NetworkError
from Placeholders import UUID
from Placeholders import NexusPB
from Placeholders import check_os
from ForceLogin import FLogin
from Main import SelectMenu
from urllib import request


class system_loading:
    def load(self, conf_version, sys_version, UUID, Force_Login):
        """This will load into the system Admin area. If this is a new system,
           You will be able to add Admin accounts as well create new POS login's.
           Otherwise it will load into the normal Log screen."""
        if Force_Login == 'True':
            l = FLogin()
            l.login()
        elif bool(Simple_Mode) == 'True':
            print(Simple_Mode)
            print("Simple Mode Enabled")
            time.sleep(5)
        elif bool(Lock_Mode) == 'True':
            print(Lock_Mode)
            print("Lock Mode Enabled")
            # Start Code for Lock Mode
        else:
            print("System has started ")
            os.system('cls')
            SelectMenu().MainMenu()
            # start the system

    def check_update(self, conf_version, sys_version):
        """This Will connect to NovaOS Git and check for system updates
        if No updates are found system will start to load. if an
        update is found it will direct you to the site"""
        try:
            """Connects to Web Server than grabs newest version of system
               if found the system will prompt user to update. You will
               Not be able to use the system without updating."""

            print("[#] Checking for Updates ...")
            time.sleep(2)
            send_request = request.urlopen(auto_update)
            read_request = str(send_request.read(), 'utf-8').split("\n")
            if read_request[0] == '3.0':
                os.system('cls')
                print(f"[#] No updates found. System is Running v{sys_version}")
                print(f"[*] UUID: {UUID}")
                time.sleep(3)
                system_loading().load(conf_version, sys_version, str(UUID), Force_Login)
            else:
                os.system('cls')
                print(f"Running: [{sys_version}] | Update Available: [{read_request[0]}]")
                print("[!] Update Found | Get the update below.")
                print("[#] https://github.com/DJNovaTech/Nexus-Phone-bot")



        except Exception as e:
            if str(e) in NetworkError:
                print("\n")
                print("        ([X] WARNING [X] | No Internet connection)")
                print("Your System is not connected to internet | Please connect now")
                print("            To use the full system.")

    def check_dir(self):
        """This will check for the main dir."""
        try:
            if os.path.exists(file_path):
                print("Nexus > Files Found | Main Root")
            else:
                print("Nexus > Creating Files | Main Root")
                os.makedirs(file_path)
            try:
                if os.path.exists(img_path):
                    print("Nexus > Files Found | Img File")
                else:
                    print("Nexus > Files Missing | Img File")
                    os.makedirs(img_path)
            except Exception as error:
                print(error)

            try:
                if os.path.exists(conf_path):
                    print("Nexus > Files found | Config.ini")
                else:
                    print("Nexus > Files Missing | Config.ini")
                    create().config()
            except Exception as error:
                print(error)

            try:
                if os.path.exists(database_path) and os.path.exists(database_file_path):
                    print("Nexus > Files found | database Root")
                    print("Nexus > Files Found | System.db\n")
                    print("Nexus > All Files Found | Checking for Updates !\n")
                    config = configparser.ConfigParser()
                    config.read(conf_path)
                    sys_version = config.get('Information', 'sys_version')
                    conf_version = config.get('Information', 'conf_version')
                    time.sleep(2)
                    system_loading.check_update(self, conf_version, sys_version)

                elif os.path.exists(database_path) is False:
                    os.makedirs(database_path)
                    create().database()
                elif os.path.exists(database_file_path) is False:
                    create().database()
                else:
                    print("Restarting System | please wait...")

            except Exception as error:
                print(error)

        except Exception as error:
            print(error)


class create:
    @staticmethod
    def config():
        try:
            print("Note - This Program requires a Twilio Account !")
            print("Create one here | " + Referral)
            conf = configparser.ConfigParser()
            Bot_Number = ''
            while Bot_Number is not int:
                try:
                    Bot_Number = int(input('Nova > Bots Number: '))
                    if len(str(Bot_Number)) == 10:
                        print(f"Nexus > Number Accepted | {Bot_Number}")
                        break
                    else:
                        print(f"Nexus > Must be a 10 digit number. | {Bot_Number}")
                except ValueError:
                    print(f'Nexus > Must be a 10 digit number. | {Bot_Number}')

            Account_SID = input("Enter Twilio SID: ")
            Auth_Token = input("Enter Twilio Auth Token: ")
            Voice_Link = input("Enter a Voice Link: ")
            Music_Link = input("Enter a Music Link: ")

            conf['Information'] = {
                'UUID': UUID,
                'sys_version': 3.0,
                'conf_version': 3.0,
                'System_OS': check_os,
            }

            conf['Settings'] = {
                'Bot-Number': "+1" + str(Bot_Number),
                'Account-SID': Account_SID,
                'Auth-Token': Auth_Token,
                'Force-Login': 'False',
                'Simple-Mode': 'False',
                'Lock-Mode': 'False',
                'Auto-Update': 'False',
                'Database': 'False',
                'Local-Database': 'True',
                'Log-Path': 'C:/NovaOS/Modules/NexusPhoneBot/Logs',
                'Voice-Link': Voice_Link,
                'Music-Link': Music_Link,
            }
            conf['Database'] = {
                'db-Host': 'LocalHost',
                'db-Port': 80,
                'db-Fallback-Port': 89,
                'db-Username': 'NovaOS',
                'db-Password': 'Password1234'
            }
            conf['CustomAttacks'] = {
                'Attack-Name': ['Line 1',
                                'Line 2',
                                'Line 3']
            }
            with open(conf_path, 'w') as configfile:
                conf.write(configfile)
            try:
                if system_path[2]:
                    pass
                else:
                    os.makedirs(database_path)
                if system_path[3]:
                    pass
                else:
                    create.database()
            except Exception as error:
                print(error)

        except Exception as error:
            print(error)

    @staticmethod
    def database():
        try:
            connect = sqlite3.connect(database_file_path)
            disconnect = connect.cursor()

            with sqlite3.connect(database_file_path) as db:
                cursor = db.cursor()
                cursor.execute('\n'
                               'CREATE TABLE IF NOT EXISTS User(\n'
                               'UUID PRIMARY KEY,\n'
                               'Username VARCHAR(20) NOT NULL,\n'
                               'Password VARCHAR(20) NOT NULL,\n'
                               'Admin TEXT (1) NOT NULL ,\n'
                               'Pin INTEGER (6) NOT NULL);\n''')
            disconnect.close()
            print("Nexus > Files Created | System.db")
            print("Warning > System restarting")
            time.sleep(3)
            system_loading().check_dir()
        except Exception as error:
            print(error)


if __name__ == '__main__':
    print(NexusPB)
    print("System is initializing ..")
    time.sleep(4)
    try:
        if os.path.exists(conf_path):
            config = configparser.ConfigParser()
            config.read(conf_path)
            sys_version = config.get('Information', 'sys_version')
            conf_version = config.get('Information', 'conf_version')
            Force_Login = config.get('Settings', 'Force-Login')
            Simple_Mode = config.get('Settings', 'Simple-Mode')
            Lock_Mode = config.get('Settings', 'Lock-Mode')

        if Force_Login == 'True':
            try:
                print("Force Login | Enabled")
                print("Note - Lock Mode has been disabled.")
                print("")
                with open(conf_path, 'w') as configfile:
                    config.set("Settings", "lock-mode", 'False')
                    config.write(configfile)
            except Exception as error:
                print("Error 1")
                print(error)


        elif Lock_Mode == 'True':
            try:
                print("Nexus > Lock Mode | Enabled")
                print("Note - Force Login has been disabled")
                print("")
                with open(conf_path, 'w') as configfile:
                    config.set("Settings", "force-login", 'False')
                    config.write(configfile)
            except configparser.Error as error:
                print("Error 2 ?")
                print(error)
        else:
            print("System Login Functions Disabled")

        if Simple_Mode == 'True' or 'False':
            print("Settings Information: ")
            print("-------------------------------------")
            print(f"(#) Force Login Enabled | {Force_Login}")
            print(f"(#) Lock Mode Enabled | {Lock_Mode}")
            print(f"(#) Simple Mode Enabled | {Simple_Mode}")
            print("-------------------------------------")
            system_loading().check_dir()
        else:
            print("Files Missing | Creating files")
            system_loading().check_dir()

    except Exception:
        print("Files Missing | Creating files")
        system_loading().check_dir()
