import twilio
from twilio.rest import Client
from Placeholders import MainMenu_Icon, BetaMenu_Icon, VoiceMenu_Icon, SMSMenu_Icon, CustomMenu_Icon, CloseSys,SettingsMenu_Icon, ip
from Placeholders import MenuSelection
import sys
import os
import configparser
import time

config = configparser.ConfigParser()
config.read("C:/NovaOS/Modules/NexusPhoneBot/config.ini")


class SelectMenu:
    def MainMenu(self):
        print("Hello This was pushed to Git")
        print(MainMenu_Icon)
        print(MenuSelection["Main_1"])
        print(MenuSelection["Main_2"])
        print(MenuSelection["Main_3"])
        print(MenuSelection["Main_4"])
        print(MenuSelection["Main_5"])
        print(MenuSelection["Main_6"])
        print(MenuSelection["Main_quit"])
        user = input("> ")
        if user == '1':
            SelectMenu().SMSMenu()
        elif user == '2':
            SelectMenu().VoiceMenu()
        elif user == '3':
            SelectMenu().CustomMenu()
        elif user == '4':
            print("\nBETA MENU SELECTED ?")
            SelectMenu().BetaMenu()
        elif user == '5':
            SearchNumber()
        elif user == '6':
            SelectMenu().SettingsMenu()
        elif user == '7':
            SelectMenu().MainMenu()
        elif user in CloseSys:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Thank you for using Nexus")
            print("  [NovaOS Technology]")
            sys.exit()
        else:
            print("Nexus > Not an Option")
            time.sleep(0.8)
            SelectMenu().MainMenu()

    def SMSMenu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(SMSMenu_Icon)
        print(MenuSelection["SMS_1"])
        print(MenuSelection["SMS_2"])
        print(MenuSelection["SMS_3"])
        print(MenuSelection["SMS_4"])
        print(MenuSelection["SMS_back"])
        user = input("> ")
        if user == '1':
            SMS().SA(6, 10, 0)
        elif user == '2':
            SMS().SA(2, 20, 0)
        elif user == '3':
            SMS().ASA(0)
        elif user == '4':
            pass
        elif user.lower() == 'b':
            os.system('cls' if os.name == 'nt' else 'clear')
            SelectMenu().MainMenu()
        else:
            print("Nexus > Not an Option")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            SelectMenu().SMSMenu()

    def VoiceMenu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(VoiceMenu_Icon)
        print(MenuSelection["Voice_1"])
        print(MenuSelection["Voice_2"])
        print(MenuSelection["Voice_3"])
        print(MenuSelection["Voice_4"])
        print(MenuSelection["Voice_back"])
        user = input("> ")
        if user == '1':
            Voice().BVA(5, 10, 0)
        elif user == '2':
            Voice().AVA(2, 30, 0)
        elif user == '3':
            Voice().MA(10, 3, 0)
        elif user == '4':
            pass
        elif user.lower() == 'b':
            os.system('cls' if os.name == 'nt' else 'clear')
            SelectMenu().MainMenu()
        else:
            print("Nexus > Not an Option")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            SelectMenu().SMSMenu()

    def CustomMenu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(CustomMenu_Icon)
        print(MenuSelection["Custom_1"])
        print(MenuSelection["Custom_2"])
        print(MenuSelection["Custom_back"])
        user = input("> ")
        if user == '1':
            Voice().Custom(0)
        elif user == '2':
            SMS().Custom(0)
        elif user.lower() == 'b':
            os.system('cls' if os.name == 'nt' else 'clear')
            SelectMenu().MainMenu()
        else:
            print("Nexus > Not an Option")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            SelectMenu().CustomMenu()

    def BetaMenu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(BetaMenu_Icon)
        print(MenuSelection["Beta_1"])
        print(MenuSelection["Beta_2"])
        print(MenuSelection["Beta_3"])
        print(MenuSelection["Beta_4"])
        print(MenuSelection["Beta_back"])
        user = input("> ")
        if user == '1':
            pass
        elif user == '2':
            pass
        elif user == '3':
            pass
        elif user == '4':
            pass
        elif user.lower() == 'b':
            os.system('cls' if os.name == 'nt' else 'clear')
            SelectMenu().MainMenu()
        else:
            print("Nexus > Not an Option")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            SelectMenu().BetaMenu()

    def SettingsMenu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(SettingsMenu_Icon)
        print(MenuSelection["Settings_1"])
        print(MenuSelection["Settings_2"])
        print(MenuSelection["Settings_3"])
        print(MenuSelection["Settings_4"])
        print(MenuSelection["Settings_5"])
        print(MenuSelection["Settings_back"])
        user = input("> ")
        if user == '1':
            pass
        elif user == '2':
            pass
        elif user == '3':
            pass
        elif user == '4':
            pass
        elif user.lower() == 'b':
            os.system('cls' if os.name == 'nt' else 'clear')
            SelectMenu().MainMenu()
        else:
            print("Nexus > Not an Option")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            SelectMenu().SMSMenu()


class Voice:
    def VA(self, delay, attack_count, count):
        SysTime = time.ctime()
        ACCOUNT_SID = config.get('Settings', 'Account-SID')
        AUTH_TOKEN = config.get('Settings', 'Auth-Token')
        Voice_link = config.get('Settings', 'Voice-link')
        Attacker = config.get('Settings', 'Bot-Number')
        victim = ''
        while victim is not int:
            try:
                victim = int(input('Nexus > Victims Number: '))
                if len(str(victim)) == 10:
                    print(f"Nexus > Number is valid | {victim}")
                    break
                else:
                    print(f"Nexus > Number is Invalid | {victim}")
            except ValueError:
                print("Nexus > Must be a number and contain no numbers or symbol's")

        print("Nexus > Get Ready to Attack | Number Valid")
        print("<---------[Attack Information]-------->\n"
              f"[*] Bots Number    | ({Attacker})\n"
              f"[*] Victims Number | ({victim})\n"
              f"[*] Attack Delay   | ({delay}) seconds\n"
              f"[*] Attack Count   | ({attack_count}) Attacks\n"
              "<------------------------------------->")
        user = input("If all is correct Press [Y] if not press [N]\n> ").lower()
        if user == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Nexus > Started Attack | {SysTime}")
            try:
                client = Client(ACCOUNT_SID, AUTH_TOKEN)
                while count < attack_count:
                    client.calls.create(
                        to=victim,
                        from_=Attacker,
                        url=Voice_link
                    )
                    count += 1
                    time.sleep(delay)
                    print(f"Nexus > Bot Made a Call to: [{victim}] from [{Attacker})] | ({count}/{attack_count})")
                    time.sleep(delay)
                print(f"Nexus > Attack Over ! | [{count}/{attack_count}]")
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                SelectMenu().MainMenu()
            except Exception as error:
                print(error)
        elif user in CloseSys:
            Voice().BVA(5, 10, 0)
        else:
            print("Nexus > Not an option")
            time.sleep(3)
            SelectMenu().VoiceMenu()

    def MA(self, delay, attack_count, count):
        SysTime = time.ctime()
        ACCOUNT_SID = config.get('Settings', 'Account-SID')
        AUTH_TOKEN = config.get('Settings', 'Auth-Token')
        Attacker = config.get('Settings', 'Bot-Number')
        Music_Link = config.get('Settings', 'Music-Link')
        victim = ''
        while victim is not int:
            try:
                victim = int(input('Nexus > Victims Number: '))
                if len(str(victim)) == 10:
                    print(f"Nexus > Number is valid | {victim}")
                    break
                else:
                    print(f"Nexus > Number is Invalid | {victim}")
            except ValueError:
                print("Nexus > Must be a number and contain no letters or symbol's")

        print("Nexus > Get Ready to Attack | Number Valid")
        print("WARNING - This is an intense attack please use default settings.")
        time.sleep(2)
        print("<---------[Attack Information]-------->\n"
              f"[*] Bots Number    | ({Attacker})\n"
              f"[*] Victims Number | ({victim})\n"
              f"[*] Attack Delay   | ({delay}) seconds\n"
              f"[*] Attack Count   | ({attack_count}) Attacks\n"
              "<------------------------------------->")
        user = input("If all is correct Press [Y] if not press [N]\n> ").lower()
        if user == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Nexus > Started Attack | {SysTime}")
            try:
                client = Client(ACCOUNT_SID, AUTH_TOKEN)
                while count < attack_count:
                    client.calls.create(
                        to=victim,
                        from_=Attacker,
                        url=Music_Link
                    )
                    count += 1
                    print(f"Nexus > Bot Made a Call to: [{victim}] from [{Attacker})] | ({count}/{attack_count})")
                    time.sleep(delay)
                print(f"Nexus > Attack Over ! | [{count}/{attack_count}]")
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                SelectMenu().MainMenu()
            except Exception as error:
                print(error)
        elif user in CloseSys:
            Voice().MA(10, 3, 0)
        else:
            print("Nexus > Not an option")
            time.sleep(3)
            SelectMenu().VoiceMenu()

    def MMA(self):  # Mad Max Attack (MMA)
        pass


    def Custom(self, count):
        SysTime = time.ctime()
        ACCOUNT_SID = config.get('Settings', 'Account-SID')
        AUTH_TOKEN = config.get('Settings', 'Auth-Token')
        Voice_link = config.get('Settings', 'Voice-link')
        Attacker = config.get('Settings', 'Bot-Number')
        delay = ''
        attack_count = ''
        victim = ''
        while delay is not int:
            try:
                delay = int(input('Nexus > Delay in seconds: '))
                if delay <= 5:
                    print("[X] Warning [X] This is a very Low delay recommended (10)")
                print("Nexus > Number Accepted (!)")
                break
            except ValueError:
                print("Nexus > Must be an int/Whole number")

        while attack_count is not int:
            try:
                attack_count = int(input('Nexus > Number of Attacks: '))
                if attack_count >= 70:
                    print(f"[X] Warning [X] You are about to send ({attack_count}) recommended (30)")
                break
            except ValueError:
                print("Nexus > Must be an int/Whole number")

        while victim is not int:
            try:
                victim = int(input('Nexus > Victims Number: '))
                if len(str(victim)) == 10:
                    print(f"Nexus > Number is valid | {victim}")
                    break
                else:
                    print(f"Nexus > Number is Invalid | {victim}")
            except ValueError:
                print("Nexus > Must be a number and contain no numbers or symbol's")

        print("Nexus > Get Ready to Attack | Number Valid")
        print("<---------[Attack Information]-------->\n"
              f"[*] Bots Number    | ({Attacker})\n"
              f"[*] Victims Number | ({victim})\n"
              f"[*] Attack Delay   | ({delay}) seconds\n"
              f"[*] Attack Count   | ({attack_count}) Attacks\n"
              f"[*] System IP      | ({ip})\n"
              f"[*] VoIP server    | (False/Null)\n"
              "<------------------------------------->")
        user = input("If all is correct Press [Y] if not press [N]\n> ").lower()
        if user == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Nexus > Started Attack | {SysTime}")
            try:
                client = Client(ACCOUNT_SID, AUTH_TOKEN)
                while count < attack_count:
                    client.calls.create(
                        to=victim,
                        from_=Attacker,
                        url=Voice_link
                    )
                    count += 1
                    print(f"Nexus > Bot Made a Call to: [{victim}] from [{Attacker})] | ({count}/{attack_count}) | (IP: {ip})")
                    time.sleep(delay)
                print(f"Nexus > Attack Over ! | [{count}/{attack_count}]")
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                SelectMenu().MainMenu()
            except Exception as error:
                print(error)
        elif user in CloseSys:
            Voice().Custom(0)
        else:
            print("Nexus > Not an option")
            time.sleep(3)
            SelectMenu().VoiceMenu()


class SMS:
    def SA(self, delay, attack_count, count):
        SysTime = time.ctime()
        ACCOUNT_SID = config.get('Settings', 'Account-SID')
        AUTH_TOKEN = config.get('Settings', 'Auth-Token')
        Attacker = config.get('Settings', 'Bot-Number')
        victim = ''
        while victim is not int:
            try:
                victim = int(input('Nexus > Victims Number: '))
                if len(str(victim)) == 10:
                    print(f"Nexus > Number is valid | {victim}")
                    break
                else:
                    print(f"Nexus > Number is Invalid | {victim}")
            except ValueError:
                print("Nexus > Must be a number and contain no letters or symbol's")

        print("Nexus > Get Ready to Attack | Number Valid")
        print("<---------[Attack: Basic SMS]-------->\n"
              f"[*] Bots Number    | ({Attacker})\n"
              f"[*] Victims Number | ({victim})\n"
              f"[*] Attack Delay   | ({delay}) seconds\n"
              f"[*] Attack Count   | ({attack_count}) Attacks\n"
              "<------------------------------------->")
        user = input("If all is correct Press [Y] if not press [N]\n> ").lower()
        if user == 'y':
            client = Client(ACCOUNT_SID, AUTH_TOKEN)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Nexus > Started Attack | {SysTime}")
            while count < attack_count:
                try:
                    client.messages.create(
                        to=victim,
                        from_=Attacker,
                        body="Test"
                    )
                    count += 1
                    print(f"Nexus > Bot Made a Call to: [{victim}] from [{Attacker})] | ({count}/{attack_count})")
                    time.sleep(delay)
                except twilio.rest.TwilioException:
                    print(f"Nexus > Your Number has been blocked by the user. | {victim}")
                    time.sleep(2)
                    SelectMenu().SMSMenu()

    def CSA(self, count): # Custom SMS Attack - ASM
        SysTime = time.ctime()
        ACCOUNT_SID = config.get('Settings', 'Account-SID')
        AUTH_TOKEN = config.get('Settings', 'Auth-Token')
        Attacker = config.get('Settings', 'Bot-Number')
        victim = ''
        delay = input("Please enter a delay in seconds: ")
        attack_count = input("Please enter number of attacks: ")
        response = input("Please enter a custom message: ")
        while victim is not int:
            try:
                victim = int(input('Nexus > Victims Number: '))
                if len(str(victim)) == 10:
                    print(f"Nexus > Number is valid | {victim}")
                    break
                else:
                    print(f"Nexus > Number is Invalid | {victim}")
            except ValueError:
                print("Nexus > Must be a number and contain no letters or symbol's")

        print("Nexus > Get Ready to Attack | Number Valid")
        print("<---------[Attack: Basic SMS]-------->\n"
              f"[*] Bots Number    | ({Attacker})\n"
              f"[*] Victims Number | ({victim})\n"
              f"[*] Attack Delay   | ({delay}) seconds\n"
              f"[*] Attack Count   | ({attack_count}) Attacks\n"
              f'[*] Attack Response| ("{response}")'
              "<------------------------------------->")
        user = input("If all is correct Press [Y] if not press [N] | Press [Enter] to Main Menu\n> ").lower()
        if user.lower()== 'y':
            client = Client(ACCOUNT_SID, AUTH_TOKEN)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Nexus > Started Attack | {SysTime}")
            while int(count) < attack_count:
                try:
                    client.messages.create(
                        to=victim,
                        from_=Attacker,
                        body=response
                    )
                    count += 1
                    print(f"Nexus > Bot Made a Call to: [{victim}] from [{Attacker})] | ({count}/{attack_count})")
                    time.sleep(int(delay))
                except twilio.rest.TwilioException:
                    print(f"Nexus > Your Number has been blocked by the user. | {victim}")
                    time.sleep(2)
                    SelectMenu().SMSMenu()
        elif user in CloseSys:
            print("Nexus > Going back")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            SMS().ASA(0)
        else:
            print("Nexus > Going to Main Menu |")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            SelectMenu().MainMenu()
    def Custom(self, count):
        SysTime = time.ctime()
        ACCOUNT_SID = config.get('Settings', 'Account-SID')
        AUTH_TOKEN = config.get('Settings', 'Auth-Token')
        Voice_link = config.get('Settings', 'Voice-link')
        Attacker = config.get('Settings', 'Bot-Number')
        delay = ''
        attack_count = ''
        victim = ''
        while delay is not int:
            try:
                delay = int(input('Nexus > Delay in seconds: '))
                if delay <= 5:
                    print("[X] Warning [X] This is a very Low delay recommended (10)")
                print("Nexus > Number Accepted (!)")
                break
            except ValueError:
                print("Nexus > Must be an int/Whole number")

        while attack_count is not int:
            try:
                attack_count = int(input('Nexus > Number of Attacks: '))
                if attack_count >= 70:
                    print(f"[X] Warning [X] You are about to send ({attack_count}) recommended (30)")
                break
            except ValueError:
                print("Nexus > Must be an int/Whole number")

        while victim is not int:
            try:
                victim = int(input('Nexus > Victims Number: '))
                if len(str(victim)) == 10:
                    print(f"Nexus > Number is valid | {victim}")
                    break
                else:
                    print(f"Nexus > Number is Invalid | {victim}")
            except ValueError:
                print("Nexus > Must be a number and contain no numbers or symbol's")

        message = input("Enter Custom Message: ")

        print("Nexus > Get Ready to Attack | Number Valid")
        print("<---------[Attack Information]-------->\n"
              f"[*] Bots Number    | ({Attacker})\n"
              f"[*] Victims Number | ({victim})\n"
              f"[*] Attack Delay   | ({delay}) seconds\n"
              f"[*] Attack Count   | ({attack_count}) Attacks\n"
              f"[*] Message        | ({message})\n"
              f"[*] System IP      | ({ip})\n"
              f"[*] VoIP server    | (False/Null)\n"
              "<------------------------------------->")
        user = input("Nexus > Ready to Attack ?\n[Y] - Start Attack\n[N] - Change Settings\n> ").lower()
        if user == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Nexus > Started Attack | {SysTime}")
            try:
                client = Client(ACCOUNT_SID, AUTH_TOKEN)
                while count < attack_count:
                    client.messages.create(
                        to=victim,
                        from_=Attacker,
                        body=message
                    )
                    count += 1
                    print(f"Nexus > Bot Made a Call to: [{victim}] from [{Attacker})] | ({count}/{attack_count}) | (IP: {ip})")
                    time.sleep(delay)
                print(f"Nexus > Attack Over ! | [{count}/{attack_count}]")
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                SelectMenu().MainMenu()
            except Exception as error:
                print(error)
        elif user in CloseSys:
            Voice().Custom(0)
        else:
            print("Nexus > This is not an option.")
            time.sleep(3)
            SelectMenu().VoiceMenu()


class Music:
    def MA(self, delay, attack_count, count):
        SysTime = time.ctime()
        ACCOUNT_SID = config.get('Settings', 'Account-SID')
        AUTH_TOKEN = config.get('Settings', 'Auth-Token')
        Attacker = config.get('Settings', 'Bot-Number')
        Music_Link = config.get('Settings', 'Music-Link')
        victim = ''
        while victim is not int:
            try:
                victim = int(input('Nexus > Victims Number: '))
                if len(str(victim)) == 10:
                    print(f"Nexus > Number is valid | {victim}")
                    break
                else:
                    print(f"Nexus > Number is Invalid | {victim}")
            except ValueError:
                print("Nexus > Must be a number and contain no letters or symbol's")

        print("Nexus > Get Ready to Attack | Number Valid")
        print("<---------[Attack: Basic SMS]-------->\n"
              f"[*] Bots Number    | ({Attacker})\n"
              f"[*] Victims Number | ({victim})\n"
              f"[*] Attack Delay   | ({delay}) seconds\n"
              f"[*] Attack Count   | ({attack_count}) Attacks\n"
              "<------------------------------------->")
        user = input("If all is correct Press [Y] if not press [N] | Press [Enter] to go back\n> ").lower()
        if user == 'y':
            client = Client(ACCOUNT_SID, AUTH_TOKEN)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Nexus > Started Attack | {SysTime}")
            while count < attack_count:
                try:
                    client.messages.create(
                        to=victim,
                        from_=Attacker,
                        body="Test"
                    )
                    count += 1
                    print(f"Nexus > Bot Made a Call to: [{victim}] from [{Attacker})] | ({count}/{attack_count})")
                    time.sleep(delay)
                except twilio.rest.TwilioException:
                    print(f"Nexus > Your Number has been blocked by the user. | {victim}")
                    time.sleep(2)
                    SelectMenu().SMSMenu()
        elif user in CloseSys:
            Music().BMA(15, 3, 0)
        else:
            print("Nexus > Not an option")
            time.sleep(3)
            SelectMenu().VoiceMenu()


def SearchNumber():
    print("Waring this will charge your Twilio account 15 cents per lookup.")
    print("Same rates apply to making bot calls.")
    user = input("Would you like to search a number [Y/N]\n> ")
    if user == 'y'.lower():
        print("Ok checking number")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Ok going back ?")
        SelectMenu().MainMenu()
