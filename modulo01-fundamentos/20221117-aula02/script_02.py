"""
Laço for

O laço for é usado para iterar (acessar sequencialmente item a item) sobre sequências de itens

list    -   Listas
dict    -   Dicionários
tuple   -   Tuplas
set     -   Sets (conjuntos)

Além desses tipos de sequências, também podemos utilizar o laço for em strings

Dentro do laço for, podemos utilizar 2 comandos
    - break: Interrompe imediatamente a execução do laço for
    - continue: Ignora o resto do bloco, e volta a linha do for

"""

# Leia os itens da lista até encontrar a palavra "Nenhuma". Caso encontre, saia do loop.

if __name__ == "__main__":
    lista_palavras = [
        "Abacaxi", "Manga", "Nenhuma", "Uva", "Pitanga"
    ]

    for palavra in lista_palavras:
        if palavra == "Nenhuma":
            break       # Interrompe o loop e sai
        print(palavra)

    lista_numeros = [
        5, 10, 14, 7, 8
    ]

    soma = 0

    for numero in lista_numeros:
        if numero % 2 == 1:
            continue

        if 1 == 1:
            pass

        soma += numero
    print(f"Soma: {soma}")
