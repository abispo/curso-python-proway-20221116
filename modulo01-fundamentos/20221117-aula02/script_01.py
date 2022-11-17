"""
Laço for

O laço for é usado para iterar (acessar sequencialmente item a item) sobre sequências de itens

list    -   Listas
dict    -   Dicionários
tuple   -   Tuplas
set     -   Sets (conjuntos)

Além desses tipos de sequências, também podemos utilizar o laço for em strings

Calcular o quadrado de uma lista de números

"""
if __name__ == "__main__":

    lista_numeros = [2, 5, 8, 14, 21, 40]

    for numero in lista_numeros:
        print(numero * numero)
