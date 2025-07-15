import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from controllers.product_controller import listar_produtos, cadastrar_produto, atualizar_produto, deletar_produto
from views.login_view import LoginView

class ProductView:
    def __init__(self, master, produto_id=None, atualizar_callback=None):
        self.master = master
        self.master.title("Gerenciar Produto")
        self.atualizar_callback = atualizar_callback
        self.master.geometry("400x300")

        self.produto_id = produto_id
        self.produto = None
        if produto_id is not None:
            produtos = listar_produtos()
            for p in produtos:
                if p['id'] == produto_id:
                    self.produto = p
                    break

        self.frame = tk.Frame(master)
        self.frame.pack(pady=20)

        # Campos
        tk.Label(self.frame, text="Nome do Produto").grid(row=0, column=0)
        self.entry_nome = tk.Entry(self.frame)
        self.entry_nome.grid(row=0, column=1)

        tk.Label(self.frame, text="Quantidade").grid(row=1, column=0)
        self.entry_quantidade = tk.Entry(self.frame)
        self.entry_quantidade.grid(row=1, column=1)

        tk.Label(self.frame, text="Qtd. Mínima").grid(row=2, column=0)
        self.entry_minima = tk.Entry(self.frame)
        self.entry_minima.grid(row=2, column=1)

        # Preenche campos se for edição
        if self.produto:
            self.entry_nome.insert(0, self.produto['nome'])
            self.entry_quantidade.insert(0, str(self.produto['quantidade']))
            self.entry_minima.insert(0, str(self.produto['quantidade_minima']))

        # Botões
        if self.produto:
            self.btn_salvar = tk.Button(self.frame, text="Salvar Alterações", command=self.salvar)
            self.btn_salvar.grid(row=3, column=0, pady=10)
            self.btn_deletar = tk.Button(self.frame, text="Deletar Produto", command=self.deletar)
            self.btn_deletar.grid(row=3, column=1, pady=10)
        else:
            self.btn_cadastrar = tk.Button(self.frame, text="Cadastrar Produto", command=self.cadastrar)
            self.btn_cadastrar.grid(row=3, column=0, columnspan=2, pady=10)

    def cadastrar(self):
        nome = self.entry_nome.get()
        quantidade = self.entry_quantidade.get()
        minima = self.entry_minima.get()
        if not nome or not quantidade or not minima:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return
        if cadastrar_produto(nome, int(quantidade), int(minima)):
            messagebox.showinfo("Sucesso", "Produto cadastrado!")
            if self.atualizar_callback:
                self.atualizar_callback()
            self.master.destroy()
        else:
            messagebox.showerror("Erro", "Falha ao cadastrar produto.")

    def salvar(self):
        nome = self.entry_nome.get()
        quantidade = self.entry_quantidade.get()
        minima = self.entry_minima.get()
        if not nome or not quantidade or not minima:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return
        if atualizar_produto(self.produto_id, nome, int(quantidade), int(minima)):
            messagebox.showinfo("Sucesso", "Produto atualizado!")
            if self.atualizar_callback:
                self.atualizar_callback()
            self.master.destroy()
        else:
            messagebox.showerror("Erro", "Falha ao atualizar produto.")

    def deletar(self):
        if messagebox.askyesno("Confirmação", "Tem certeza que deseja deletar este produto?"):
            if deletar_produto(self.produto_id):
                messagebox.showinfo("Sucesso", "Produto deletado!")
                if self.atualizar_callback:
                    self.atualizar_callback()
                self.master.destroy()
            else:
                messagebox.showerror("Erro", "Falha ao deletar produto.")