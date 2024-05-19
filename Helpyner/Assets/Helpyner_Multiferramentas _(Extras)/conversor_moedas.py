#1. <---------IMPORTANDO BIBLIOTECAS--------->
#estou me referindo que "customtkinter é ctk".
import customtkinter as ctk  # <- importando modulo CustomTkinter


#2 <---------Configurações da JANELA PRINCIPAL!--------->
janela = ctk.CTk()  # criando uma variavel chamada janela. janela será responsavél por rodar o ctk. 
janela.title("Conversor De Moedas [Beta!]") #titulo da janela.
janela.geometry("890x480") #geometria da janela.
ctk.set_appearance_mode('dark') # Definindo a aparencia do app e será Escuro.
ctk.set_default_color_theme('blue')


#</NÃO MEXE, APENAS FOI UMA IDEIA DESCARTADA/>
# Canvas Teste
# canvas = ctk.CTkCanvas(
#     janela,
#     bg = 'blue',
#     width = 890,
#     height = 480
# )
# canvas.place(x = 0, y = 0)


#3.<---------Configurações Gerais Texto, Botões etc...!--------->

#Pt.I ---------> Texto.

# Como usar as configurações ctk?
#Ex.: ctk.CTkLabel/OptionMenu e outros....(nome_variavel, valor="", valor=("arial bold", 14)).pack(padding e pixel)
h1 = ctk.CTkLabel(janela, text="Bem-vindo(a) ao conversor de moedas", font=("arial bold", 20))
h1.pack(pady=20, padx=5)

h2 = ctk.CTkLabel(janela, text="Selecione as opções para a conversão: ", font=("arial bold", 14))
h2.pack()


#Pt.II ---------> BOTÕES.

# Aqui ele exibirá uma definição "tipos_moedas" printada.
# O print só vai ocorrer quando o usuário esolher alguma moeda especifica e exibirá no terminal.
# Mostrar prints é bom, pois saberemos se o código realmente funciona.
def tipos_moedas1(escolha):
    print(f"Sua moeda da opcao 1 eh: {escolha}")


#variavel    =   Opção.
tipos_moedas1 = ctk.CTkOptionMenu(janela, 
                                 values=["BRL", "DOGE_COIN", "Bit_COIN", "ARS", "USD", "CAD", "DOP", "AUD", "EUR", "PZN" "GD_FILE"],
                                 command=tipos_moedas1) 
tipos_moedas1.pack(pady=10) #valor=[""] é uma string. Já o valor=[] colocando valoresnúmericos não é uma string.
tipos_moedas1.set("Escolha o tipo da moeda") # Aqui ele vai definir na inicialização "Escolha o tipo da moeda".


def tipos_moedas2(escolha):
    print(f"Sua moeda da opcao 2 eh: {escolha}")

tipos_moedas2 = ctk.CTkOptionMenu(janela, 
                                 values=["BRL", "DOGE_COIN", "Bit_COIN", "ARS", "USD", "CAD", "DOP", "AUD", "EUR", "PZN" "GD_FILE"],
                                 command=tipos_moedas2)

tipos_moedas2.pack(pady=10) #valor=[""] é uma string. Já o valor=[] colocando valoresnúmericos não é uma string.
tipos_moedas2.set("Escolha o tipo da moeda")



janela.mainloop() # Rodando a janela, em loop.