# Python Fundamentos - Aula 02

## Laços de repetição no Python

### Laço `for`

O laço `for` é utilizado quando queremos iterar (percorrer item a item) uma sequência. Essa sequência pode ser uma lista, uma tupla, um dicionário, um conjunto ou uma string.

O bloco do laço `for` será executado enquanto houverem itens na sequência a serem lidos. Exemplo:
```python
carros = ["Gol", "Fusca", "Opala"]

for carro in carros:
    print(carro)
```

Caso queiramos interromper a execução desse laço for antes de todos os itens da sequência serem lidos, utilizamos o comando `break`:
```python
# Esse código imprime a sequência 0, 1, 2, 3, 4, 5, 6, 7, 8. E depois finaliza.
# A função built-in range() gera uma sequência de números. Ela pode receber até 3 argumentos
for numero in range(10):
    if numero > 8:
        break
    print(numero)
```

Dentro de um laço for, o comando `continue` retorna automaticamente ao início da iteração, ignorando todo o código após ele.
```python
# Esse código imprime todos os números ímpares 0 até 19
for numero in range(20):
    if numero % 2 == 0:
        continue
    print(numero)
```

Caso queiramos executar um outro bloco de código logo após todos os itens serem iterados, podemos utilizar o bloco `else` no mesmo nível do for. O código dentro desse bloco somente será executado se a cláusula break não for executada
```python
itens = ["Banana", "Batata", "Abacaxi"]

for item in itens:
    if item == "Uva":
        break
        print(item)
    else:
        print("Todos os itens foram lidos")
```

### Laço `while`

Assim como o laço `for`, `while` também executa um bloco de código repetidas vezes. Mas enquanto o `for` funciona até não houverem mais itens em uma sequência, o laço `while` executa um bloco de código até uma condição definida for verdadeira.
```python
# A função randint() do módulo random gera um número randômico dentro de um determinado intervalo
from random import randint

score = 0

while score > 90:
    # Gera um número randômico entre 1 e 10 e adiciona a variável score
    score += randint(1, 10)
```

Em um bloco `while` também podemos fazer uso das instruções `break`, `continue` e `else`. Elas possuem exatamente o mesmo significado que no bloco `for`

### Listas
Lista é um dos 4 tipos de dados dentro do Python que servem para armazenar múltiplos valores. Listam podem inclusive armazenar outras listas.

As listas podem ser definidas como estruturas de dados ordenadas, indexáveis, modificáveis e que permitem itens repetidos

#### Criação de listas
Listas podem ser criadas de 2 maneiras: Diretamente ou utilizando a função built-in `list()`
```python
primeira_lista = [1, 2, 3, 4, 5]
segunda_list = list("Python")

print(primeira_lista)
print(segunda_list)
```

#### Acessando e alterando elementos em uma lista
Como listas são itens indexáveis, podemos acessar qualquer item de uma lista através do índice. Índices são as posições dos elementos em uma lista, e os índices sempre iniciam por zero
```python
nomes = ["Maria", "José", "João"]
#           0       1       2
print(nomes[2])         # Imprime João, pois é o terceiro item da lista (índice 2)
```

Podemos alterar um item da lista utilizando o seu índice
```python
nomes = ["Maria", "José", "João"]
nomes[1] = "Roberto"
print(nomes)            # Será impresso ["Maria", "Roberto", "João"]
```

#### Adicionando e removendo elementos de uma lista
Para adicionar itens em uma lista, podemos utilizar 3 métodos de listas: `append()`, `insert()` e `extend()`

O método `append()` insere um novo item no final da lista

```python
lista = [1, 2, 3]
lista.append(5)
print(lista)        # Irá imprimir [1, 2, 3, 5)
```

O método `insert()` insere um novo item na lista a partir do índice informado
```python
lista = [1, 2, 3, 4, 5]
lista.insert(3, 50)
print(lista)        # Irá imprimir [1, 2, 3, 50, 4, 5]
```

E finalmente o método `extend()` adiciona uma lista (ou um iterável) existente no final da lista
```python
lista = [1, 2, 3, 4, 5]
lista.extend([6, 7, 8])
print(lista)        # Irá imprimir [1, 2, 3, 4, 5, 6, 7, 8]
```

Podemos remover itens de uma lista utilizando 4 opções: Os métodos `remove()`, `pop()` e `clear()`, e a palavra reservada `del`
```python
lista = ["Blumenau", "Gaspar", "Pomerode", "Indaial", "Brusque"]

# O método remove() remove um item de uma lista a partir de seu valor
lista.remove("Gaspar")      # Remove o item "Gaspar" da lista

# O método pop() remove um item a partir de seu índice, e retorna o valor do item removido
cidade = lista.pop("Brusque")     # Remove o item "Brusque" da lista e atribui a variável cidade

# Podemos também utilizar a palavra reservada del para remover um item de uma lista a partir de seu índice
# del pode ser utilizada também para remover qualquer tipo de variável do contexto de execução do programa
del lista[2]        # Remove o valor "Indaial"

# O método clear() remove todos os itens de uma lista
lista.clear()       # A lista agora é uma lista vazia []
```

#### "Fatiando (slicing)" listas
Utilizando índices, podemos pegar partes de listas (e de strings) utilizando a sintaxe de slicing
```python
lista = ["Python", "Java", "CSharp", "Golang", "Kotlin", "TypeScript", "PHP", "Perl", "SQL", "C++"]
print(lista[2:4])       # Irá gerar uma nova lista com os itens ["CSharp", "Golang"]
```

Os índices 2 e 4, significam: O índice de início e o índice final. Ainda podemos colocar um terceiro argumento, chamado `step`, que indica de quantos em quantos itens vamos mostrar
print(lista[::2])       # Irá mostrar a lista ["Python", "CSharp", "Kotlin", "PHP", "SQL"]

### Dicionários
#### Criação de dicionários
#### Acessando e alterando elementos de um dicionário
#### Adicionando e removendo elementos de um dicionário
#### Loop em dicionários
#### Copiando dicionários

## Exercícios laços de repetição

1. Calcule a soma de todos os números de 1 até o número informado. O usuário deve informar um número qualquer maior do que 0 e o programa deve retornar a soma de todos os números de 1 até esse número.
```python
Informe o número: 5
A soma de todos os números de 1 até 5 é 15
```
