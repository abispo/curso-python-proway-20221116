"""
Funções lambda

Funções lambda são funções anônimas. Elas geralmente são usadas  em conjunto com as funções
map(), filter() e reduce()

E porque funções anônimas? Elas não tem nome definido.

"""

from random import randint

if __name__ == "__main__":

    quadrado = lambda x: x ** 2
    """
    def func(x):
        return x ** 2
    """

    print(quadrado(10))

    # Criando uma lista de números aleatórios de 1 a 50
    lista_numeros = [randint(1, 50) for _ in range(1000)]

    lista_pares = filter(lambda x: x % 2 == 0, lista_numeros)
    print(list(lista_pares))

    lista_quadrados = map(lambda x: x ** 2, lista_numeros)
    print(list(lista_quadrados))
