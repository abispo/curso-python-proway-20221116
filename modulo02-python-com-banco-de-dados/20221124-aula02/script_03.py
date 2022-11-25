"""
Programação Orientada a Objetos em Python

Herança -> Quando uma classe herda métodos e atributos de outra classe

"""

from random import randint

# A função uuid4 gera um id randômico, composto de letras e número, separados por -
from uuid import uuid4

# Classe de pagamento que será herdada pelas outras classes
class Pagamento:

    def __init__(self, valor):
        self._valor = valor

    def pagar(self):
        raise NotImplementedError("Você deve implementar esse pagamento")


# Criamos a classe PagamentoBorBoleto que herda da classe pagamento
class PagamentoPorBoleto(Pagamento):

    # Sobrescrevemos o comportamento do método pagar da superclasse
    def pagar(self):
        print(f"O boleto no valor de {self._valor} foi pago.")


class PagamentoPorCartaoDeCredito(Pagamento):

    def __init__(self, valor, numero_cartao, codigo_seg):
        # A função built-in super() chama um método da superclasse.
        # Nesse caso, estamos chamando o método construtor de Pagamento passando o parâmetro valor
        super().__init__(valor)
        self._numero_cartao = numero_cartao
        self._codigo_seg = codigo_seg

    # Esse método retorna um valor booleano aleatório.
    # Python considera o valor 0 como False, e qualquer valor diferente de 0 como True
    def _tem_limite_disponivel(self):
        return bool(randint(0, 1))

    def pagar(self):
        if self._tem_limite_disponivel():
            print(f"O valor de {self._valor} foi pago com cartão de crédito.")
        else:
            print("Não há limite disponível")


if __name__ == "__main__":
    pagamento_por_boleto = PagamentoPorBoleto(200)
    pagamento_por_boleto.pagar()

    pagamento_por_cartao_de_credito = PagamentoPorCartaoDeCredito(
        300, "8789234561789001", "001"
    )
    pagamento_por_cartao_de_credito.pagar()