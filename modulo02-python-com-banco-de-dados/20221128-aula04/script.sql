PRAGMA foreign_keys = ON;

SELECT * FROM tb_usuarios tu ;
SELECT * FROM tb_perfis tp ;
SELECT * FROM tb_postagens tpo ;
SELECT * FROM tb_categorias tc ;
SELECT * FROM tb_postagens_categorias tpc ;


INSERT INTO tb_usuarios (email, senha) VALUES
	("maria@email.com", "123"),
	("jose@email.com", "123"),
	("elena@email.com", "123");

INSERT INTO tb_perfis (id, nome) VALUES (1, "Maria");
INSERT INTO tb_perfis (id, nome) VALUES (2, "José");


INSERT INTO tb_postagens (id_usuario, titulo, texto) VALUES
	(1, "Python", "Python é legal"),
	(1, "SQL", "SQL é muito útil"),
	(1, "Java", "Java é robusto"),
	(2, "Golang", "Golang é rápido"),
	(2, "PHP", "PHP é popular");

/* Utilização do JOIN para selecionar dados de 2 tabelas */

SELECT tp.nome, tpo.titulo, tpo.texto FROM tb_perfis tp
INNER JOIN tb_postagens tpo ON tp.id == tpo.id_usuario
WHERE tp.id = 2;

INSERT INTO tb_categorias (nome) VALUES
	("Programação"),
	("Python"),
	("Banco de dados"),
	("Java"),
	("2022"),
	("PHP"),
	("Golang"),
	("TI"),
	("Proway");

/* Associando as categorias a postagens */
INSERT INTO tb_postagens_categorias
	(id_postagem, id_categoria)
VALUES
	(2, 3),
	(2, 5),
	(2, 9);

/* Mostrar as categorias associadas a postagem de id 2 */
SELECT tpo.titulo, tpo.texto, tc.nome FROM tb_postagens tpo
INNER JOIN tb_postagens_categorias tpc ON tpo.id = tpc.id_postagem
INNER JOIN tb_categorias tc ON tc.id = tpc.id_categoria
WHERE tpo.id = 2;
