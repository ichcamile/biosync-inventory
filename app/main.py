# app/main.py

import tkinter as tk
from views.login_view import LoginView
from utils.db import criar_tabelas

def iniciar_aplicacao():
    # Inicializa o banco de dados e cria tabelas, se necessário
    criar_tabelas()

    # Inicia a interface gráfica
    root = tk.Tk()
    root.title("BioSync - Inventory Control System")
    root.geometry("400x300")
    
    app = LoginView(root)
    root.mainloop()

if __name__ == "__main__":
    iniciar_aplicacao()
