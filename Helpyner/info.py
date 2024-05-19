# Importação das bibliotecas!
import sys, time
import pyautogui
from colorama import Fore, init


# Inicializa o colorama.
init()

# Definir a pausa do pyautogui. Ir mais rapido sem travamentos
pyautogui.PAUSE = 0.5

#Variaveis "Info1" e "info2" serão as reponsáveis por exibir textos na tela do espectador.
info = (Fore.GREEN + """

         
git clone https://github.com/GuilhermeSantos97
Instagram https://www.instagram.com/_gordon_.g/
Facebook https://www.facebook.com/guilherme.Santos.Oficial97
Discord hey_ronak
""" + Fore.RESET)


#info2 é uma variável
info2 = (Fore.RED + """     
-- Santos Solutions --
Programa destinado para ajudar e corrigir o seu PC!
Helpyner agradeçe seu apoio!


Licença
Helpyner 2024 Licença
""" + Fore.RESET)

# Aqui ele irá fazer uma animação de typerWrite atravez de uma variavel "info". vc pode acionar outras variaveis.
for char in info: 
    sys.stdout.write (char) 
    sys.stdout.flush() 
    time.sleep (0.1)


for char in info2: 
    # pygame.mixer.music.load('Som.wav')
    # pygame.mixer.music.play()
    sys.stdout.write (char) 
    sys.stdout.flush() 
    time.sleep (0.1)

# Display menu do usuario
def display_menu():
    print(Fore.CYAN + """
    ―――――――――――――――――――――――――――――――――――――――――――――――――――――     
    |     [1]: GitHub                                   |    
    |     [2]: Facebook                                 |
    |     [3]: Discord                                  |
    |     [4]: Instagram                                | 
    ―――――――――――――――――――――――――――――――――――――――――――――――――――――  """ + Fore.RESET)

    #   Aqui ele vai executar um comando atravez de um número
def execute_command(command):

    # Área De comandos
    #Os dois "==" são definidos como resposta.
    #GitHub Diretório
    if command == '1':
        pyautogui.press("win")
        pyautogui.write("chrome")
        pyautogui.press("enter")
        pyautogui.write("https://github.com/GuilhermeSantos97")
        pyautogui.press("enter")
        time.sleep(3)
#Facebook diretório
    elif command == '2':
        pyautogui.press("win")
        pyautogui.write("chrome")
        pyautogui.press("enter")
        pyautogui.write("https://www.facebook.com/guilherme.Santos.Oficial97")
        pyautogui.press("enter")
        time.sleep(3)

    elif command == '3':
        pyautogui.press("win")
        pyautogui.write("chrome")
        pyautogui.press("enter")
        pyautogui.write("https://discord.com/channels/@me")
        pyautogui.press("enter")
        pyautogui.click(x=1316, y=223)
        pyautogui.write("hey_ronak")
        time.sleep(3)


    elif command == '4':
        pyautogui.press("win")
        pyautogui.write("chrome")
        pyautogui.press("enter")
        pyautogui.write("https://www.instagram.com/_gordon_.g/")
        pyautogui.press("enter")
        time.sleep(3)
        
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

