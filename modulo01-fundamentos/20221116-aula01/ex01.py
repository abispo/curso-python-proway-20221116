
if __name__ == "__main__":

    # Criamos 3 variáveis, cada uma irá armazenar o valor de um produto
    produto_1 = float(input("Informe o valor do primeiro produto: "))
    produto_2 = float(input("Informe o valor do segundo produto: "))
    produto_3 = float(input("Informe o valor do terceiro produto: "))

    # Variável que armazena o valor da soma dos 3 produtos
    soma_produtos = produto_1 + produto_2 + produto_3
    mensagem_desconto_ganho = "\tVocê não ganhou desconto :("

    if soma_produtos < 1000:
        valor_final = soma_produtos

    elif soma_produtos >= 1000 and soma_produtos < 5000:
        desconto = 10
        valor_final = soma_produtos - (soma_produtos * (desconto / 100))
        mensagem_desconto_ganho = f"""
        Você ganhou um desconto de {desconto}%
        O valor total agora é de R$ {valor_final:.2f}
        Você ganhou um desconto de R$ {soma_produtos - valor_final:.2f}
        """

    elif soma_produtos >= 5000 and soma_produtos < 10000:
        desconto = 20
        valor_final = soma_produtos - (soma_produtos * (desconto / 100))
        mensagem_desconto_ganho = f"""
        Você ganhou um desconto de {desconto}%
        O valor total agora é de R$ {valor_final:.2f}
        Você ganhou um desconto de R$ {soma_produtos - valor_final:.2f}
        """

    else:
        desconto = 30
        valor_final = soma_produtos - (soma_produtos * (desconto / 100))
        mensagem_desconto_ganho = f"""
        Você ganhou um desconto de {desconto}%
        O valor total agora é de R$ {valor_final:.2f}
        Você ganhou um desconto de R$ {soma_produtos - valor_final:.2f}
        """

    saida = f"""
    Produto 1: {produto_1:.2f}
    Produto 2: {produto_2:.2f}
    Produto 3: {produto_3:.2f}
    
    O valor total é de {soma_produtos:.2f}\n{mensagem_desconto_ganho}
    """

    print(saida)
