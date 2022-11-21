"""
Exercício 01

Crie a função calcula_nota, que receba 3 parâmetos: nota_1, nota_2, nota_3
Essa função deve retornar a média dessas notas

Crie uma outra função chamada exibir_resultado, que recebe o parâmetro media.
Essa função vai exibir uma mensagem de acordo com o valor do parâmetro media:
Se a media for menor do que 5, exibir a mensagem "Reprovado"
Se a media for maior ou igual a 5 e menor do que 7, exibir a mensagem "Em exame"
Se a media for igual ou maior do que 7, exibir a mensagem "Aprovado"

"""


def calcula_nota(nota_1, nota_2, nota_3):
    return (nota_1 + nota_2 + nota_3) / 3


def exibir_resultado(media):

    if media < 5:
        print("Reprovado!")
    elif media >= 5 and media < 7:
        print("Em exame.")
    else:
        print("Aprovado!")


if __name__ == "__main__":

    media = calcula_nota(4, 5.5, 5)
    exibir_resultado(media)

    exibir_resultado(calcula_nota(6, 6, 9))
