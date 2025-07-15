# views/login_view.py

import tkinter as tk
from tkinter import messagebox
from controllers.auth_controller import autenticar_usuario
from utils.session import usuario_logado
# Remova o import do DashboardView do topo
# from views.dashboard_view import DashboardView

class LoginView:
    def __init__(self, master):
        self.master = master
        self.master.title("BioSync - Login")
        self.master.geometry("350x200")

        self.frame = tk.Frame(master)
        self.frame.pack(pady=20)

        # Usuário
        tk.Label(self.frame, text="Usuário").grid(row=0, column=0, pady=5)
        self.entry_username = tk.Entry(self.frame)
        self.entry_username.grid(row=0, column=1)

        # Senha
        tk.Label(self.frame, text="Senha").grid(row=1, column=0, pady=5)
        self.entry_senha = tk.Entry(self.frame, show="*")
        self.entry_senha.grid(row=1, column=1)

        # Botão Entrar
        self.btn_login = tk.Button(self.frame, text="Entrar", command=self.login)
        self.btn_login.grid(row=2, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.entry_username.get()
        senha = self.entry_senha.get()

        if autenticar_usuario(username, senha):
            messagebox.showinfo("Sucesso", "Login efetuado com sucesso!")
            self.frame.destroy()
            # Importe DashboardView aqui, dentro do método
            from views.dashboard_view import DashboardView
            DashboardView(self.master)
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos")