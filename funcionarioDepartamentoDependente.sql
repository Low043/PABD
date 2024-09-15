CREATE TABLE Departamento(
    codigo int,
    descricao varchar(200),
    CONSTRAINT pk_departamento PRIMARY KEY (codigo)
);

CREATE TABLE Funcionario(
    codigo int,
    nome varchar(50),
    endereco varchar(150),
    telefone int,
    cod_departamento int,
    CONSTRAINT pk_funcionario PRIMARY KEY (codigo),
    CONSTRAINT fk_funcionario FOREIGN KEY (cod_departamento) references Departamento (codigo)
);

CREATE TABLE Dependente(
    codigo int,
    codigo_funcionario int,
    nome varchar(50),
    data_nascimento int,
    CONSTRAINT pk_dependente PRIMARY KEY (codigo),
    CONSTRAINT fk_dependente FOREIGN KEY (codigo_funcionario) references Funcionario (codigo)
);