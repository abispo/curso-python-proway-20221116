"""
Empacotamento e desempacotamento de argumentos
Ou
Argumentos arbitrários

*args       -> Lista arbitrária de argumentos
    -> Passamos os argumentos para a função por posição

**kwargs    -> Conjunto chave-valor de argumentos
    - Passamos os argumentos para a função por nome

Os nomes args e kwargs são apenas nomes padrão que são recomendados utilizar. Podemos utilizar
qualquer nome que quisermos

"""

from random import uniform
from exercicio_01 import calcula_media, exibir_resultado

# Exemplo de empacotamento de argumentos
def func01(*args):
    return len(args)


# Exemplo de desempacotamento de argumentos
def func02(inicio, fim, valor):
    return inicio <= valor <= fim


if __name__ == "__main__":

    # Estamos "empacotando" os argumentos no parâmetro args
    print(func01(4, 7, 10, 43, 10))
    print(func01("Cachorro", "Gato", 82.9))
    print(func01())

    # Chamando a função passando os valores dos argumentos normalmente
    print(func02(3, 4, 10))
    lista_faixas = [
        # func02(4, 6, 5)
        (4, 6, 5),

        # func02(10, 90, 56)
        (10, 90, 56),

        # func02(30, 45, 20)
        (30, 45, 20)
    ]

    for lista in lista_faixas:
        # print(func02(lista[0], lista[1], lista[2]))
        # Substituimos a expressão acima por
        print(func02(*lista))


    # Exemplo 2: Calculando as médias aleatórios de 100 alunos
    # Usando list comprehension para criar uma lista de listas com 100 itens
    lista_notas = [
        [uniform(1, 10), uniform(1, 10), uniform(1, 10)] for _ in range(100)
    ]
    print(lista_notas)

    for lista in lista_notas:
        exibir_resultado(calcula_media(*lista))
