"""
Tuplas e sets (conjuntos)

Tuplas e sets, junto com listas e dicionários, são os tipos de dados em Python que são tratados
como sequências

"""

from random import randint

if __name__ == "__main__":

    tupla1 = (1, 2, 3,)
    print(tupla1)

    # Tuplas são muito parecidas com listas, a difença mais significante é que tuplas não permitem
    # alteração dos seus valores (é imutável)
    # A linha abaixo causará um erro
    # tupla1[2] = 10

    # Caso realmente seja necessário alterar o valor de uma tupla, podemos convertê-la para lista,
    # fazer a alteração e converter novamente para tupla
    lista1 = list(tupla1)
    lista1[2] = 10
    tupla1 = tuple(lista1)
    print(tupla1)

    # sets(conjuntos) são outro tipo de sequência em Python. Podem ser entendidos como
    # representação dos conjuntos matemáticos na linguagem. Um detalhe interessante, é que sets não
    # permitem valores repetidos

    # Criar uma lista de 100 itens, com valores randômicos entre 1 e 20
    lista_numeros = []
    for _ in range(100):
        lista_numeros.append(randint(1, 20))

    print(lista_numeros)
    lista_numeros.clear()

    # Podemos fazer a mesma coisa utilizando list comprehension
    lista_numeros = [randint(1, 20) for _ in range(100)]
    print(lista_numeros)

    lista_repetidos = []
    nova_lista = []

    # for item in lista_numeros:
    #     if item not in lista_repetidos:
    #         nova_lista.append(item)
    #         lista_repetidos.append(item)
    #     else:
    #         lista_repetidos.append(item)
    #
    # nova_lista.sort()
    # print(nova_lista)

    # Devemos agora remover os itens repetidos da lista
    lista_numeros.sort()
    print(list(set(lista_numeros)))

