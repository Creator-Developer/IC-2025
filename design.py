from colorama import Fore
import os
import sys
import time

# Colors
blue = Fore.BLUE
magenta = Fore.MAGENTA
red = Fore.RED
cyan = Fore.CYAN
green = Fore.GREEN

# CMD func
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def ExitError(type:str, message:str):
    clear()
    print(f"{red}[{type}] {message}{red}")
    sys.exit()
def Error(type:str, message:str):
    clear()
    print(f"{red}[{type}] {message}{red}")
    time.sleep(2)

# Banner

github = 'github.com/Creator-Developer'

banner = f'''
{blue}██╗ ██████╗              ██████╗  ██████╗ ██████╗ ███████╗
{cyan}██║██╔════╝              ╚════██╗██╔═████╗╚════██╗██╔════╝
{blue}██║██║         █████╗     █████╔╝██║██╔██║ █████╔╝███████╗
{cyan}██║██║         ╚════╝    ██╔═══╝ ████╔╝██║██╔═══╝ ╚════██║
{blue}██║╚██████╗              ███████╗╚██████╔╝███████╗███████║
{cyan}╚═╝ ╚═════╝              ╚══════╝ ╚═════╝ ╚══════╝╚══════╝
{magenta}              {github}'''

# Functions

o1_no_formated = 'Create installator'
o2_no_formated = 'Info'
o3_no_formated = 'GitHub'
o4_no_formated = 'Exit'
o5_no_formated = 'SOON'

option_1 = f'{cyan}[{blue}1{cyan}] {blue}{o1_no_formated}'
option_2 = f'{cyan}[{blue}2{cyan}] {blue}{o2_no_formated}'
option_3 = f'{cyan}[{blue}3{cyan}] {blue}{o3_no_formated}'
option_4 = f'{cyan}[{blue}4{cyan}] {blue}{o4_no_formated}'
option_5 = f'{cyan}[{blue}5{cyan}] {blue}{o5_no_formated}'

# Testing

def test():
    clear()
    print(banner)
    print(option_1)
    print(option_2)
    print(option_3)
    print(option_4)
    print(option_5)

