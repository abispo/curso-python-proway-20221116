-- ATENÇÃO: A sintaxe abaixo é do banco SQLite

/*
 * 2FN - Segunda Forma Normal
 *
 * Segunda Forma normal é baseada no conceito de Dependência Funcional Total
 * Para estar na 2FN, uma tabela precisa:
 * - Estar na 1FN
 * - Todo atributo não chave da tabela deve ser dependente de todas as partes da chave primária
 * - Caso exista um atributo que dependa parcialmente da chave, esse atributo deve estar em
 * outra tabela
 */

-- Exemplo de tabela fora da 2FN

CREATE TABLE IF NOT EXISTS tb_itens(
	id INTEGER,
	id_fornecedor INTEGER,
	uf_fornecedor TEXT NOT NULL,
	telefone_fornecedor TEXT NOT NULL,
	qtd_estoque INT NOT NULL,
	PRIMARY KEY(id, id_fornecedor)
);

INSERT INTO tb_itens (id, id_fornecedor, uf_fornecedor, telefone_fornecedor, qtd_estoque) VALUES
	(1001, 10, "SP", "23784449", 150),
	(1002, 10, "SP", "23784449", 90),
	(1002, 11, "CE", "28900198", 12);

SELECT * FROM tb_itens ti ;

/*
 * Como visto, os campos uf_fornecedor e telefone_fornecedor estão dentro do mesmo domínio que
 * id_fornecedor, ou seja, dependem apenas de 1 lado da chave primária.
 * Nesse caso, precisamos remover esses campos da tabela de itens e colocá-los em outra tabela,
 * que no caso chamaremos de tb_fornecedores
 */

CREATE TABLE IF NOT EXISTS tb_fornecedores(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	uf_fornecedor TEXT NOT NULL,
	telefone_fornecedor TEXT NOT NULL
);

-- Renomear a tb_itens para criação da nova tb_itens
ALTER TABLE tb_itens RENAME TO tb_itens_naonormalizada;

-- Criar a nova tabela tb_itens já com a 2FN aplicada
CREATE TABLE IF NOT EXISTS tb_itens(
	id INTEGER NOT NULL,
	id_fornecedor INTEGER NOT NULL,
	qtd_estoque INTEGER NOT NULL,
	PRIMARY KEY (id, id_fornecedor),
	FOREIGN KEY (id_fornecedor) REFERENCES tb_fornecedores(id)
);

SELECT * FROM tb_fornecedores ;
SELECT * FROM tb_itens ti ;
