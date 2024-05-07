# Pip install pyautogui.
# Pyatogui ele está definido como "py"
import pyautogui as py 
import random
import time

time.sleep(5)

# Em menssagens voce pode colocar qualquer coisa aqui!
menssagens = ["Ui ele gosta", "Aí pai para", "Pesadããããooo", "Vem pro fut,VEM",
              "Acorda meu jovem", "izzzii", "chegou menssagem para vc", "Coe", "Olha aqui",
              "tmj", "Aqui é o Brazil", "XDDDDDDD", "Nunca nem vi","meeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeehhhhhhhhhhh"]


# O "i" siginifica inteiro
# O "range" serve para criar uma sequência de números de acordo com os parâmetros que passamos pra ele.
# Também A função `range` em Python é uma ferramenta poderosa para gerar sequências de números em loops e iterações.
for i in range(100):
    msg = random.choice(menssagens) # Variavel menssagens dentro do parentese
    py.write(msg)
    py.press("enter")

    # Santos Troll Tools NEO - 2024 COPYRIGHT