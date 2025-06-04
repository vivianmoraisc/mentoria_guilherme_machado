# Construir um código Python que extraia dados da API da Gupy, e que esses dados sejam salvos em um JSON na pasta “dados/vagas”

import requests
import json
import os


cargo = input("Digite qual cargo deseja pesquisar: ")

url = f"https://portal.api.gupy.io/api/v1/jobs?jobName={cargo}"

response = requests.get(url)

print("Os dados estao sendo requisitados...")

dados = response.json()

pasta = "dados_das_vagas"

if not os.path.exists(pasta):
    os.makedirs(pasta)

with open("dados_das_vagas/dados.json", "w") as arquivo:

    json.dump(dados, arquivo, indent = 4)

    print("Pasta criada contendo os dados dos cargos com sucesso!")


'''

Código faz o que foi pedido, mas tem muitas coisas a serem melhoradas. Quando um novo cargo é pesquisado, a pasta com os dados subescritos vão pra outro lugar 
e não são atualizadas no lugar de origem dela. Entre outras coisas, como ao colocar o nome de um cargo, so permitir string.

Código será aperfeiçoado no próximo desafio.

'''