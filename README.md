# BioSync - Controle de Estoque

## Objetivo
Aplicação para controle de estoque de produtos com cadastro, movimentação, alertas e controle de usuários (administrador e comum).

## Tecnologias
- Python 3.11+
- Tkinter (interface gráfica)
- MySQL (banco de dados)
- bcrypt (criptografia de senha)

## Estrutura do Projeto
- `main.py`: ponto de entrada da aplicação
- `controllers/`: lógica do negócio (autenticação, produtos)
- `models/`: modelos de dados
- `views/`: interfaces gráficas
- `utils/`: conexão DB, validações, controle de sessão
- `.env`: configurações de conexão com banco
- `create_tables.sql`: script SQL para criar banco e tabelas

## Como usar
1. Configure seu banco MySQL com o script `create_tables.sql`.
2. Preencha o arquivo `.env` com suas credenciais.
3. Instale dependências: `pip install mysql-connector-python bcrypt`
4. Execute: `python main.py`

## Fluxograma
(Inserir imagem do fluxograma aqui, feita no draw.io ou outra ferramenta)
