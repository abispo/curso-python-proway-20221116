-- ATENÇÃO: A sintaxe abaixo é do banco SQLite

/*
 * 3FN - Terceira Forma Normal
 *
 * Baseada no conceito de dependência transitiva
 * A tabela não deve ter um atributo não chave dependente de outro atributo não chave
 *
 * Para estar na 3FN, uma tabela deve:
 * 	- Estar na 2FN.
 * 	- Não podem existir dependências transitivas
 */

CREATE TABLE IF NOT EXISTS tb_pedidos_itens(
	id_pedido INTEGER NOT NULL,
	id_item INTEGER NOT NULL,
	quantidade INTEGER NOT NULL,
	valor_unitario REAL NOT NULL,		-- REAL = FLOAT
	subtotal REAL NOT NULL
);

SELECT * FROM tb_pedidos_itens ;

INSERT INTO tb_pedidos_itens (id_pedido, id_item, quantidade, valor_unitario, subtotal) VALUES
	(1, 20, 3, 3.59, 3.59 * 3),
	(1, 21, 5, 1.19, 1.19 * 5),
	(1, 49, 11, 0.68, 0.68 * 11);

/*
 * A coluna subtotal depende do resultado da multiplicação entre as colunas quantidade e valor_unitario
 * Ou seja, temos um atributo não chave da tabela dependendo de outro(s) atributo(s) não chave.
 * Nesse caso, devemos excluir a coluna subtotal, e fazer esse cálculo na hora em que estivermos
 * trazendo as informações da tabela
 */

-- 1: Excluir a coluna subtotal
ALTER TABLE tb_pedidos_itens DROP COLUMN subtotal ;

/*
 * 2: Fazer a operação de multiplicação e apresentar como a coluna subtotal, utilizando 'AS'
 * A coluna "subtotal" existirá apenas enquanto o comando SELECT estiver sendo executado.
 * Ou seja, ela não existe fisicamente na tabela
 */
SELECT
	id_pedido, id_item, quantidade, valor_unitario, quantidade * valor_unitario AS "subtotal"
FROM tb_pedidos_itens;
