from Placeholders import check_help
from Placeholders import console_help



class SimpleMode():

    def Console(self):
        print("Simple Mode enabled | NovaOS Technology | Please enter a command below")
        while True:
            user = input("> ")
            if user in check_help:
                print(console_help)
            elif user == 'v':
                print("Unknown Command | Try 'V'")
            elif user == 'V':
                print("Usage: V -attack <Attack Type>")
            elif user == 'V -attack test':
                print("Attack Found | Starting Attack")
                break
