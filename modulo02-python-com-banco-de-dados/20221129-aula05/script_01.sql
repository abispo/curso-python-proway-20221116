-- ATENÇÃO: A sintaxe abaixo é do banco SQLite

/*
1FN - Primeira Forma Normal.

Dizemos que uma tabela está na Primeira Forma Normal, quando:
	- Possui uma chave primária
	- Ela não possui atributos multivalorados
			- (os valores dos atributos devem ser atômicos, ou indivisíveis)
	- E não possui atributos compostos
*/

-- Exemplo de tabela fora da 1FN

CREATE TABLE IF NOT EXISTS tb_contatos(
	id INTEGER NOT NULL,
	nome TEXT NOT NULL,
	endereco TEXT NOT NULL,
	telefone TEXT NOT NULL
);

-- Inserindo alguns registros
INSERT INTO tb_contatos (id, nome, endereco, telefone) VALUES
	(2, "João", "Rua dez, 1000, Garcia, Blumenau, SC", "47998763331"),
	(3, "José", "Rua quinze, 16, Ponta Aguda, Blumenau, SC", "47988780123, 23401865"),
	(4, "Maria", "Rua do Bosque, 98, Vila Itoupava, Blumenau, SC", "47980134442, 29999873");

SELECT * FROM tb_contatos;

-- Renomeando a tabela tb_contatos
ALTER TABLE tb_contatos RENAME TO tb_contatos_naonormalizada;

-- Aplicando as regras da 1FN
/*
 * Definimos a coluna id como chave primária
 * Retiramos a coluna telefones, e criamos a tabela tb_telefones para armazenar os múltiplos
 * valores de telefone, removendo assim a coluna multivalorada
 * 'Quebramos' o campo composto endereco em vários outros campos (logradouro, numero, etc)
 */
CREATE TABLE IF NOT EXISTS tb_contatos(
	-- Definir um campo como chave primária
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	tipo_logradouro TEXT NOT NULL,
	logradouro TEXT NOT NULL,
	numero TEXT NOT NULL,
	bairro TEXT NOT NULL,
	cidade TEXT NOT NULL,
	uf TEXT NOT NULL
);

/*
 * Aqui criamos uma tabela para armazenar os dados de telefone dos contatos. Dessa maneira
 * podemos retirar o atributo multivalorado 'telefone' da tabela tb_contatos
 */
CREATE TABLE IF NOT EXISTS tb_telefones(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_contato INTEGER NOT NULL,
	telefone TEXT NOT NULL,
	FOREIGN KEY (id_contato) REFERENCES tb_contatos (id)
);

SELECT * FROM tb_contatos tc ;
SELECT * FROM tb_telefones;

-- Para converter os dados, rode o arquivo script_01.py
