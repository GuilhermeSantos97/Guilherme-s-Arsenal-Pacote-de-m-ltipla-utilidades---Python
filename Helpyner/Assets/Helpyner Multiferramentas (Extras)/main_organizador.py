# O programa irá organizar os arquivos
# Em sua respectiva pasta

import os
from tkinter.filedialog import askdirectory


def main():
    # Localizar a pasta que será feita a organização
    pasta = askdirectory(title="Selecione uma pasta para organizar")
    print(pasta)

    # Criar uma lista de arquivos da pasta selecionada
    lista_arquivos = os.listdir(pasta)
    print(lista_arquivos)

    locais = {
        "Documentos": [".doc", ".docx"],
        "Planilhas":[".xls", ".xlsx"],
        "ArquivoPDF": [".pdf"],
        "Imagens": [".jpeg", ".jpg",".png", ".gif", ".psd", ".bmp"],
        "Vídeos": [".mpeg", ".mp4", ".avi", ".mov", ".mpg"]
    }

    for arquivo in lista_arquivos:

        #Categorias (Nome, extensão de arquivos)
        nome, extensao = os.path.splitext(f"(pasta)/(arquivo)")

        for local in locais: # O If representa "Se"
            if extensao in locais[local]:
                # Verificar se a pasta de separa existe
                # Senão existir vai criar a pasta
                if not os.path.exists(f"(pasta)/(local)"):
                    os.mkdir(f"(pasta)/(local)")

                #Trasferir/Mover o arquivo para a pasta da organização
                os.rename(
                    f"(pasta)/(arquivo)",
                    f"(pasta)/(local)/(arquivo)"
                )


if __name__ == "__main__":
    main()