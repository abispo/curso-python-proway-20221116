"""
Listas em Python

Listas em Python são um tipo de dado onde podemos armazenar um conjunto de dados, inclusive outras listas

Listas são objetos indexáveis, modificáveis, iteráveis e que permitem valores repetidos

"""

if __name__ == "__main__":

    # Podemos criar uma lista de 2 maneiras:
    lista1 = [4, 5, 5, 5, 4.3, "python", [2, 4]]
    lista2 = list("Python")

    print(lista1)
    print(lista2)

    # Como listas são objetos indexáveis, podemos acessar qualquer item da lista pelo seu índice
    # Atenção: O índice em uma lista começa pelo valor 0
    # Acessamos o item pelo seu índice passando o índice dentro de colchetes
    lista3 = ["Abacaxi", "Manga", "Melancia", "Limão"]
    print(lista3[2])

    # A partir dos índices também conseguimos alterar um valor na lista
    lista3[3] = "Abacate"
    print(lista3)

    # Para inserir itens na nossa lista, podemos utilizar os métodos:

    # append()  -> Insere um novo item no final da lista
    lista3.append("Goiaba")
    print(lista3)

    # insert()  -> Insere um novo item na lista no índice especificado
    # Insere "Pitanga" no índice 2 da lista
    lista3.insert(2, "Pitanga")
    print(lista3)

    # extend()  -> Ele insere os itens de um outro iterável no final da lista
    lista4 = ["Batata", "Tomate", "Alface", "Brócolis"]
    lista3.extend(lista4)
    print(lista3)