"""
Trabalhando com arquivos csv no Python

reader e DictReader

CSV -> Comma Separated Values -> Valores separados por vírgula

"""

import csv
import os

# pasta_files terá o caminho completo até a pasta files do projeto
pasta_files = os.path.join(os.getcwd(), "files")

if __name__ == "__main__":

    # Utilizando reader
    # O método reader retorna as linhas do arquivo como listas, com os itens sendo separados
    # pelo delimitador
    with open(os.path.join(pasta_files, "notas.csv"), "r", encoding="utf-8") as arquivo:
        # O parâmetro delimiter indica qual é o caractere separador das colunas
        reader = csv.reader(arquivo, delimiter=';')

        for linha in reader:
            print(linha)

    print('-'*30)

    # Utilizando DictReader
    # A classe DictReader retorna as linhas como dicionários, com as chaves sendo os valores
    # da primeira linha (cabeçalho) e os valores sendo os dados a partir da segunda linha
    with open(os.path.join(pasta_files, "notas.csv"), "r", encoding="utf-8") as arquivo:
        dict_reader = csv.DictReader(arquivo, delimiter=';')

        for linha in dict_reader:
            print(linha)
