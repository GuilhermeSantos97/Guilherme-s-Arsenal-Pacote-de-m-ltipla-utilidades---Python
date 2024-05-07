# importando o modulo necessário
# Se caso não souber oq são dominios
# Acesse o "MD" O que são dominios.md
import requests
from colorama import Fore, init

#inicializa o colorama
init()

#Definição de dominio Scanner.
def domain_scanner(domain_name,sub_domnames):
    print(Fore.RED + 'URLS FORAM ENCONTRADOS!: ' + Fore.RESET)
     
    
    for subdomino in sub_domnames:
       
       # Aqui será a entrada do url
        url = f"https://{subdomino}.{domain_name}"
         
        
        try:
            
            requests.get(url)
             
            # Aqui irá printar o url
            print(f'[+] {url}')
             
        # Se caso der erro de conexão, ele exibirá aqui através.
        # Do Except.
        except requests.ConnectionError:
            pass
 

if __name__ == '__main__':
   
    print("Por favor APENAS coloque o URL e o nome de domínio")
    domínio = input("Nome do Dominio: ")
 
    
    with open('basiclist.txt','r') as f:
       
        
        nome = f.read()
         
       
        sub_dom = nome.splitlines()
         

    domain_scanner(domínio,sub_dom)