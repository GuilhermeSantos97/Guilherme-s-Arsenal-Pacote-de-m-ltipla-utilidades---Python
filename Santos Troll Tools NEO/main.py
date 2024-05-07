# Pyautigui é um sistema mais automático!
# Sem precisar mouse ou teclado para apertar a tecla.Sistema automático!! :) 
# Não precisa de Ferramenta física ele já simula sozinho.

import time
import pyautogui


# Os numeros do python sempre seguem por ponto. Padrão Americano.
# Aqui posso alterar o PAUSE pela a minha preferência.
pyautogui.PAUSE = 0.5 # Comando de Pausa. 

#1.----------------Inicialização -----------------
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)

#2. ----------------Texto----------------
pyautogui.click(x=494, y=81)
pyautogui.write("Computador hackeado 👺, hihihi")

# Aqui ele vai ficar em um limite de loop de "29"
for apagar in range(29):
    apagar = pyautogui.press("backspace")

pyautogui.write("https://youtu.be/uHgt8giw1LY?si=rIju3PiW6VbvrAwb")
pyautogui.press("enter")
time.sleep(2)


pyautogui.press ("f")


