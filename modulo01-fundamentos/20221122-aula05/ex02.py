
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
                "valor_vendas": valor,
                "bonus": 0,
                "adicional": 0
            }

            lista_vendedores.append(data)

            # Altera a posição inicial e final que os dados serão capturados
            inicio += passo
            final += passo

        # A função built-in sum() soma todos os valores de uma lista numérica
        valor_total_de_vendas = sum([vendedor.get("valor_vendas") for vendedor in lista_vendedores])
        media_total_de_vendas = valor_total_de_vendas / len(lista_vendedores)

        for vendedor in lista_vendedores:

            valor_vendas = vendedor.get("valor_vendas")

            if valor_vendas >= 5000 and valor_vendas < 9999.99:
                vendedor["bonus"] = 10
            elif valor_vendas >= 10000 and valor_vendas < 14999.99:
                vendedor["bonus"] = 20
            elif valor_vendas >= 15000:
                vendedor["bonus"] = 30

        lista_vendedores = sorted(lista_vendedores, key=lambda vendedor: vendedor.get("valor_vendas"), reverse=True)

        # Distribuindo os valores adicionais para os 3 primeiros colocados
        lista_vendedores[0]["adicional"] = 500
        lista_vendedores[1]["adicional"] = 250
        lista_vendedores[2]["adicional"] = 125

        print("*"*50)
        print("* INFORMAÇÕES SOBRE AS VENDAS *")
        print(f"VALOR TOTAL DAS VENDAS: {valor_total_de_vendas:.2f}")
        print(f"VALOR MÉDIO POR VENDEDOR: {media_total_de_vendas:.2f}")
        print("*" * 50)
        print("* RANKING DOS VENDEDORES")

        for vendedor in lista_vendedores:
            print(f"{'Código:'.ljust(30)} {vendedor.get('codigo')}")
            print(f"{'Nome:'.ljust(30)} {vendedor.get('nome').ljust(40)}")
            print(f"{'Total de Vendas:'.ljust(30)} {vendedor.get('valor_vendas'):.2f}")
            print(f"{'Bônus:'.ljust(30)} {vendedor.get('bonus')}%")

            if vendedor.get("adicional"):
                print(f"{'Valor adicional'.ljust(30)} R$ {vendedor.get('adicional')}")

            print("-"*50)
