# Projeto Banco de Dados 2º Bimestre
## Explicação do Projeto
Meu projeto consiste em um app de aluguel de imóveis dividido em 4 telas:
- Tela de login/autenticação de usuários
- Feed para exibir as casas e alugá-las por certo período
- "Carrinho" onde se pode ver e editar alugueis feitos
- Tela para colocar casas para alugar

## Requisitos
Requisitos do projeto e onde eles foram satisfeitos:
- :white_check_mark: CRUD
  - :white_check_mark: CREATE (Adicionar casas para alugar)
  - :white_check_mark: READ (Visualizar casas alugadas pelo usuário)
  - :white_check_mark: UPDATE (Editar período de aluguel)
  - :white_check_mark: DELETE (Remover casa)
- :white_check_mark: 4 Telas no mínimo (login, feed, "carrinho" e alugar)
- :white_check_mark: 3 Tabelas no mínimo (Usuários, Casas e Alugueis)
- :white_check_mark: 2 Tabelas relacionadas no mínimo (Aluguel relaciona um Usuário e uma Casa)

## Como Executar
- Opção 1 (Executável):
  - Abra o último Release no lado direito do Github
  - Instale o executável
  - Execute-o (Pode ser necessário dar permissão para o programa ser executado)
- Opção 2 (Código):
  - Baixe o .zip do código clicando em "**<> code**"
  - Extraia o arquivo e abra a pasta por um editor de código
  - Abra a pasta extraída com o Terminal pelo editor ou Prompt de Comando
  - Inicie o ambiente virtual com o comando "**python -m venv .venv**"
  - Após iniciar o ambiente, ative-o com a seguinte sequência de comandos:
    - "**cd .venv**"
    - "**cd Scripts**"
    - "**./activate**"
    OBS: Em alguns casos, o terminal não possui permissão de executar ./activate, este erro pode ser resolvido digitando "**Set-ExecutionPolicy RemoteSigned**" no PowerShell do Windows em modo de administrador.
  - Volte o terminal para a pasta principal digitando "**cd ..**" duas vezes
  - Instale as dependências do projeto com o comando "**pip install -r requirements.txt**"
  - Execute o arquivo "**main.py**"

## Fazer Login
O programa não possui nenhum método para criar usuários, porém, são criados dois usuários de teste junto ao banco de dados, são eles:
- `Daniel` senha: `pabd`
- `Luis` senha: `desalojado`

> [!WARNING]  
> Para que o programa funcione perfeitamente é necessário que se tenha o **PostgreSQL** instalado e gonfigurado com a senha "**pabd**". Caso seu Postgres esteja configurado de maneira diferente você deverá editar o arquivo **"src/services/builder.py"** para que coincida com suas configurações. **Mesmo que o banco de dados não tenha sido criado, o próprio programa se encarregará de criá-lo.**