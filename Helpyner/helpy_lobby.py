import os,time
import random
import platform

from colorama import Fore,init
from win10toast import ToastNotifier


# inicializa o colorama
init()

#Criando uma váriavel chamada de "toast"
toast = ToastNotifier()



#Variavel da Menssagem 1
msg = (Fore.RED+""""
                    
                          ⣀⣀⣤⣤⣤⣤⡼⠀⢀⡀  ⢱⡄⡀⠀⠀⠀⢲⣤⣤⣤⣤⣀⣀⡀
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
 """) 


menssagem2 = [Fore.RED + "Tip: Não use Softwares pitaras!", "Tip: Seja bem vindo Guerreiro", "Tip: Você sabia que esse software está sendo desenvolvido a mais de 1 mês e meio?",
              "Tip: Qualquer dúvida, veja na opção > 2 Info (Contato DEV)",
              "Tip: O pai tá On!!!"]   

for i in range(1):
    msg2 = random.choice(menssagem2) # Variavel msg vai definer as "menssagens" dentro do parentese.
    time.sleep(3)


toast.show_toast(
    "Helpyner Service", #Nome da notificação
    f"Bem-vindo(a) ao Helpyner {platform.node()}", #Corpo da notificação
    duration = 10, #Duração
    icon_path = "images.png", #Icone
    threaded = True, 
)


#aqui ele irá printar as váriaveis
print(msg + msg2)

#def -> Criar uma função
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
        print(Fore.BLUE + """"
              
/// ╔═══════════════════════════════════════════════════════════════════════╗
/// ║    ██╗                        ██╗  ██╗ ██████╗ ██╗  ██╗               ║
/// ║██╗██╔╝                        ██║  ██║██╔═████╗██║  ██║               ║
/// ║╚═╝██║                         ███████║██║██╔██║███████║               ║
/// ║██╗██║                         ╚════██║████╔╝██║╚════██║               ║
/// ║╚═╝╚██╗                             ██║╚██████╔╝     ██║               ║
/// ║    ╚═╝                             ╚═╝ ╚═════╝      ╚═╝               ║
/// ║                                                                       ║
/// ║                                                                       ║
/// ║                                                                       ║
/// ║          "Opção Errada! Por favor selecione a opção Certa!!!"         ║
/// ╚═══════════════════════════════════════════════════════════════════════╝ """)

while True:
    display_menu()
    command = input(Fore.RED + 'Helpyner> ')

    if command.lower() == 'sair':
       break

    execute_command(command)
