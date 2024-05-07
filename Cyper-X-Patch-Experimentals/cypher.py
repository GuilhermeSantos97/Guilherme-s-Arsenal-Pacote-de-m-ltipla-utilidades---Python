import sys, time, os
import pygame
from colorama import Fore, init

# Inicializa o colorama
init()

menssagem1 = (Fore.GREEN+"""

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
                    ░█████╗░██╗░░░██╗██████╗░██╗░░██╗███████╗██████╗░  ░░░░░░  ██╗░░██╗ beta 1.2.2
                    ██╔══██╗╚██╗░██╔╝██╔══██╗██║░░██║██╔════╝██╔══██╗  ░░░░░░  ╚██╗██╔╝
                    ██║░░╚═╝░╚████╔╝░██████╔╝███████║█████╗░░██████╔╝  █████╗  ░╚███╔╝░
                    ██║░░██╗░░╚██╔╝░░██╔═══╝░██╔══██║██╔══╝░░██╔══██╗  ╚════╝  ░██╔██╗░
                    ╚█████╔╝░░░██║░░░██║░░░░░██║░░██║███████╗██║░░██║  ░░░░░░  ██╔╝╚██╗
                    ░╚════╝░░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ░░░░░░  ╚═╝░░╚═╝
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
                    
""")

for char in menssagem1: 
    # pygame.mixer.music.load('Som.wav')
    # pygame.mixer.music.play()
    sys.stdout.write (char) 
    sys.stdout.flush() 
    time.sleep (0.1)




menssagem2 = "BY: Guilherme Santos"

for char in menssagem2: 
    sys.stdout.write (char) 
    sys.stdout.flush()  
    time.sleep (0.1)


#def é uma definição na qual você pode definir um objeto.
#Exemplos def display_menu(ele está definindo o "display_menu" )
def display_menu():
    print(Fore.MAGENTA + """
    ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
                    ----------------->  MENU PRINCIPAL  <-----------------------
          
    1: Ferramentas CyperX (Hacking Tools)      |    3: Ponto-Zero-Configs (Ultra)
    2: Info (Contato DEV)                      |    4: Rota das Conquistas (Achievement System)
          
    ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
          
    """ + Fore.RESET)


# Definição para executar um comando
def execute_command(command):

    #Os dois "==" são definidos como resposta.
    if command == '1':
        os.system('cmd /k "python /Ponto-Zero/zero-tool.py"' if os.name == 'nt' else 'python .\Ponto-Zero\zero-tool.py')
        

# Opção 2 (Contato DEV)
    elif command == '2':
        os.system('cmd /k "python info.py"' if os.name == 'nt' else 'python info.py')

        display_menu()


    elif command == '3':
        print(Fore.RED + 'Em breve...')
        #os.system('cmd /k "python Zero-Web-Hacktool/web_bugger.py"')


    elif command == '4':
        print(Fore.ORANGE + 'Em breve')

    else:
        print('Invalid option! Please choose the correct one.')

while True:
    display_menu()
    command = input('CypherX> ')

    if command.lower() == 'exit':
        break

    execute_command(command)
