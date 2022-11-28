PRAGMA foreign_keys = ON;

SELECT * FROM tb_usuarios tu ;
SELECT * FROM tb_perfis tp ;
SELECT * FROM tb_postagens tpo ;


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
INNER JOIN tb_postagens tpo ON tp.id == tpo.id_usuario ;

