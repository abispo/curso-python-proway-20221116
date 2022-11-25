"""
Programação Orientada a Objetos em Python

Composição -> Quando um objeto compõe ou é composto por outro(s)

"""

import random

NAIPES = ["\u2660", "\u2665", "\u2663", "\u2666"]
VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


class Carta:

    def __init__(self, naipe, valor):
        self._naipe = naipe
        self._valor = valor

    # __init__, __str__ e __repr__ são chamados métodos mágicos do Python
    def __str__(self):
        return f"{self._naipe}{self._valor}"

    def __repr__(self):
        return f"{self._naipe}{self._valor}"


class Baralho:

    def __init__(self):
        self._cartas = []

        for naipe in NAIPES:
            for valor in VALORES:
                self._cartas.append(Carta(naipe, valor))

    def __str__(self):
        return ' '.join([f"{carta}" for carta in self._cartas])

    def embaralhar(self):
        random.shuffle(self._cartas)

if __name__ == "__main__":

    baralho = Baralho()
    print(baralho)
    baralho.embaralhar()
    print(baralho)
