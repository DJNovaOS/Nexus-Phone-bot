import getpass
import time

class FLogin:
    def login(self):
        print("Force Login is enabled")
        username = input("Username: ")
        print("Username logged")
        password = getpass.getpass("Password: ")

        if username and password == "Admin":
            print("You have logged in")
            time.sleep(5)