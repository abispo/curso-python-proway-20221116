"""
Funções recursivas (recursividade)

São funções que chamam a si mesmas.

Exemplo de função recursiva: Cálculo do fatorial de um número inteiro
5!  -> 5 * 4 * 3 * 2 * 1    -> 120

"""


def fatorial_nao_recursivo(numero):
    contador = numero
    total = numero

    while contador > 1:
        # total = total * (contador - 1)
        total *= (contador - 1)

        # contador = contador -1
        contador -= 1

    return total


def fatorial(numero):

    if numero == 1:
        return numero

    return numero * fatorial(numero - 1)


if __name__ == "__main__":

    print(fatorial_nao_recursivo(5))
    print(fatorial(5))