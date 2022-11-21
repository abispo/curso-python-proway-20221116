"""
Funções (procedures) são blocos de código que podem ser chamados em qualquer lugar do código.

"""

from random import randint


# Sintaxe de uma função no Python
# Sempre iniciamos uma função com a palavra reservada def
# Uma função pode ou não receber parâmetros
# E uma função pode ou não retornar um valor
def hello():
    print("Olá")


# Podemos criar funções que recebem parâmetros.
# Parâmetros nada mais são que variáveis que receberão valores que serão passados para dentro
# da função
# name é um argumento obrigatório da função hello_name
# is_name possui um valor padrão. Se o argumento não for indicado, o valor de is_new será False
# is_new é um parâmetro opcional, pois recebe um valor padrão
# Sempre indicamos primeiro os parâmetros obrigatório, depois os opcionais
def hello_name(name, is_new=False):
    print(f"Olá {name}.")
    if is_new:
        print("Você é novo na empresa.")
    else:
        print("Você não é novo na empresa.")


def calculate_bonus(name, sector=1):
    print(f"Olá {name}!")

    if sector == 2:
        print("Seu bônus é de 10%")
    elif sector == 3:
        print("Seu bônus é de 20%")
    else:
        print("Você não recebe bônus")


# A palavra reservada return, usada dentro da função, indica o valor de retorno que essa função
# irá retornar depois que terminar a sua execução
def is_on():
    valor = randint(1, 100)

    # É a mesma coisa que as 4 instruções abaixo
    # return not valor < 70

    if valor < 70:
        return False
    else:
        return True


if __name__ == "__main__":
    # Chamamos uma função pelo nome dela
    # Não esquecer dos parêntesis no final
    hello()
    hello_name("Maria")
    hello_name("Paulo", True)

    # Além de passarmos os valores na ordem dos argumentos, podemos também indicar os valores
    # para os argumentos em qualquer ordem.
    hello_name(
        is_new=True,
        name="Cíntia"
    )

    # Passando os valores na ordem correta por posição
    calculate_bonus("Maria", 3)

    # Passando os valores em qualquer ordem pelo nome do argumento
    calculate_bonus(sector=3, name="Bruna")

    # Passando apenas os valores obrigatórios por posição
    calculate_bonus("Daniele")

    # A função calculate_bonus retorna None
    print(calculate_bonus("Eduarda"))

    # If de uma linha só
    retorno = "Ligado" if is_on() else "Desligado"
    print(retorno)
