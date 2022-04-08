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
from mcstatus import JavaServer

init()

# Colors

red = Fore.RED
lred = Fore.LIGHTRED_EX
black = Fore.BLACK
lblack = Fore.LIGHTBLACK_EX
white = Fore.WHITE
lwhite = Fore.LIGHTWHITE_EX
green = Fore.GREEN
lgreen = Fore.LIGHTGREEN_EX
cyan = Fore.CYAN
lcyan = Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lmagenta = Fore.LIGHTMAGENTA_EX
yellow = Fore.YELLOW
lyellow = Fore.LIGHTYELLOW_EX
blue = Fore.BLUE
lblue = Fore.LIGHTBLUE_EX
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
 \_| \_| \____/_| |_|\___|\___|_|\_\___|_|   {lgreen}v1.2

 {white}Created by {lcyan}@wrrulos
{reset}"""


def check_connection():
    """ Check if you have an internet connection """
    try:
        socket.gethostbyname("google.com")
        return True

    except:
        print(" You need to be connected to the internet")
        return False


def check_file():
    """ Check file """
    if os.path.exists(file):
        return True

    print(" File not found!")
    return False


def check_timeout():
    """ Check file """
    if str(timeout).isdecimal():
        return True

    print(" Please enter a valid timeout value!")
    return False


def replace_text(text):
    """ Replace the text """
    if "§0" in text:
        text = text.replace("§0", "{}".format(lblack))

    if "§1" in text:
        text = text.replace("§1", "{}".format(blue))

    if "§2" in text:
        text = text.replace("§2", "{}".format(lgreen))

    if "§3" in text:
        text = text.replace("§3", "{}".format(cyan))

    if "§4" in text:
        text = text.replace("§4", "{}".format(red))

    if "§5" in text:
        text = text.replace("§5", "{}".format(magenta))

    if "§6" in text:
        text = text.replace("§6", "{}".format(yellow))

    if "§7" in text:
        text = text.replace("§7", "{}".format(lblack))

    if "§8" in text:
        text = text.replace("§8", "{}".format(lblack))

    if "§9" in text:
        text = text.replace("§9", "{}".format(lblue))

    if "§a" in text:
        text = text.replace("§a", "{}".format(lgreen))

    if "§b" in text:
        text = text.replace("§b", "{}".format(lcyan))

    if "§c" in text:
        text = text.replace("§c", "{}".format(lred))

    if "§d" in text:
        text = text.replace("§d", "{}".format(lmagenta))

    if "§e" in text:
        text = text.replace("§e", "{}".format(lyellow))

    if "§f" in text:
        text = text.replace("§f", "{}".format(white))

    if "§k" in text or "§l" in text or "§m" in text or "§n" in text or "§o" in text or "§r" in text:
        text = text.replace("§k", "").replace("§l", "").replace("§m", "").replace("§n", "").replace("§o", "").replace("§r", "")

    if "\n" in text:
        text = text.replace("\n", "")

    text = re.sub(" +", " ", text)
    return text


def checker():
    global ips

    if not logs_file:
        date = datetime.now()
        log_file = f"RChecker_{str(date.day)}-{str(date.month)}-{str(date.year)}_{str(date.hour)}.{str(date.minute)}.{str(date.second)}.txt"

        f = open(log_file, "w+")
        f.write(f"RChecker by @wrrulos \nFile: {file}\n\n")

    os.system("cls || clear")
    print(scan_banner)

    f_ = open(file, "r", encoding="utf8")
    content = f_.read()
    f_.close()

    if "Nmap scan report for" in content:
        nmap_file = True

    else:
        nmap_file = False

    if nmap_file:
        with open(file, encoding="utf8") as nmap_result:
            for line in nmap_result:
                ip = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
                ip = " ".join(ip)
                ip = ip.replace("(", "").replace(")", "")
                port = re.findall("\d{1,5}\/tcp open", line)
                port = " ".join(port)

                if "." in ip:
                    ip_current = ip

                if "tcp" in port:
                    port = port.replace("/tcp open", "")
                    ip_current_backup = ip_current

                    try:
                        ip_current = ip_current.split(" ")
                        ip_current = ip_current[1]

                    except:
                        ip_current = ip_current_backup

                    ips.append(f"{ip_current}:{port}")

    else:
        with open(file, encoding="utf8") as results:
            for line in results:
                ip = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{1,5}", line)
                ip = " ".join(ip)
                if ":" in ip:
                    ips.append(f"{ip}")

    if len(ips) == 0:
        print(f" No IP addresses found in the file")
        exit()

    for ip in ips:
        try:
            srv = JavaServer.lookup(ip)
            response = srv.status()
            motd = replace_text(response.description)
            motd_ = response.description.replace('§1', '').replace('§2', '').replace('§3', '').replace('§4', '').replace('§5', '').replace('§6', '').replace('§7', '').replace('§8', '').replace('§9', '').replace('§0', '').replace('§a', '').replace('§b', '').replace('§c', '').replace('§d', '').replace('§e', '').replace('§f', '').replace('§k', '').replace('§l', '').replace('§m', '').replace('§n', '').replace('§o', '').replace('§r', '').replace('\n', '')
            motd_ = re.sub(" +", " ", motd_)
            version = replace_text(response.version.name)
            version_ = response.version.name.replace('§1', '').replace('§2', '').replace('§3', '').replace('§4', '').replace('§5', '').replace('§6', '').replace('§7', '').replace('§8', '').replace('§9', '').replace('§0', '').replace('§a', '').replace('§b', '').replace('§c', '').replace('§d', '').replace('§e', '').replace('§f', '').replace('§k', '').replace('§l', '').replace('§m', '').replace('§n', '').replace('§o', '').replace('§r', '').replace('\n', '')
            version_ = re.sub(" +", " ", version_)

            if not logs_file:
                f.write(f"({ip}) (Version: {version_}) ({response.players.online}/{response.players.max}) ({motd_})\n")

            print(f" {white}({lmagenta}{ip}{white}) ({lgreen}Version: {green}{version}{white}) ({lyellow}{response.players.online}/{response.players.max}{white}) ({motd})")

        except KeyboardInterrupt:
            exit()

        except socket.timeout:
            if not logs_file:
                f.write(f"({ip[0]}:{ip[1]}) (timeout)\n")

            print(f" {white}({lmagenta}{ip}{white}) ({lred}timeout{white})")

        except:
            pass

    if not logs_file:
        f.close()


def check_arguments():
    """ Check the arguments """
    global file
    global logs_file
    global timeout

    parser = ArgumentParser()
    parser.add_argument("-f", help="File name", required=True, action="store", dest="file")
    parser.add_argument("--timeout", help="Server ping timeout (default is 2)", default="2", dest="timeout", action="store")
    parser.add_argument("--no-output", help="Prevents RChecker from saving the results to a text file", default=False, dest="logs_file", action="store_true")
    args = parser.parse_args()

    file = args.file
    logs_file = args.logs_file
    timeout = args.timeout


def main():
    print(banner)
    check_arguments()
    check__file = check_file()

    if check__file:
        check__timeout = check_timeout()
        if check__timeout:
            check__connection = check_connection()
            if check__connection:
                checker()


if __name__ == "__main__":
    main()
