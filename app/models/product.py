class Product:
    def __init__(self, id, nome, quantidade, quantidade_minima):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.quantidade_minima = quantidade_minima

    def precisa_repor(self):
        return self.quantidade < self.quantidade_minima
