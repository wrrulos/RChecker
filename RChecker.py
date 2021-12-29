# =============================================================================
#                     RChecker www.github.com/wrrulos
#                      Checker for Minecraft Servers
#                            Made by wRRulos
#                               @wrrulos
# =============================================================================

# Any error report it to my discord please, thank you.
# Programmed in Python 3.10.1
# Discord: Rulo#9224


import os
import re
import socket

from datetime import datetime
from argparse import ArgumentParser
from colorama import Fore, init

init()

# Colors

red = Fore.RED
lred = Fore.LIGHTRED_EX
black = Fore.BLACK
lblack = Fore.LIGHTBLACK_EX
white = Fore.WHITE
green = Fore.GREEN
lgreen = Fore.LIGHTGREEN_EX
lcyan = Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lmagenta = Fore.LIGHTMAGENTA_EX
yellow = Fore.YELLOW
lyellow = Fore.LIGHTYELLOW_EX
reset = Fore.RESET

file = ""
ips = []
logs_file = ""
timeout = 0

banner = f"""{lmagenta}
 ______  _____ _               _             
 | ___ \/  __ \ |             | |            
 | |_/ /| /  \/ |__   ___  ___| | _____ _ __ 
 |    / | |   | '_ \ / _ \/ __| |/ / _ \ '__|
 | |\ \ | \__/\ | | |  __/ (__|   <  __/ |   
 \_| \_| \____/_| |_|\___|\___|_|\_\___|_|   
                                          
{reset}"""

scan_banner = f"""{lmagenta}
 ______  _____ _               _             
 | ___ \/  __ \ |             | |            
 | |_/ /| /  \/ |__   ___  ___| | _____ _ __ 
 |    / | |   | '_ \ / _ \/ __| |/ / _ \ '__|
 | |\ \ | \__/\ | | |  __/ (__|   <  __/ |   
 \_| \_| \____/_| |_|\___|\___|_|\_\___|_|   {lgreen}v1.0
 
 {white}Created by {lcyan}@wrrulos
{reset}"""


def clear():
    """
    Clean the screen
    """
    if os.name == "nt":
        os.system("cls")

    else:
        os.system("clear")


def check_connection():
    """
    Check if you have an internet connection
    """
    try:
        socket.gethostbyname("google.com")

    except:
        print(" You need to be connected to the internet")
        exit()


def check_file():
    """
    Check file
    """
    if os.path.exists(file):
        pass

    else:
        print(" File not found!")
        exit()


def checker():
    global ips

    if not logs_file:
        date = datetime.now()
        log_file = f"RChecker_{str(date.day)}-{str(date.month)}-{str(date.year)}_{str(date.hour)}.{str(date.minute)}.{str(date.second)}.txt"

        f = open(log_file, "w+")
        f.write(f"RChecker by @wrrulos \nFile: {file}\n\n")

    clear()
    print(scan_banner)

    with open(file, encoding="utf8") as qubo_result:
        for line in qubo_result:
            ip = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{1,5}", line)
            ip = " ".join(ip)
            if ":" in ip:
                ips.append(f"{ip}")

    for ip in ips:
        ip = ip.split(":")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(int(timeout))
            s.connect((ip[0], int(ip[1])))
            s.send(b"\xfe\x01")
            data = s.recv(1024)[3:].decode("utf-16be")[3:].split("\x00")
            s.close()

            version = re.sub(r"§[a-zA-Z0-9]", "", data[1].strip().replace("  ", "").replace("  ", ""))
            motd = re.sub(r"§[a-zA-Z0-9]", "", data[2].strip().replace("  ", "").replace("  ", ""))
            players = re.sub(r"§[a-zA-Z0-9]", "", f"{data[3]}/{data[4]}".strip().replace("  ", "").replace("  ", ""))

            motd = motd.replace("\n", "")

            if not logs_file:
                f.write(f"({ip[0]}:{ip[1]}) (Version: {version}) ({players}) ({motd})\n")

            print(f" {white}({lmagenta}{ip[0]}:{ip[1]}{white}) ({lgreen}Version: {green}{version}{white}) ({lyellow}{players}{white}) ({lcyan}{motd}){white})")

        except socket.timeout:
            if not logs_file:
                f.write(f"({ip[0]}:{ip[1]}) (timeout)\n")

            print(f" {white}({lmagenta}{ip[0]}:{ip[1]}{white}) ({lred}timeout{white})")

        except:
            pass

    if not logs_file:
        f.close()


def check_arguments():
    """
    Check the arguments
    """
    global file
    global logs_file
    global timeout

    parser = ArgumentParser()
    parser.add_argument("-f", help="File name", required=True, action="store", dest="file")
    parser.add_argument("--timeout", help="Server ping timeout (default is 2)", default=2, dest="timeout", action="store")
    parser.add_argument("--no-output", help="Prevents RChecker from saving the results to a text file", default=False, dest="logs_file", action="store_true")
    args = parser.parse_args()

    file = args.file
    logs_file = args.logs_file
    timeout = args.timeout

    print(logs_file)


def main():
    print(banner)
    check_os()
    check_arguments()
    check_file()
    checker()


if __name__ == "__main__":
    main()