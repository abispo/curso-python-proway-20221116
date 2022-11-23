
import csv
import os

if __name__ == "__main__":

    print("Carregando o arquivo nomes.txt...")

    with open(os.path.join(os.getcwd(), "files", "nomes.txt"), "r", encoding="utf-8") as arquivo:

        print("Limpando dados...")

        # Lê o conteúdo do arquivo como uma lista de strings
        conteudo = arquivo.readlines()

        # Utilizaremos list-comprehension para formatar o conteúdo da lista
        # Removemos o caractere especial '\n' das strings
        conteudo = [item.replace("\n", "") for item in conteudo]

        # Convertemos todas as letras da palavra para minusculas
        conteudo = [item.lower() for item in conteudo]

        # Convertemos as strings da lista para o formato snake cake
        conteudo = [item.replace(" ", "_") for item in conteudo]

        # Criando o dicionário que irá armazenar as informações
        repeticao_nomes = {}

        for item in conteudo:
            contador = repeticao_nomes.get(item, 0)
            contador += 1
            repeticao_nomes[item] = contador

        # Criar a estrutura final que irá mostrar os resultados
        lista_final = []
        for chave, valor in repeticao_nomes.items():
            lista_final.append(
                {"nome": chave, "vezes": valor}
            )


        # Ordenando os dicionários pelo valor da chave 'vezes': Do maior para o menor
        # Para isso utilizamos a função built-in sorted()
        lista_final = sorted(lista_final, key=lambda item: item.get("vezes"), reverse=True)

        # Mostrando os 10 primeiros nomes na tela
        print("Primeiros 10 nomes que mais aparecem")
        for item in lista_final[:10]:
            saida = f"{item.get('nome').replace('_', ' ').title().ljust(15, ' ')} {item.get('vezes')}"
            print(saida)

        with open(os.path.join(os.getcwd(), "files", "nomes.csv"), "w", encoding="utf-8", newline="") as arquivo_csv:

            dict_writer = csv.DictWriter(arquivo_csv, fieldnames=["nome", "quantidade"], delimiter=";")
            dict_writer.writeheader()

            for item in lista_final:
                data = {
                    "nome": f"{item.get('nome').replace('_', ' ').title()}",
                    "quantidade": item.get("vezes")
                }
                dict_writer.writerow(data)
