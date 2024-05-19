import os
import random
import json

from colorama import Fore,init
from pystyle import Colorate, Colors


# inicializa o colorama & pystyle
init()

# Criando uma váriavel chamada de "toast"
# "notificação" vai inicializar com a responta do "=" o ToastNotifier()


#Variavel da Menssagem 1
titulo = ("""
                    
                
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
          version: 1.9.1
            -----------------------------------------------------------------
        """) 

titulo = Colorate.Horizontal(Colors.red_to_yellow, titulo)

menssagem2 = [Fore.RED + "Tip: Não use Softwares pitaras!", Fore.RED + "Tip: Você sabia que esse software está sendo desenvolvido a mais de 1 mês e meio?", Fore.RED +
              "Tip: Qualquer dúvida, veja na opção > 2 Info (Contato DEV)", Fore.RED +
              "Tip: O pai tá On!!!", "Tip: Quer  ver novos aprimoramentos? Veja no gitHub Oficial!"]   


# Aqui terá um loop para cada menssagem dentro da váriavel menssagem2.
# variavel msg responsvel por gurdar as informações da  "menssagem2"
for i in range(31):
    msg = random.choice(menssagem2) # Variavel msg vai definer as "menssagens" dentro do parentese.



# Print!
#aqui ele irá printar as váriaveis
print(titulo + msg)

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
        

# def notificacao():
# # Configurações gerais de notificação.
#     notificação.toast(
#     "Helpyner Service", #Nome da notificação
#     f"Bem-vindo(a) ao Helpyner {os.environ.get('USERNAME')}", #Corpo da notificação. Ele exibirá o seu nome como uma forma dinâmica.
#     duration = 6, #Duração 
#     threaded = True, # Valor definido como Verdadeiro.
#     )

while True:
                     # titulo da ferramenta
    display_menu() # Menu Display da ferramenta
    comando = input(Fore.RED + 'Helpyner> ')

    if comando.lower() == 'sair':
       break

    execute_command(comando)
