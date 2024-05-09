class Cliente:
    def __init__(self):
        self.nome = "Desconhecido"
        self.cpf = "Desconhecido"
        self.idade = 0
    
    def comprar(self):
        print("Estou comprando um produto")

    def reclamar(self):
        print("Vim reclamar do produto")

    def trocar(self):
        print(f"{self.nome} está querendo trocar o produto")