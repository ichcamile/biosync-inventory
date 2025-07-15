# app/__init__.py

from app.utils.db import criar_conexao
from app.utils.session import SessaoUsuario

# Inicializa a conexão com o banco de dados
conexao = criar_conexao()

# Sessão global (poderá ser controlada pelas views de login)
sessao = SessaoUsuario()

# Você pode importar controladores ou modelos se quiser expor diretamente
# Exemplo:
# from app.controllers.auth_controller import login_usuario
