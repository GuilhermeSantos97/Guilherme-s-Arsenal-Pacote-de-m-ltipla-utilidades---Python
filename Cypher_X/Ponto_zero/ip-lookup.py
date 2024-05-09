#Importar as bibliotecas!

import requests
from colorama import Fore

def phone_locator(phone_number, api_key):
    url = f"https://api.apilayer.com/number_verification/validate?number={phone_number}"
    #cabeçalho
    headers = { 
        "apikey": api_key
    }

    #aqui é a resposta
    response = requests.get(url, headers=headers)
    data = response.json()
    return data


def print_phone_details(phone_details):
    print("Detalhes do Telefone:")
    print(f"Número: {phone_details['Número']}")
    print(f"País: {phone_details['country_name']} ({phone_details['country_code']})")
    print(f"Carrier: {phone_details['carrier']}")
    print(f"Line Type: {phone_details['line_type']}")
    print(f"Localização: {phone_details['Localização']}")
    print(f"Valido: {phone_details['Valido']}")

api_key = "22WfDqB635jMOWkxdeC1r2BXew1tXHLU"

phone_number = input(Fore.MAGENTA+"Digite o número de telefone para localizar: ")

phone_details = phone_locator(phone_number, api_key)
print_phone_details(phone_details)