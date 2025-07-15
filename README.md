
# 💊 BioSync - Sistema de Controle de Estoque

## 🎯 Objetivo

O **BioSync** é uma aplicação desktop desenvolvida em **Python**, com interface gráfica em **Tkinter** e banco de dados **MySQL**, voltada para o controle de estoque de produtos e materiais.  
Ela permite o cadastro, movimentação (entrada e saída), alertas automáticos e controle de usuários com níveis de acesso (administrador e comum).

## 🧰 Tecnologias Utilizadas

- Python 3.11+
- Tkinter (interface gráfica)
- MySQL (banco de dados relacional)
- bcrypt (criptografia de senha)
- dotenv (variáveis de ambiente)

## 📁 Estrutura do Projeto

```

biosync-inventory/
├── app/
│   ├── main.py                 # Ponto de entrada da aplicação
│   ├── config.py               # Configuração via .env
│   ├── controllers/            # Regras de negócio (auth e produto)
│   ├── models/                 # Acesso ao banco
│   ├── views/                  # Telas (Tkinter)
│   └── utils/                  # Sessão, validações, conexão DB
├── .env                        # Variáveis de conexão com o banco
├── create\_tables.sql           # Script SQL para criar banco e dados iniciais
└── docs/
├── README.md               # Documentação
└── fluxograma.png          # Fluxograma do sistema (inserir imagem)

````

## ▶️ Como usar

### 1. Criar o banco de dados
Execute o script `create_tables.sql` no seu MySQL:

```bash
mysql -u root -p < create_tables.sql
````

Isso criará as tabelas e incluirá um usuário admin de testes.

### 2. Configurar o `.env`

Crie um arquivo `.env` na raiz do projeto com os dados de conexão do seu MySQL:

```
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=biosync_db
```

### 3. Instalar dependências

No terminal, execute:

```bash
pip install mysql-connector-python bcrypt python-dotenv
```

### 4. Executar o sistema

Acesse a pasta `app/` e rode:

```bash
python main.py
```

Ou, se preferir rodar como pacote (recomendado):

```bash
python -m app.main
```


## 🔐 Usuário de Testes

Use as credenciais abaixo para acessar o sistema:

* **Usuário:** `admin`
* **Senha:** `admin123`


## 📌 Funcionalidades

* Autenticação com senhas criptografadas
* Perfis de usuário (administrador e comum)
* Cadastro, listagem e edição de produtos
* Registro de entradas e saídas de estoque
* Alerta visual para produtos abaixo da quantidade mínima
* Interface amigável com campos validados


## 👩‍💻 Desenvolvido por

Camile Santana
Projeto acadêmico de aplicação real com integração completa entre front-end e banco de dados.


