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
        # super()
        self._valor = valor
        self._numero_cartao = numero_cartao
        self._codigo_seg = codigo_seg

    def _tem_limite_disponivel(self):
        return bool(randint(0, 1))

    def pagar(self):
        if self._tem_limite_disponivel():
            print(f"O valor de {self._valor} foi pago com cartão de crédito.")


if __name__ == "__main__":
    pagamento_por_boleto = PagamentoPorBoleto(200)
    pagamento_por_boleto.pagar()
