# Projeto Banco de Dados 2º Bimestre
## Explicação do Projeto
Meu projeto consiste em um app de compra de NFTs dividido em 4 telas:
- Tela de login/autenticação de usuários
- Tela de registro/criação de novos usuários
- Feed para exibir os NFTs e salvá-los no carrinho
- Carrinho

## Requisitos
Requisitos do projeto e onde eles foram satisfeitos:
- :white_check_mark: CRUD
  - :white_check_mark: CREATE (Criação de usuários/Adicionar ao carrinho)
  - :white_check_mark: READ (Visualizar itens do carrinho)
  - :white_check_mark: UPDATE (Editar carrinho)
  - :white_check_mark: DELETE (Remover itens do carrinho)
- :white_check_mark: 4 Telas no mínimo (login, registro, feed e carrinho)
- :white_check_mark: 3 Tabelas no mínimo (Usuários, NFTs e Compras)
- :white_check_mark: 2 Tabelas relacionadas no mínimo (Compra relaciona um Usuário e uma NFT)

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
  - Volte o terminal para a pasta principal digitando "**cd ..**" duas vezes
  - Instale as dependências do projeto com o comando "**pip install -r requirements.txt**"
  - Execute o arquivo "**main.py**"
 
## Sobre Escolhas
Caso você avalie o código irá reparar na existência de um arquivo chamado "LittleCar.py" representando o carrinho do sistema.
Em minha defesa, a vida é muito triste e é preciso um pouco de humor, então não me julgue por ter chamado o "carrinho" de "little car". Eu compreendo que o nome correto é "cart", que essa não é uma prática profissional e jamais faria isso em um ambiente sério.