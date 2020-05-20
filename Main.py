import twilio
from twilio.rest import Client
from Placeholders import BetaMenu_Icon, VoiceMenu_Icon, SMSMenu_Icon, FunMenu_Icon, CloseSys,SettingsMenu_Icon, ip, MenuSelection, CN, CAC,CD,SearchNumber,Nexus,NexusPB
from CrashManager import crash
from emoji import emoji
import random
import sys
import os
import configparser
import time

config = configparser.ConfigParser()
config.read("C:/NovaOS/Modules/NexusPhoneBot/config.ini")


class SelectMenu:
    def MainMenu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Nexus)
        print(MenuSelection["Main_1"])
        print(MenuSelection["Main_2"])
        print(MenuSelection["Main_3"])
        print(MenuSelection["Main_4"])
        print(MenuSelection["Main_5"])
        print(MenuSelection["Main_6"])
        print(MenuSelection["Main_quit"])
        print("-----------------------------")
        user = input("Nexus > ")
        if user == '1':
            SelectMenu().SMSMenu()
        elif user == '2':
            SelectMenu().VoiceMenu()
        elif user == '3':
            SelectMenu().FunMenu()
        elif user == '4':
            SelectMenu().BetaMenu()
        elif user == '5':
            ACCOUNT_SID = config.get('Settings', 'Account-SID')
            AUTH_TOKEN = config.get('Settings', 'Auth-Token')
            Log_Path = config.get('Settings', 'Log-Path')
            num = ''
            SearchNumber(num, ACCOUNT_SID, AUTH_TOKEN,Log_Path)
            time.sleep(3)
            SelectMenu().MainMenu()
        elif user == '6':
            SelectMenu().SettingsMenu()
        elif user in CloseSys:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(NexusPB)
            print("Closing System. Thank you for using Nexus Phone Bot")
            print('       [A NovaOSTechnology Program]\n\n\n')
            sys.exit()
        else:
            print("Nexus > Not an Option")
            time.sleep(0.8)
            SelectMenu().MainMenu()

    def SMSMenu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(SMSMenu_Icon)
        print("-----------------------------")
        print(MenuSelection["SMS_1"])
        print(MenuSelection["SMS_2"])
        print(MenuSelection["SMS_3"])
        print(MenuSelection["SMS_back"])
        print("-----------------------------")
        user = input("Nexus > ")
        if user == '1':
            SMS().SA(6, 10)
        elif user == '2':
            SMS().SA(2, 20)
        elif user == '3':
            SMS().Custom()
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
        print("-----------------------------")
        print(MenuSelection["Voice_1"])
        print(MenuSelection["Voice_2"])
        print(MenuSelection["Voice_3"])
        print(MenuSelection["Voice_back"])
        print("-----------------------------")
        user = input("Nexus > ")
        if user == '1':
            Voice().VA(5, 10)
        elif user == '2':
            Voice().VA(2, 30)
        elif user == '3':
            Voice().Custom()
        elif user.lower() == 'b':
            os.system('cls' if os.name == 'nt' else 'clear')
            SelectMenu().MainMenu()
        else:
            print("Nexus > Not an Option")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            SelectMenu().SMSMenu()

    def FunMenu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(FunMenu_Icon)
        print("-----------------------------")
        print(MenuSelection["Fun_1"])
        print(MenuSelection["Fun_2"])
        print(MenuSelection["Fun_3"])
        print(MenuSelection["Fun_4"])
        print(MenuSelection["Fun_back"])
        print("-----------------------------")
        user = input("Nexus > ")
        if user == '1':
            Fun().EA2(4,10)
        elif user == '2':
            Fun().MA(60,2)
        elif user == '3':
            print("COMING SOON !")
            time.sleep(1.5)
            SelectMenu().MainMenu()
        elif user == '4':
            Fun().MMA(5,4)
        elif user.lower() == 'b':
            os.system('cls' if os.name == 'nt' else 'clear')
            SelectMenu().MainMenu()
        else:
            print("Nexus > Not an Option")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            SelectMenu().FunMenu()

    def BetaMenu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(BetaMenu_Icon)
        print("-----------------------------")
        print(MenuSelection["Beta_1"])
        print(MenuSelection["Beta_2"])
        print(MenuSelection["Beta_3"])
        print(MenuSelection["Beta_4"])
        print(MenuSelection["Beta_back"])
        print("-----------------------------")
        user = input("Nexus > ")
        if user == '1':
            SelectMenu().MainMenu()
        elif user == '2':
            SelectMenu().MainMenu()
        elif user == '3':
            SelectMenu().MainMenu()
        elif user == '4':
            SelectMenu().MainMenu()
        elif user.lower() == 'b':
            SelectMenu().MainMenu()
        else:
            print("Nexus > Not an Option")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            SelectMenu().BetaMenu()

    def SettingsMenu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(SettingsMenu_Icon)
        print("-----------------------------")
        print(MenuSelection["Settings_1"])
        print(MenuSelection["Settings_2"])
        print(MenuSelection["Settings_3"])
        print(MenuSelection["Settings_4"])
        print(MenuSelection["Settings_5"])
        print(MenuSelection["Settings_back"])
        print("-----------------------------")
        user = input("Nexus > ")
        if user == '1':
            SelectMenu().MainMenu()
        elif user == '2':
            SelectMenu().MainMenu()
        elif user == '3':
            SelectMenu().MainMenu()
        elif user == '4':
            SelectMenu().MainMenu()
        elif user.lower() == 'b':
            os.system('cls' if os.name == 'nt' else 'clear')
            SelectMenu().MainMenu()
        else:
            print("Nexus > Not an Option")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            SelectMenu().SMSMenu()

class Voice:
    def VA(self,delay, attack_count): #Voice Attack (VA)
        SysTime = time.ctime()
        ACCOUNT_SID = config.get('Settings', 'Account-SID')
        AUTH_TOKEN = config.get('Settings', 'Auth-Token')
        Voice_link = config.get('Settings', 'Voice-link')
        Attacker = config.get('Settings', 'Bot-Number')
        victim = ''
        victim = CN(victim)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Nexus > Get Ready to Attack | Settings Valid\n")
        print("<---------[Attack: Voice]-------->\n"
              f"[*] Bots Number    | ({Attacker})\n"
              f"[*] Victims Number | ({victim})\n"
              f"[*] Attack Delay   | ({delay}) seconds\n"
              f"[*] Attack Count   | ({attack_count}) Attacks\n"
              "<-------------------------------------->")
        user = input("Nexus > Ready to Attack ?\n[Y] - Start Attack\n[N] - Go Back\n> ").lower()
        if user == 'y':
            try:
                client = Client(ACCOUNT_SID, AUTH_TOKEN)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"Nexus > Started Attack | {SysTime}")
                for i in range(attack_count):
                    i += 1
                    client.calls.create(
                        to=victim,
                        from_=Attacker,
                        url=Voice_link
                    )
                    print(f"Nexus > Bot Made a Call to: [{victim}] from [{Attacker})] | ({i}/{attack_count})")
                    time.sleep(delay)
                print(f"Nexus > Attack Over ! | [{i}/{attack_count}]")
                time.sleep(2.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                SelectMenu().MainMenu()
            except Exception as error:
                crash().Create_Log(error)
        elif user in CloseSys:
            SelectMenu().VoiceMenu()
        else:
            print("Nexus > Not an Option")
            time.sleep(2.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            SelectMenu().VoiceMenu()

    def Custom(self):
        SysTime = time.ctime()
        ACCOUNT_SID = config.get('Settings', 'Account-SID')
        AUTH_TOKEN = config.get('Settings', 'Auth-Token')
        Attacker = config.get('Settings', 'Bot-Number')
        delay = ''
        attack_count = ''
        victim = ''

        victim = CN(victim)
        attack_count = CAC(attack_count)
        delay = CD(delay)
        Voice_link = input("Please enter a Voice Link: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Nexus > Get Ready to Attack | Settings Valid\n")
        print("<---------[Attack: Custom Voice]-------->\n"
              f"[*] Bots Number    | ({Attacker})\n"
              f"[*] Victims Number | ({victim})\n"
              f"[*] Attack Delay   | ({delay}) seconds\n"
              f"[*] Attack Count   | ({attack_count}) Attacks\n"
              f"[*] Voice Link     | ({Voice_link})"
              f"[*] System IP      | ({ip})\n"
              f"[*] VoIP server    | (False/Null)\n"
              "<------------------------------------->")
        user = input("Nexus > Start Attack ?\n[Y] - Start Attack\n[C] - Change Settings\n[B] - Go Back\n> ").lower()
        if user == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Nexus > Started Attack | {SysTime}")
            try:
                client = Client(ACCOUNT_SID, AUTH_TOKEN)
                i: int
                for i in range(attack_count):
                    i += 1
                    client.calls.create(
                        to=victim,
                        from_=Attacker,
                        url=Voice_link
                    )
                    print(f"Nexus > Bot Made a Call to: [{victim}] from [{Attacker})] | ({i}/{attack_count}) | (IP: {ip})")
                    time.sleep(delay)
                print(f"Nexus > Attack Over ! | [{i}/{attack_count}]")
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                SelectMenu().MainMenu()
            except Exception as error:
                crash.Create_Log(error)
        elif user in CloseSys:
            SelectMenu().VoiceMenu()
        elif user == 'c':
            Voice().Custom()
        else:
            print("Nexus > Not an option")
            time.sleep(3)
            SelectMenu().VoiceMenu()

class SMS:
    def SA(self, delay, attack_count): #SMS Attack Basic (SA)
        os.system('cls' if os.name == 'nt' else 'clear')
        SysTime = time.ctime()
        ACCOUNT_SID = config.get('Settings', 'Account-SID')
        AUTH_TOKEN = config.get('Settings', 'Auth-Token')
        Attacker = config.get('Settings', 'Bot-Number')
        victim = ''
        victim = CN(victim)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Nexus > Get Ready to Attack | Settings Valid\n")
        print("<---------[Attack: SMS]-------->\n"
              f"[*] Bots Number    | ({Attacker})\n"
              f"[*] Victims Number | ({victim})\n"
              f"[*] Attack Delay   | ({delay}) seconds\n"
              f"[*] Attack Count   | ({attack_count}) Attacks\n"
              "<------------------------------>")
        user = input("Nexus > Ready to Attack ?\n[Y] - Start Attack\n[N] - Go Back\nNexus > ").lower()
        if user == 'y':
            try:
                client = Client(ACCOUNT_SID, AUTH_TOKEN)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"Nexus > Started Attack | {SysTime}")
                for i in range(attack_count):
                    try:
                        i += 1
                        client.messages.create(
                            to=victim,
                            from_=Attacker,
                            body='Your phone has been targeted by Nexus 3.0.1 🤬'
                        )
                        print(f"Nexus > Bot send a message: [{victim}] from [{Attacker})] | ({i}/{attack_count})")
                        time.sleep(delay)
                    except twilio.rest.TwilioException:
                        print(f"Nexus > Your Number has been blocked by the user. | {victim}")
                        time.sleep(2)
                        SelectMenu().SMSMenu()
            except Exception as error:
                crash().Create_Log(error)

            print(f"Nexus > Attack Over ! | [{i}/{attack_count}]")
            time.sleep(2.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            SelectMenu().MainMenu()

        elif user in CloseSys:
            SelectMenu().SMSMenu()
        else:
            print("Nexus > Not an option")
            time.sleep(3)
            SelectMenu().SMSMenu()





    def Custom(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        SysTime = time.ctime()
        ACCOUNT_SID = config.get('Settings', 'Account-SID')
        AUTH_TOKEN = config.get('Settings', 'Auth-Token')
        Attacker = config.get('Settings', 'Bot-Number')
        delay = ''
        attack_count = ''
        victim = ''

        victim = CN(victim)
        attack_count = CAC(attack_count)
        delay = CD(delay)
        message = input("Nexus > Please enter a message: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Nexus > Get Ready to Attack | Settings Valid\n")
        print("<---------[Attack: Custom SMS]-------->\n"
              f"[*] Bots Number    | ({Attacker})\n"
              f"[*] Victims Number | ({victim})\n"
              f"[*] Attack Delay   | ({delay}) seconds\n"
              f"[*] Attack Count   | ({attack_count}) Attacks\n"
              f"[*] Message        | ({message})\n"
              f"[*] System IP      | ({ip})\n"
              f"[*] VoIP server    | (False/Null)\n"
              "<------------------------------------->")
        user = input("Nexus > Start Attack ?\n[Y] - Start Attack\n[C] - Change Settings\n[B] - Go Back\nNexus > ").lower()
        if user == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Nexus > Started Attack | {SysTime}")
            try:
                client = Client(ACCOUNT_SID, AUTH_TOKEN)
                i: int
                for i in range(attack_count):
                    i += 1
                    client.messages.create(
                        to=victim,
                        from_=Attacker,
                        body=message
                    )
                    print(f"Nexus > Bot Made a Call to: [{victim}] from [{Attacker})] | ({i}/{attack_count}) | (IP: {ip})")
                    time.sleep(delay)
                print(f"Nexus > Attack Over ! | [{i}/{attack_count}]")
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                SelectMenu().MainMenu()
            except Exception as error:
                crash.Create_Log(error)
        elif user in CloseSys:
            SelectMenu().SMSMenu()
        elif user == 'c':
            os.system('cls' if os.name == 'nt' else 'clear')
            SMS().Custom()
        else:
            print("Nexus > Not an option")
            time.sleep(3)
            SelectMenu().SMSMenu()

class Fun:
    def EA2(self,delay, attack_count):
        os.system('cls' if os.name == 'nt' else 'clear')
        SysTime = time.ctime()
        ACCOUNT_SID = config.get('Settings', 'Account-SID')
        AUTH_TOKEN = config.get('Settings', 'Auth-Token')
        Attacker = config.get('Settings', 'Bot-Number')
        victim = ''
        victim = CN(victim)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Nexus > Get Ready to Attack | Settings Valid\n")
        print("<---------[Attack: Emoji v2]-------->\n"
              f"[*] Bots Number    | ({Attacker})\n"
              f"[*] Victims Number | ({victim})\n"
              f"[*] Attack Delay   | ({delay}) seconds\n"
              f"[*] Attack Count   | ({attack_count}) Attacks\n"
              f"[*] Fist Message   | ({emoji[0]})\n"
              "<------------------------------------->")
        user = input("Nexus > Ready to Attack ?\n[Y] - Start Attack\n[N] - Go Back\n> ").lower()
        if user == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Nexus > Started Attack | {SysTime}")
            try:
                client = Client(ACCOUNT_SID, AUTH_TOKEN)
                for i in range(attack_count):
                    ID = random.randint(0,33)
                    i += 1
                    client.messages.create(
                        to=victim,
                        from_=Attacker,
                        body=emoji[ID]
                    )
                    print(f"Nexus > Bot Made a Call to: [{victim}] from [{Attacker})] | ({i}/{attack_count})")
                    time.sleep(delay)
                print(f"Nexus > Attack Over ! | [{i}/{attack_count}]")
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                SelectMenu().MainMenu()
            except Exception as error:
                crash.Create_Log(error)

        elif user in CloseSys:
            SelectMenu().FunMenu()

        else:
            print("Nexus > Not an option")
            time.sleep(3)
            SelectMenu().FunMenu()

    def MA(self, delay, attack_count): #Music Attack - (MA)
        os.system('cls' if os.name == 'nt' else 'clear')
        SysTime = time.ctime()
        ACCOUNT_SID = config.get('Settings', 'Account-SID')
        AUTH_TOKEN = config.get('Settings', 'Auth-Token')
        Attacker = config.get('Settings', 'Bot-Number')
        Music_link = config.get('Settings', 'Music-Link')
        victim = ''
        victim = CN(victim)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Nexus > Get Ready to Attack | Settings Valid\n")
        print("<---------[Attack: Music Voice]-------->\n"
              f"[*] Bots Number    | ({Attacker})\n"
              f"[*] Victims Number | ({victim})\n"
              f"[*] Attack Delay   | ({delay}) seconds\n"
              f"[*] Attack Count   | ({attack_count}) Attacks\n"
              f"[*] Music Link     | ({Music_link})\n"
              "<-------------------------------------->")
        user = input("Nexus > Ready to Attack ?\n[Y] - Start Attack\n[C] - Change settings\n[B] - Go Back\nNexus > ").lower()
        if user == 'y':
            try:
                client = Client(ACCOUNT_SID, AUTH_TOKEN)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("[X] - Warning because this is a video it will send every 1 minute")
                print(f"Nexus > Started Attack | {SysTime}")
                for i in range(attack_count):
                    i += 1
                    client.calls.create(
                        to=victim,
                        from_=Attacker,
                        url=Music_link
                    )
                    print(f"Nexus > Bot Made a Call to: [{victim}] from [{Attacker})] | ({i}/{attack_count})")
                    time.sleep(delay)
                print(f"Nexus > Attack Over ! | [{i}/{attack_count}]")
                time.sleep(2.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                SelectMenu().MainMenu()
            except Exception as error:
                crash().Create_Log(error)
        elif user in CloseSys:
            SelectMenu().FunMenu()
        elif user == 'c':
            Fun().MA(60,3)
        else:
            print("Nexus > Not an Option")
            time.sleep(2.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            SelectMenu().FunMenu()


    def MMA(self, delay, attack_count): #Mad Max Attack - (MMA)
        os.system('cls' if os.name == 'nt' else 'clear')
        SysTime = time.ctime()
        ACCOUNT_SID = config.get('Settings', 'Account-SID')
        AUTH_TOKEN = config.get('Settings', 'Auth-Token')
        Attacker = config.get('Settings', 'Bot-Number')
        Music_link = config.get('Settings', 'Music-Link')
        Voice_link = config.get('Settings', 'Voice-link')
        victim = ''
        victim = CN(victim)
        message = 'Your phone has been targeted by Nexus 3.0.1 🤬'
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Nexus > Get Ready to Attack | Settings Valid\n")
        print("<------------[Attack: Mad Max]----------->\n"
              f"[*] Bots Number    | ({Attacker})\n"
              f"[*] Victims Number | ({victim})\n"
              f"[*] Attack Delay   | ({delay}) seconds\n"
              f"[*] Attack Count   | ({attack_count}) Attacks\n"
              f"[*] System IP      | ({ip})\n"
              f"[*] VoIP server    | (False/Null)\n"
              "<---------[Attack links/messages]-------->\n"
              f"[*] Music Link     | ({Music_link})\n"
              f"[*] Voice Link     | ({Voice_link})\n"
              f"[*] System Message | ({message})\n"
              f"[*] Emoji message  | ({emoji[0]})\n"
              "<----------------------------------------->")
        user = input("Nexus > Ready to Attack ?\n[Y] - Start Attack\n[C] - Change settings\n[B] - Go Back\nNexus > ").lower()
        if user == 'y':
            try:
                client = Client(ACCOUNT_SID, AUTH_TOKEN)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("[X] WARNING > This is a VERY intense attack. Use with care No custom mode available [*]")
                time.sleep(6)
                print(f"Nexus > Started Attack | {SysTime}")
                for i in range(attack_count):
                    i += 1
                    ID = random.randint(0, 33)
                    client.calls.create(to=victim, from_=Attacker, url=Music_link)
                    client.calls.create(to=victim, from_=Attacker, url=Voice_link)
                    client.messages.create(to=victim, from_=Attacker, body=message)
                    client.messages.create(to=victim, from_=Attacker, body=emoji[ID])
                    print(f"Nexus > Bot sent a Message/Call to: [{victim}] from [{Attacker})] | ({i}/{attack_count}) | (IP: {ip})")
                    time.sleep(delay)

                print(f"Nexus > Attack Over ! | [{i}/{attack_count}]")
                time.sleep(2.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                SelectMenu().MainMenu()
            except Exception as error:
                crash().Create_Log(error)
        elif user in CloseSys:
            SelectMenu().FunMenu()
        elif user == 'c':
            Fun().MMA(5,4)
        else:
            print("Nexus > Not an Option")
            time.sleep(2.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            SelectMenu().FunMenu()
