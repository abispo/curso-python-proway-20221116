"""
Script para criação do banco de dados e das tabelas

"""

import sqlite3

if __name__ == "__main__":

    # Primeira coisa a fazer é criar a conexão com o banco de dados
    conexao = sqlite3.connect("db.sqlite3")

    # O comando CREATE é usado para criar uma nova tabela no banco
    # CREATE TABLE é um comando DDL (Data Definition Language)
    comando = """
    CREATE TABLE IF NOT EXISTS tb_contatos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        sobrenome TEXT NOT NULL,
        telefone TEXT NOT NULL,
        email TEXT
    )
    """

    # Executamos o comando SQL definido anteriormente
    conexao.execute(comando)
