
class Contato:
    def __init__(self, nome : str = "",
                 telefone : str = "",
                 email : str = ""):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def dicionario(self) -> dict:
        contato_dicionario = {"nome": self.nome,
                              "telefone": self.telefone,
                              "email": self.email}
        return contato_dicionario

    def __str__(self) -> str :
        texto = f"""Nome: {self.nome}\t
        Telefone:{self.telefone}\t
        Email:{self.email}"""
        return texto

