"""
Programação Orientada a Objetos em Python

Classes, objetos, atributos e métodos

"""


# Utilizamos a palavra reservada class para criar uma classe
# Preferencialmente, utilizamos o padrão PascalCase para o nome de classes
class Pokemon:

    valor = 123

    # Quando instanciamos uma classe, o método construtor é chamado. É esse o método
    # responsável por criar e inicializar os atributos de uma classe
    # No caso do Python, quando uma classe é instanciada, o método __init__() é chamado
    def __init__(self, name, type, health):
        # Dentro do método __init__, criaremos os atributos de instância
        # No Python, caso queiramos identificar um atributo ou método como privado,
        # Devemos colocar um underline antes de nome.
        # Essa é uma boa prática, pois no python não temos o conceito de público e privado
        # como em outras linguagens (C#, Java, PHP, etc)
        self._name = name
        self._type = type
        self._health = health

    # Quando temos atributos privados, não podemos acessá-los diretamente. Precisamos
    # utilizar métodos getters e setters para fazer isso.
    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    # No caso do Python, podemos atingir o mesmo objetivo utilizando o decorator @property
    # Ele faz os métodos se comportarem como atributos da classe
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, new_type):
        self._type = new_type

    # TAREFA: Criar os métodos attack(), dodge() e evolve()
    # Os métodos attack() e dodge() vão ser simplesmente prints das ações do pokemon
    # Por exemplo: O método attack vai imprimir na tela ("O Pikachu atacou!")
    # O método evolve, vai alterar os atributos _name e health do pokemon


if __name__ == "__main__":
    # Instanciamos a classe chamando ela como se fosse uma função
    pikachu = Pokemon(name="Pikachu", type="Elétrico", health=70)
    pikachu.set_name("Raichu")
    print(pikachu.get_name())

    pikachu.type = "Eletric"
    print(pikachu.type)

    bulbasaur = Pokemon(name="Bulbasaur", type="Planta", health=85)
