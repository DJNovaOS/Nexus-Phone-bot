import time
import os
from Placeholders import crash_logo, NovaAI
import configparser
import sys

config = configparser.ConfigParser()
config.read("C:/NovaOS/Modules/NexusPhoneBot/config.ini")


class crash:
    def Create_Log(self, error):
        LogPath = config.get('Settings', 'Log-Path')
        print("[X] The System has crashed we are creating a log file/Report...")
        try:
            if os.path.isdir(str(LogPath)):
                pass
            else:
                os.makedirs(str(LogPath))
        except Exception:
            print(NovaAI)
        try:
            with open(f"{LogPath}/Log.txt", 'a') as log:
                print(crash_logo)
                print(f"[$] System Error | {error}")
                TM = time.strftime("[%a %b %d %H:%M:%S] ")
                log.write(TM)
                log.write(error)
                log.close()
                time.sleep(6)
                crash().CloseSYS()

        except Exception as error:
            print(NovaAI)
            print(f"[$] System Error | {error}")

    def CloseSYS(self):
        print("Nexus > To prevent any more issues the system will close now !")
        print("If you keep having issues please contact support on GitHub.")
        time.sleep(4)
        sys.exit()


