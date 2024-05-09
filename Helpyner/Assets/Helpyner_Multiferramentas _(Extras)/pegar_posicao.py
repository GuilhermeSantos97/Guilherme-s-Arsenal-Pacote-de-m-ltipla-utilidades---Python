#Importar as bibliotecas necessárias

#pegar_posição.py é dedicado ao pegar posição do ponteiro do mouse!
import time
import pyautogui

# Ele vai esperar 5 segundos
print("Escolhe o local onde vc deseja pegar a posição do ponteiro mouse")
print("Agurde 5 segundos")
time.sleep(5)
print(pyautogui.position()) # Ele vai dizer onde está a posição do mouse.

pyautogui.scroll(200)

#Para exibir tudo do seu teclado:
#print(KEYBOARD_KEYS)