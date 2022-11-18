"""
Dicionários

Dicionários são estruturas que armazenam dados no formato chave: valor

Dicionários são estruturas iteráveis, indexáveis, modificáveis e que não permitem
chaves duplicadas

"""

if __name__ == "__main__":

    # Podemos criar dicionários de 2 maneiras
    cliente1 = {
        # chave: valor
        # key: value
        "nome": "Maria",
        "idade": 20,
        "sexo": "F",
        "setor": "TI",
        "cargo": "Especialista"
    }

    cliente2 = dict(
        nome="João",
        idade=30,
        sexo="M",
        setor="TI",
        cargo="Sênior"
    )

    print(cliente1)
    print(cliente2)

    # Como dicionários são iteráveis, podemos acessar os seus itens de forma sequencial
    # dentro de um laço for

    # Por padrão, os nomes das chaves são mostrados como itens do dicionário
    # É a mesma coisa que fazer for item in cliente2.keys()
    for item in cliente2:
        print(item)

    print('-'*30)
    # Se quisermos mostrar os valores em um dicionário, utilizamos o método .values()
    for value in cliente2.values():
        print(value)

    print('-'*30)
    # Se quisermos mostrar tanto a chave quanto o valor, utilizamos o método .items()
    for chave, valor in cliente2.items():
        print(f"{chave} = {valor}")
