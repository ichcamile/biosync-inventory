# utils/session.py

sessao = {
    "usuario": None
}

def criar_sessao(usuario):
    sessao["usuario"] = usuario

def limpar_sessao():
    sessao["usuario"] = None

def usuario_logado():
    return sessao["usuario"] is not None

def is_admin():
    return sessao["usuario"] and sessao["usuario"]["perfil"] == "admin"
