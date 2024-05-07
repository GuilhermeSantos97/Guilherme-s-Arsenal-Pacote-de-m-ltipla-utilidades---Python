import os
from colorama import Fore, init

# Inicializa o colorama
init()


def display_menu():
    print(Fore.MAGENTA + """
                    _____________________________________________________________________________________
                    |---------------------――――> ESCOLHA UMA OPÇÃO QUE DESEJA  <――――-------------------- |
                    |                                                                                   |
                    |                     > 1: Removedor De Fundo da Imagem                             |
                    |                     > 2: Organizador De Aqrquivos                                 |
                    |                                                                                   |   
                    |―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――| 
""" + Fore.RESET)
    
    

#   Aqui ele vai executar um comando atravez de um número
def execute_command(command):

    #Os dois "==" são definidos como resposta.
    if command == '1':
        os.system('cmd /k "python Helpyner Multiferramentas (Extras)/removedorDeFundo_Imagens"' if os.name == 'nt' else 'python Helpyner Multiferramentas (Extras)/removedorDeFundo_Imagens')
    elif command == '2':
        os.system('cmd /k "python info.py"' if os.name == 'nt' else 'python info.py')
    elif command == '3': 
        os.system('cmd /k "python ."' if os.name == 'nt' else 'python .')
    elif command == '4':
        os.system('cmd /k "python Assets/main_organizador.py"' if os.name == 'nt' else 'python Assets/main_organizador.py')
    else:
        print('Opção invalida! Por favor use a opção certa.')

while True:
    display_menu()
    command = input(Fore.RED + 'Helpyner> ')

    if command.lower() == 'sair':
       break

    execute_command(command)