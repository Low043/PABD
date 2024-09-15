CREATE TABLE Secao(
	cod_secao SERIAL PRIMARY KEY,/*Define o código como serial (não é mais preciso indicar o código manualmente)*/
	nome varchar(50) not null
);

CREATE TABLE Livro(
	cod_livro SERIAL PRIMARY KEY,
	nome varchar(50) not null,
	cod_secao int,
	CONSTRAINT fk_secao FOREIGN KEY (cod_secao) references Secao (cod_secao)
);

INSERT INTO Secao (nome) VALUES ('Terror');
INSERT INTO Secao (nome) VALUES ('Romance');
INSERT INTO Secao (nome) VALUES ('Comédia');

INSERT INTO Livro (nome,cod_secao) VALUES ('Pé de cemitério',1);
INSERT INTO Livro (nome,cod_secao) VALUES ('Vilarejo de Rafael Mendes',1);
INSERT INTO Livro (nome,cod_secao) VALUES ('A seleção',2);
INSERT INTO Livro (nome,cod_secao) VALUES ('Epaminondas o gato explicador',3);

UPDATE Livro SET nome='Livro com nome alterado' WHERE cod_livro=4;/*Atualiza a tabela de livros alterando o nome onde o código do livro for 4*/
DELETE FROM Livro WHERE cod_livro=2;

SELECT * FROM Livro;/*Exibe tudo da tabela de Livros*/
/*Exibe tudo da tabela de Livros que esteja na seção de terror
SELECT * FROM Livro WHERE cod_secao=1
*/