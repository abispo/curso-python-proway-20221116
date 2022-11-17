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

Também podemos utilizar else ao lado do for, para executar um bloco após o laço for ter terminado.

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

    print("-"*20)

    lista_numeros = [
        5, 10, 14, 7, 8
    ]

    soma = 0

    for numero in lista_numeros:
        if numero % 2 == 1:
            continue

        if numero == 98:
            break

        soma += numero
    else:
        print("Todos os itens foram processados")

    print(f"Soma: {soma}")

    # Utilizando for com a função geradora range()
    for numero in range(1, 100):
        print(numero)
