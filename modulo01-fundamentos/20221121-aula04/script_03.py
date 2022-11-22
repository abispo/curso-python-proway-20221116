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


# Exemplo de empacotamento de argumentos
def func01(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave} = {valor}")

# Exemplo de desempacotamento de argumentos por nome
def func02(inicio, fim, valor):
    return inicio <= valor <= fim


if __name__ == "__main__":
    func01(nome="Maria", idade=20)
    func01(jogo="Brasil x Argentina", data="12/12/2022")

    # Desempacotando os valores do dicionários nos parâmetros da função
    print(func02(**{"valor": 10, "inicio": 15, "fim": 20}))
    print(func02(**{"fim": 30, "valor": 25, "inicio": 20}))

    # func02(inicio=20, fim=30, valor=25)
