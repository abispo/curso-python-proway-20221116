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

    # 20221118
    # Para excluir itens de uma lista, podemos utilizar 4 maneiras

    # remove()  -> Remove itens de uma lista a partir do valor
    lista3.remove("Alface")
    print(lista3)

    # pop()     -> Remove um item da lista a partir do seu índice, e retorna esse item
    valor_removido = lista3.pop(2)
    print(f"Valor removido: {valor_removido}")
    print(lista3)

    # del       -> del é uma palavra reservada que é utilizada para remover objetos da memória
    # Utilizamos o índice da lista para excluir o item
    del lista3[5]
    print(lista3)

    # clear()   -> Apaga todos os itens da lista
    lista3.clear()
    print(lista3)

    print(f"{'-'*15} 'fatiando(slicing)' listas {'-'*15}")

    lista1 = ["Brasil", "França", "Inglaterra", "Argentina", "Bélgica", "Alemanha"]
    #           0           1           2           3           4           5
    #           -6          -5          -4          -3          -2          -1

    """
    Fatiamos uma sequência (listas, tuplas, strings, etc) utilizando a seguinte sintaxe
    sequencia[inicio:fim:passo]
    inicio  -> Índice inicial de onde vamos pegar o "pedaço" da sequência. Ele é inclusivo.
    fim     -> Índice final de onde vamos pegar o "pedaço" da sequência. Ele é exclusivo
    passo   -> Se quantos em quantos itens vamos extrair esse "pedaço"
    """

    print(lista1[2:5])      # Pegando os itens 3 a 5 da sequência
    print(lista1[-1])       # Retornando apenas o último item
    print(lista1[2:])       # A partir do índice 2, retorna todos os itens restantes
