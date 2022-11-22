"""
Entrada e saída de arquivos txt
I/O de arquivos (Input/Output)

Leitura de arquivos txt

"""

import os

if __name__ == "__main__":

    # Para abrir arquivos pelo python, utilizamos a função built-in open()
    # Temos que passar como argumentos o arquivo que deve ser aberto e o modo de abertura
    # Se o modo de abertura não for informado, o Python abrirá automaticamente esse arquivo
    # como somente-leitura.
    # A função open() retorna o objeto que representará esse arquivo.

    # os.path.join() -> Ela concatena nomes de diretórios e nomes de arquivos, garantindo assim
    # que o caminho até o arquivo esteja correto
    # os.getcwd() retorna o caminho completo até o diretório de onde o script está sendo
    # executado
    arquivo = open(os.path.join(os.getcwd(), "log.txt"), encoding="utf-8")

    # Podemos ler arquivos texto no python de 4 maneiras diferentes

    # Usando o método read(n)
    # n significa quantos caracteres serão lidos. Se não for passado, lê o arquivo inteiro
    # read() retorna uma string com o conteúdo lido
    print(arquivo.read())

    # Método readline(n)
    # Lê uma linha inteira do arquivo até a quantidade de caracteres informada
    print(arquivo.readline())

    # A linha acima não imprime nada, pois o cursor do arquivo está no final dele (pois chamamos)
    # o método read(). Podemos verificar a posição atual do cursor utilizando o método
    # tell
    print(arquivo.tell())

    # Se quisermos ler o arquivo novamente, precisamos "rebobinar" esse cursor até o início do
    # arquivo (posição 0). Utilizamos o método seek() para isso
    arquivo.seek(0)

    print(arquivo.readline(10))
    print(arquivo.readline())

    # readlines()
    # Lê as linhas do arquivo e retorna como itens de uma lista
    print(arquivo.readlines(100))

    # Sempre que abrimos um arquivo, devemos fechá-lo
    arquivo.close()
