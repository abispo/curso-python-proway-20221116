"""
Cálculo de média das provas

Trabalhando com operadores aritméticos, lógicos e de comparação

O sistema recebe 3 notas, e calcula a média aritmética dessas notas

Se a média for menor do que 5, o sistema mostra uma mensagem de aluno reprovado
Se a média for maior ou igual a 5 e menor do que 7, o sistema mostra uma mensagem de aluno em recuperação
Se a média for maior do que 7, o sistema mostra uma mensagem de aluno aprovado

"""

if __name__ == "__main__":

    nota_1 = float(input("Informe a primeira nota: "))
    nota_2 = float(input("Informe a segunda nota: "))
    nota_3 = float(input("Informe a terceira nota: "))

    media = (nota_1 + nota_2 + nota_3) / 3

    print("A média do aluno foi {:.2f}".format(media))

    if media < 5:
        print("O aluno foi reprovado.")

    elif media >= 5 and media < 7:
        print("O aluno está de recuperação.")

    else:
        print("O aluno foi aprovado!")
