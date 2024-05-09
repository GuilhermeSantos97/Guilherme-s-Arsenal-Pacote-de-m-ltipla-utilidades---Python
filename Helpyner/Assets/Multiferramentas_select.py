import os
from colorama import Fore, init

# Inicializa o colorama
init()


def display_menu():
    print(Fore.MAGENTA + """
 _____________________________________________________________________________________
|---------------------――――> ESCOLHA UMA OPÇÃO QUE DESEJA  <――――-------------------- |
|                                                                                   |
|   [1]: Removedor De Fundo da Imagem.    |   [3]: Pegar a posição do mouse         |
|   [2]: Organizador De Aqrquivos.        |   [4]: Sobre o meu Pc                   |
|                                                                                   |   
|―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――| 
          
""" + Fore.RESET)
    
    

#   Aqui ele vai executar um comando atravez de um número
def execute_command(command):

    #Os dois "==" são definidos como resposta.
    if command == '1':
        os.system('cmd /k "python Helpyner_Multiferramentas _(Extras)/removedorDeFundo_Imagens.py"' if os.name == 'nt' else 'python Helpyner_Multiferramentas _(Extras)/removedorDeFundo_Imagens.py')
    elif command == '2':
        os.system('cmd /k "python Helpyner Helpyner_Multiferramentas _(Extras)/main_organizador.py"' if os.name == 'nt' else 'python Helpyner_Multiferramentas _(Extras)/main_organizador.py')
    elif command == '3': 
        os.system('cmd /k "python Helpyner_Multiferramentas _(Extras)/pegar_posicao.py"' if os.name == 'nt' else 'python Helpyner_Multiferramentas _(Extras)/pegar_posicao.py')
    elif command == '4':
        os.system('cmd /k "python Helpyner_Multiferramentas _(Extras)/sobre_meu_pc.py"' if os.name == 'nt' else 'python Helpyner_Multiferramentas _(Extras)/sobre_meu_pc.py')
    else:
        print('Opção invalida! Por favor use a opção certa.')

while True:
    display_menu()
    command = input(Fore.RED + 'Helpyner> ')

    if command.lower() == 'sair':
       break

    execute_command(command)