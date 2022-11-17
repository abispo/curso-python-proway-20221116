"""
Entrada e saída padrão em Python

Utilizamos 2 funções de entrada e saída padrão no Python
    print()     -> Imprime um texto na tela
    input()     -> Recebe uma informação pelo teclado

Conversor de reais para dólares

"""


if __name__ == "__main__":

    """
    valor_em_reais e cotacao_dolar são variáveis definidas no Python
    
    Uma variável em python pode receber qualquer valor mesmo depois de ja ter sido criada. Ou seja, uma variável
    que foi criada com um valor do tipo string, pode receber um valor do tipo int, e vice-versa.
    """
    valor_em_reais = float(input("Insira o valor em reais: "))
    cotacao_dolar = float(input("Insira a cotação atual do dólar: "))

    """
    A função input sempre retorna uma string, independentemente do valor que foi informado no terminal.
    Para operações matemáticas, precisamos primeiro converter esse valor de entrada que é uma string,
    em um valor numérico.
    
    Nesse caso, utilizamos as funções built-in int() e/ou float()
    """
    valor_convertido = valor_em_reais / cotacao_dolar

    """
    O f no início da string significa f-string. Utilizando f-strings, conseguimos inserir facilmente expressões python
    dentro de string.
    
    Podemos também utilizar o método .format()
    """
    print(f"O valor convertido é igual a {valor_convertido:.2f}")
    print("Mostrando o valor convertido utilizando .format: {:.2f}".format(valor_convertido))
