
import sqlite3

if __name__ == "__main__":
    conexao = sqlite3.connect("aula05_db.sqlite3")

    comando = "SELECT * FROM tb_contatos_naonormalizada"

    # Criamos o cursor que irá navegar entre os registros
    cursor = conexao.cursor()

    # Atribuímos o objeto cursor a variável resultado
    resultado = cursor.execute(comando)

    contatos = resultado.fetchall()

    print(contatos)

    for contato in contatos:
        nome = contato[1]
        endereco = contato[2].split(", ")
        telefones = contato[3].split(", ")

        tipo_logradouro = endereco[0].split(" ")[0]
        logradouro = ' '.join(endereco[0].split(" ")[1:])
        numero = endereco[1]
        bairro = endereco[2]
        cidade = endereco[3]
        uf = endereco[4]

        comando = f"""
        INSERT INTO tb_contatos(nome, tipo_logradouro, logradouro, numero, bairro, cidade, uf)
        VALUES (
            '{nome}',
            '{tipo_logradouro}',
            '{logradouro}',
            '{numero}',
            '{bairro}',
            '{cidade}',
            '{uf}'
        )
        """
        cursor.execute(comando)
        conexao.commit()

        contato_id = cursor.lastrowid

        for telefone in telefones:
            comando = f"""
            INSERT INTO tb_telefones(id_contato, telefone) VALUES ('{contato_id}', '{telefone}')
            """
            cursor.execute(comando)
            conexao.commit()
