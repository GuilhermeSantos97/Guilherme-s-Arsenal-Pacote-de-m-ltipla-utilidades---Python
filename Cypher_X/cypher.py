import sys, time, os
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
                    
""" + Fore.RESET)

# Aqui será uma pequena animação de texto usando o loop "for".

print(menssagem1)
    

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

    # Os dois "==" são definidos como resposta.
    # Aqui ele abrirá um arquivo diretamente do diretório!
    if command == '1':
        os.system('cmd /k "python Cypher_X/Ponto_zero/zero-tool.py"' if os.name == 'nt' else 'python Cypher_X/Ponto_zero/zero-tool.py')
        

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
        print('Opção Inválida! Seleciona uma correta.')

while True:
    display_menu()
    command = input(Fore.GREEN + 'CypherX > ')

    if command.lower() == 'exit':
        break

    execute_command(command)
