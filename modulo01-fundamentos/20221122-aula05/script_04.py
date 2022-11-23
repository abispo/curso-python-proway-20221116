"""
Trabalhando com arquivos csv no Python

writer e DictWriter

CSV -> Comma Separated Values -> Valores separados por vírgula

"""

import csv
import os

pasta_files = os.path.join(os.getcwd(), "files")

if __name__ == "__main__":

    lista_clientes = [
        ["Maria", "20", "895.23"],
        ["Mario", "40", "5401.50"],
        ["Joana", "21", "387.21"]
    ]

    with open(os.path.join(pasta_files, "clientes.csv"), "w", encoding="utf-8", newline="") as arquivo:

        writer = csv.writer(arquivo, delimiter=';')

        # Salvamos a primeira linha com os nomes das colunas
        writer.writerow(["nome", "idade", "valor"])

        # Salvamos o resto dos dados no arquivo
        writer.writerows(lista_clientes)

    lista_acessos = [
        {"nome": "Maria", "ultimo_acesso": "20221021"},
        {"nome": "Amanda", "ultimo_acesso": "20221021"},
        {"nome": "Bruna", "ultimo_acesso": "20221022"},
        {"nome": "Marcela", "ultimo_acesso": "20221022"},
        {"nome": "João", "ultimo_acesso": "20221023"},
    ]

    with open(os.path.join(pasta_files, "acessos.csv"), "w", encoding="utf-8", newline="") as arquivo:

        fieldnames = ["nome", "ultimo_acesso"]
        dict_writer = csv.DictWriter(arquivo, fieldnames=fieldnames, delimiter=';')

        # O método writeheader() escreve no arquivo os nomes das colunas definidas em
        # fieldnames
        dict_writer.writeheader()

        # Recebe um dicionário que será salvo no arquivo
        dict_writer.writerow({"nome": "Paulo", "ultimo_acesso": "20221024"})

        # Recebe uma lista de dicionários e salva no arquivo
        dict_writer.writerows(lista_acessos)
