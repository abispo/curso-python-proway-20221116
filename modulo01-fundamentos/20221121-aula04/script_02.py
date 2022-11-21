"""
Empacotamento e desempacotamento de argumentos
Ou
Argumentos arbitrários

*args       -> Lista arbitária de argumentos
    -> Passamos os argumentos para a função por posição

**kwargs    -> Conjunto chave-valor de argumentos
    - Passamos os argumentos para a função por nome

Os nomes args e kwargs são apenas nomes padrão que são recomendados utilizar. Podemos utilizar
qualquer nome que quisermos

"""

# Exemplo de empacotamento de argumentos
def func01(*args):
    return len(args)


# Exemplo de desempacotamento de argumentos
def func02(inicio, fim, valor):
    return inicio <= valor <= fim
    

if __name__ == "__main__":

    # Estamos "empacotando" os argumentos no parâmetro args
    print(func01(4, 7, 10, 43, 10))
    print(func01("Cachorro", "Gato", 82.9))
    print(func01())
