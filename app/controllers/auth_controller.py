# app/controllers/auth_controller.py

import bcrypt
from utils.db import conectar
from utils.session import criar_sessao

def autenticar_usuario(username, senha):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    usuario = cursor.fetchone()

    cursor.close()
    conn.close()

    if usuario and bcrypt.checkpw(senha.encode(), usuario["senha"].encode()):
        criar_sessao(usuario)
        return True, usuario
    else:
        return False, None


def cadastrar_usuario(username, senha, perfil):
    conn = conectar()
    cursor = conn.cursor()

    # Criptografa a senha
    senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()

    query = "INSERT INTO users (username, senha, perfil) VALUES (%s, %s, %s)"
    try:
        cursor.execute(query, (username, senha_hash, perfil))
        conn.commit()
        sucesso = True
    except Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")
        sucesso = False
    finally:
        cursor.close()
        conn.close()

    return sucesso
