"""
Entrada e saída de arquivos txt
I/O de arquivos (Input/Output)

Escrita em arquivos txt

"""

import os

pasta_alunos = os.path.join(os.getcwd(), "alunos")

if __name__ == "__main__":

    # Para abrirmos um arquivo para escrita, precisamos passar o argumento "w" para a função open()

    # with é o gerenciador de contexto do Python
    # Com o with, não precisamos chamar o método close() para fechar o arquivo. Depois que o bloco
    # de código do with é executado, o arquivo é fechado automaticamente.
    # Funciona para qualquer modo de leitura

    with open(os.path.join(pasta_alunos, "inicio.txt"), "w", encoding="utf-8") as arquivo:
        # O modo de abertura w é utilizado para somente-escrita em arquivos
        # Se o arquivo não existir, ele será criado
        # Se o arquivo existir, o seu conteúdo será truncado(apagado) e o novo conteúdo
        # será escrito por cima
        mensagem = input("Informe o seu nome: ")

        # write() Recebe uma string que será escrita no arquivo
        # O \n é um caractere especial de quebra de linha (ENTER)
        # O \t é o caractere especial que representa o espaçamento (TAB)
        arquivo.write(f"Ola {mensagem}\n")

        mensagens = ["Python é legal\n", "Java é difícil\n", "Javascript é legal\n"]
        # writelines() Recebe uma lista de strings que serão escritas no arquivo
        arquivo.writelines(mensagens)

    with open(os.path.join(pasta_alunos, "inicio.txt"), "w", encoding="utf-8") as arquivo:
        arquivo.write("Sobrescrito\n")

    # Temos também o modo append
    # No caso do modo append, se um arquivo não existir, ele é criado, e se ele existir
    # o cursor é movido para o seu final, para que sejam escritos novos dados

    with open(os.path.join(pasta_alunos, "inicio.txt"), "a", encoding="utf-8") as arquivo:
        for contador in range(10):
            arquivo.write(str(contador))

    # Caso precisemos abrir um arquivo em modo leitura e escrita, utilizamos o sinal de + depois
    # do modo (w+, r+ ou a+)
    with open(os.path.join(pasta_alunos, "inicio.txt"), mode="r+", encoding="utf-8",) as arquivo:
        pass
