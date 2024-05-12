#Importações Das Bibliotecas
import platform
import sys
from colorama import Fore, init

#inicializa o colorama
init()

# Aqui ele exibirá entre as chaves o nome da rede do Computador. com o comando
# node ->
print(Fore.CYAN + f"Nome Computador é: {platform.node()}\n" +
                  f"Sua Máquina é: {platform.machine()}\n" +
                  f"Seu Processador é: {platform.processor()}\n" +
                  f"Seu Sistema Operacional é: {platform.system()}\n" +
                  f"Seu sistema geral: {platform.win32_ver(release='', version='', csd='', ptype='')}\n" + 
                  f"Plataforma De Arquitetura é: {platform.architecture(executable=sys.executable, bits='')}\n"                
             """  ⠀
                   ⢰⠉⢷⠒⠒⠒⠒⠒⠒⠒⠒⣺⠉⡆⠀⠀
                ⠀⠀ ⠀⢧⠘⢦⣀⣀⣀⣀⣀⣀⡰⠃⡸⠁⠀⠀
                ⠀⠀⠀ ⠀⠳⣄⠑⠦⡀⢀⡠⠊⣠⠞⠁⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀ ⢑⡦⣈⠓⢤⡊⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀ ⢀⠔⢁⡤⠚⠑⠤⡈⠣⡀⠀⠀⠀⠀
                ⠀⠀⠀ ⢠⠏⡰⠯⠤⠤⠤⠤⠼⢆⠘⡄⠀⠀⠀
                ⠀⠀⠀⠸⠀⣇⣀⣀⣀⣀⣀⣀⣘⡄⢱⠀⠀⠀
                ⠀⠀⠀ ⢰⠀⡇⠀⠀⠀⠀⠀⠀ ⢰⠁⡌⠀⠀⠀
                ⠀⠀⠀ ⠈⢧⠘⢖⡒⠒⠒⠒⡲⠃⡰⠁⠀⠀⠀
                ⠀⠀⠀⠀ ⠀⠳⢄⡙⣢⠔⠊⣠⠞⠁⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀ ⢀⠴⠋⣡⢔⡛⠢⣀⠀⠀⠀⠀⠀
                ⠀⠀⠀ ⢀⡔⢁⡴⠊⠀⠀⠙⢢⡈⠣⡀⠀⠀⠀
                ⠀⠀⠀ ⡎⢠⠋⠉⠉⠉⠉⠉⠉⠙⡄⢱⡀⠀⠀
                ⠀⠀⠀ ⢇⡼⠒⠒⠒⠒⠒⠒⠒⠒⢣⣠⠃   """)











