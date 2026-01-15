import csv
import os

def salvar_dados(dados):
    arquivo = "log_registros.csv"
    arquivo_existe = os.path.exists(arquivo) #Pergunta para o sistema se o arquivo log_registros existe ou não

    with open (arquivo, mode='a', newline='') as f: #Abre ou cria o arquivo no modo append.
        colunas = ["sensor", "data", "valor", "status"]
        escritor = csv.DictWriter(f, fieldnames=colunas) #Recebe os valores de cada chave do dic e escreve no arquivo csv nas colunas correspondentes

        if not arquivo_existe:
            escritor.writeheader() #Se o arquivo não existe, cria as colunas com os respectivos valores

        escritor.writerow(dados)