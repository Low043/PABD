CREATE TABLE Departamento(
    codigo int,
    CONSTRAINT pk_departamento PRIMARY KEY (codigo)
)

CREATE TABLE Cliente(
    codigo int,
    nome varchar(50) not null,
    endereco varchar(150) not null,
    cod_departamento int,
    CONSTRAINT pk_cliente PRIMARY KEY (codigo),
    CONSTRAINT fk_cliente FOREIGN KEY (cod_departamento) references Departamento (codigo)
);