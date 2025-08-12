from design import *
from gitcommand import *
import webbrowser
import sys
import os

def file_write(text, file):
    """
    Zapisuje podany tekst do pliku.
    """
    if not os.path.exists('output'):
        os.makedirs('output')
    with open(f'output/{file}', 'w') as f:
        f.write(text)

clear()

info = f'''
{cyan}Program name{blue}:    IC - 2025
{cyan}Program version{blue}: v1.0

{cyan}Author{blue}:          Creator-Developer'''

t = True
while t:
    clear()
    print(banner, '\n')
    print(option_1)
    print(option_2)
    print(option_3)
    print(option_4)
    
    try:
        select = int(input(f'\n{cyan}Select option {blue}[{magenta}int{blue}]{cyan}: {green}'))
    except ValueError:
        Error('Error', 'Invalid input. Please enter a number.')
        continue
    
    clear()
    
    if select == 1:
        os_func = []
        repo_name = input(f'\n{cyan}Enter (full) repository name {blue}[{magenta}str{blue}]: {green}')
        github_link = generate(repo_name)
        
        dywtaamc = input(f'\n{cyan}Do you want to add any more commands {blue}[{magenta}y/n{blue}]: {green}')
        if dywtaamc.lower() == 'y':
            try:
                hm = int(input(f'{cyan}How many functions do you want to add {blue}[{magenta}int{blue}]: {green}'))
                for i in range(hm):
                    os_func.append(input(f'\n{cyan}Enter command {blue}[{magenta}str{blue}]: {green}'))
            except ValueError:
                Error('Error', 'Invalid number of commands. Skipping additional commands.')
                os_func = []
        
        # Generowanie treści pliku instalatora
        installer_commands = "\\n".join([f"os.system('{cmd}')" for cmd in os_func])
        installer_content = f"""
import os
import time

print('Starting instalation')
time.sleep(1)

# Repo clonning
os.system('{github_link}')
print('Files downloaded...')
time.sleep(1)

{installer_commands}

print('Instalation complete!')
"""
        # Poprawiona linia - zastępujemy "/" w nazwie repozytorium znakiem "-", 
        # aby uniknąć błędów w nazwie pliku.
        sanitized_repo_name = repo_name.replace('/', '-')
        file_write(installer_content, f'install-{sanitized_repo_name}.py')
        print(f'{green}Instalator file "install-{sanitized_repo_name}.py" was created in folder "output".')
        input(f'\n{blue}Press enter to continue')
        x = input(f'{cyan}Do you want to create exe? {blue}[{magenta}y/n{blue}]: {green}')
        if x.lower() == 'y':
            os.system('pyinstaller --onefile output/install-' + sanitized_repo_name + '.py')
            print(f'{green}Exe file was created in folder "dist".')
        elif x.lower() == 'n':
            continue
    elif select == 2:
        print(info)
        input(f'\n{blue}Press enter to continue')
    elif select == 3:
        webbrowser.open(github, new=2)
    elif select == 4:
        sys.exit()
    elif select == 5:
        print(f'{magenta}This feature is coming soon!')
        input(f'\n{blue}Press enter to continue')
    else:

        Error('Error', 'Invalid option selected.')
