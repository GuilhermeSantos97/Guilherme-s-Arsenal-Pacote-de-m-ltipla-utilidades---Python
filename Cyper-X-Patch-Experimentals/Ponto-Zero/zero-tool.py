import sys,os
from colorama import Fore

print(Fore.MAGENTA+"""

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――                       
        .                  .     ______           _               ______                          .
                  .              | ___ \         | |             |___  /                  .
      .                    .     | |_/ /__  _ __ | |_ ___  ______    / /  ___ _ __ ___          .
                                 |  __/ _ \| '_ \| __/ _ \ ______   / /  / _ \ '__/ _ \              .
                   .             | | | (_) | | | | || (_) |       / /__ |  __/| |  (_) |    .
         .                       \_|  \___/|_| |_|\__\___/       \_____/\___  |_| \___/          .
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
                                                                 
BY: Guilherme Santos (Experimental Tool)
""")

def display_menu():
    print(Fore.YELLOW + """
                            ―――――――――――――――――――――――――――――――――――――――――――――――――――――――
                            1. Ip-Scanner                   | 7.  Sub-Dominio-Scanner      
                            2. Discord-Nuke/Tsar            | 8.  FERRAMENTA-DDOS
                            3. Subdirectory-Scanner         | 9.  Discord-Token-Grabber
                            4. Email-Boomber                | 10. Keylogger(Chave para logar)
                            5. Phone-Locator                | 11. Web-Crawler
                            6. Port-Scanner                 | 12. Reverse-Shell 
                            ――――――――――――――――――――――――――――――――――――――――――――――――――――――――
          
    """)

#definição para executar um comando
def execute_command(command):
    if command == '1':
        os.system('cmd /k "python Zero-Tool/ip-lookup.py"' if os.name == 'nt' else 'python Zero-Tool/ip-lookup.py')

    elif command == '2':
        os.system('cmd /k "python Zero-Tool/nuke-bot/main.py"' if os.name == 'nt' else 'python Zero-Tool/nuke-bot/main.py')

    elif command == '3':
        os.system('cmd /k "python Zero-Tool/Subdirectory-scanner/main.py"' if os.name == 'nt' else 'python Zero-Tool/Subdirectory-scanner/main.py')

    elif command == '4':
        os.system('cmd /k "python Zero-Tool/email-bomber.py"' if os.name == 'nt' else 'python Zero-Tool/email-bomber.py')

    elif command == '5':
        os.system('cmd /k "python Zero-Tool/phone-locator.py"' if os.name == 'nt' else 'python Zero-Tool/phone-locator.py')

    
    elif command == '6':
        os.system('cmd /k "python Zero-Tool/port-scanner.py"' if os.name == 'nt' else 'python Zero-Tool/port-scanner.py"')

    
    elif command == '7':
        os.system('cmd /k "python Zero-Tool/subdomain/main.py"' if os.name == 'nt' else 'python Zero-Tool/subdomain/main.py')

    
    elif command == '8':
        os.system('cmd /k "python .\Ponto-Zero\ddos.py"' if os.name == 'nt' else 'python .\Ponto-Zero\ddos.py')
    
    
    elif command == '9':
        os.system('cmd /k "python .\discord-token-grabber.py"' if os.name == 'nt' else 'python Zero-Tool/discord-token-grabber.py')
    
    
    elif command == '10':
        print(Fore.RED + 'This option is not available yet! Coming soon...')
        #os.system('cmd /k "python Zero-Tool/Keylogger.py"')
    
    elif command == '11':
        print(Fore.RED + 'This option is not available yet! Coming soon...')
        #os.system('cmd /k "python Zero-Tool/Web-Crawler.py"')
    
    
    elif command == '12':
        print(Fore.RED + 'This option is not available yet! Coming soon...')
        #os.system('cmd /k "python Zero-Tool/Reverse-Shell.py"')
    
    
    else:
        print(Fore.RED + 'Invalid option! Please choose the correct one.')

while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)
