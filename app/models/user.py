class User:
    def __init__(self, id, nome, username, senha, perfil):
        self.id = id
        self.nome = nome
        self.username = username
        self.senha = senha
        self.perfil = perfil

    def is_admin(self):
        return self.perfil == 'admin'
