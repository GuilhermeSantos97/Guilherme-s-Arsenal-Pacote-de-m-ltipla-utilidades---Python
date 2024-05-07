import sys, time
from colorama import Fore, init

# Inicializa o colorama.
init()

info = (Fore.GREEN+"""

git clone https://github.com/GuilhermeSantos97
Instagram https://www.instagram.com/_gordon_.g/
Facebook https://www.facebook.com/guilherme.Santos.Oficial97
Discord hey_ronak
""" + Fore.RESET)
           
info2 = (Fore.RED+"""     
-- Santos Solutions --
Programa destinado para ajudar e corrigir o seu PC!
Helpyner agradeçe seu apoio!


Licença
Helpyner 2024 Licença
""" + Fore.RESET)

# Aqui ele irá fazer uma animação de typerWrite atravez de uma variavel "info". vc pode acionar outras variaveis.
for char in info: 
    # pygame.mixer.music.load('Som.wav')
    # pygame.mixer.music.play()
    sys.stdout.write (char) 
    sys.stdout.flush() 
    time.sleep (0.1)


for char in info2: 
    # pygame.mixer.music.load('Som.wav')
    # pygame.mixer.music.play()
    sys.stdout.write (char) 
    sys.stdout.flush() 
    time.sleep (0.1)
