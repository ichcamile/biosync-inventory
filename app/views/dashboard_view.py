import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from utils.session import sessao, limpar_sessao, usuario_logado, is_admin
from controllers.product_controller import listar_produtos
from views.login_view import LoginView

class DashboardView:
    def __init__(self, master):
        self.master = master
        self.master.title("BioSync - Dashboard")
        self.master.geometry("600x400")

        self.frame = tk.Frame(master)
        self.frame.pack(pady=20)

        # Botões
        self.btn_gerenciar_produtos = tk.Button(self.frame, text="Gerenciar Produto Selecionado", width=25, command=self.abrir_produto_selecionado)
        self.btn_gerenciar_produtos.grid(row=1, column=0, padx=10, pady=10)

        self.btn_novo_produto = tk.Button(self.frame, text="Adicionar Novo Produto", width=25, command=self.abrir_novo_produto)
        self.btn_novo_produto.grid(row=1, column=1, padx=10, pady=10)

        self.btn_sair = tk.Button(self.frame, text="Sair", width=20, command=self.logout)
        self.btn_sair.grid(row=1, column=2, padx=10, pady=10)

        # Tabela de produtos
        self.tree = ttk.Treeview(self.frame, columns=("id", "nome", "quantidade", "minima"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("quantidade", text="Quantidade")
        self.tree.heading("minima", text="Qtd. Mínima")
        self.tree.column("id", width=50)
        self.tree.grid(row=2, column=0, columnspan=3, pady=20)
        self.atualizar_tabela()

    def atualizar_tabela(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        produtos = listar_produtos()
        for p in produtos:
            destaque = ""
            if p['quantidade'] < p['quantidade_minima']:
                destaque = " (ABAIXO DO MÍNIMO!)"
            self.tree.insert("", "end", values=(p['id'], p['nome'] + destaque, p['quantidade'], p['quantidade_minima']))

    def abrir_produto_selecionado(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um produto na tabela.")
            return
        item = self.tree.item(selecionado[0])
        produto_id = item['values'][0]
        from views.product_view import ProductView
        ProductView(tk.Toplevel(self.master), produto_id, self.atualizar_tabela)

    def abrir_novo_produto(self):
        from views.product_view import ProductView
        ProductView(tk.Toplevel(self.master), None, self.atualizar_tabela)

    def logout(self):
        limpar_sessao()
        messagebox.showinfo("Logout", "Você saiu da aplicação.")
        self.frame.destroy()
        LoginView(self.master)