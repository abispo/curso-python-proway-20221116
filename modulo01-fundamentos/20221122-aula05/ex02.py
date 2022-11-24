
import os

if __name__ == "__main__":

    print("Abrindo o arquivo vendas.txt...")

    with open(os.path.join(os.getcwd(), "files", "vendas.txt"), "r", encoding="utf-8") as arquivo:


        # Ler o arquivo
        conteudo = arquivo.readlines()

        # Retirar o caracted especial \n
        conteudo = [item.replace("\n", "") for item in conteudo]

        # Retirar os itens que são strings vazias para a nova lista
        conteudo = [item for item in conteudo if len(item) > 0]

        inicio = 0
        final = 3
        passo = 3

        lista_vendedores = []

        while inicio < len(conteudo):

            # Pegamos um pedaço da lista de acordo com inicio e final
            dados_vendedor = conteudo[inicio:final]

            # Salvamos os dados dessa nova lista, formatando os valores
            codigo = dados_vendedor[0].split(": ")[-1]
            nome = dados_vendedor[1].split(": ")[-1]
            valor = float(dados_vendedor[2].split(": ")[-1])

            data = {
                "codigo": codigo,
                "nome": nome,
                "valor_vendas": valor
            }

            lista_vendedores.append(data)

            # Altera a posição inicial e final que os dados serão capturados
            inicio += passo
            final += passo

        # A função built-in sum() soma todos os valores de uma lista numérica
        valor_total_de_vendas = sum([vendedor.get("valor_vendas") for vendedor in lista_vendedores])
        print(f"{valor_total_de_vendas:.2f}")

        media_total_de_vendas = valor_total_de_vendas / len(lista_vendedores)
        print(f"{media_total_de_vendas:.2f}")

