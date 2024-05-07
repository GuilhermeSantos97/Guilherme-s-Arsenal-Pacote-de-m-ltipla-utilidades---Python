import os 
import random

from colorama import Fore,init

# inicializa o colorama
init()

#Variavel da Menssagem 1
menssagem1 = (Fore.RED+"""
                    
                          ⣀⣀⣤⣤⣤⣤⡼⠀⢀⡀   ⢱⡄⡀⠀⠀⠀⢲⣤⣤⣤⣤⣀⣀⡀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀
            ⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄⠀
            ⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄
            -----------------------------------------------------------------              
                             _    _      _                             
                            | |  | |    | |                            
                            | |__| | ___| |_ __  _   _ _ __   ___ _ __ 
                            |  __  |/ _ \ | '_ \| | | | '_ \ / _ \ '__|
                            | |  | |  __/ | |_) | |_| | | | |  __/ |   
                            |_|  |_|\___|_| .__/ \__, |_| |_|\___|_|   
                                          | |     __/ |                
                                          |_|    |___/     
                              
          By: Guilherme Santos
          version: 1.17.1
            -----------------------------------------------------------------
 """ + Fore.RESET)                            



print(menssagem1)


def display_menu():
    print(Fore.GREEN + """
    ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
              -----------------> ESCOLHA UMA OPÇÃO QUE DESEJA  <-----------------
          
    > 1: Ferramentas De Reparo                |    > 3: Scan (Programas mal-Intecionados)
    > 2: Info (Contato DEV)                   |    > 4: MultiFerramentas Helpyner(Extras) 
    ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――  """)
    
    

#   Aqui ele vai executar um comando atravez de um número
def execute_command(command):

    #Os dois "==" são definidos como resposta.
    if command == '1':
        os.system('cmd /k "python ."' if os.name == 'nt' else 'python .')
    elif command == '2':
        os.system('cmd /k "python info.py"' if os.name == 'nt' else 'python info.py')
    elif command == '3': 
        os.system('cmd /k "python ."' if os.name == 'nt' else 'python .')
    elif command == '4':
        os.system('cmd /k "python Assets/Multiferramentas_select.py"' if os.name == 'nt' else 'python Assets/Multiferramentas_select.py')
    else:
        print('Opção invalida! Por favor use a opção certa.')

while True:
    display_menu()
    command = input(Fore.RED + 'Helpyner> ')

    if command.lower() == 'sair':
       break

    execute_command(command)