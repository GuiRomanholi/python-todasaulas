
import json
import requests
from Contato import Contato

class ContatoService:
    def __init__(self):
        self.URL_BASE = "https://dtspm-327f2-default-rtdb.firebaseio.com"

    def salvar(self, contato : Contato) -> bool:
        response = requests.post(url=f"{self.URL_BASE}/contatos.json",
                      json=contato.dicionario(), timeout=5.0)
        return response.status_code == 200

    def ler_todos(self) -> list:
        response = requests.get(url=f"{self.URL_BASE}/contatos.json", timeout=5.0)
        lista = []
        if response.status_code == 200:
            dicionario = json.loads(response.text)
            for item in dicionario.items():
                # print(item)
                contato_dict = item[1]
                c1 = Contato(nome=contato_dict.get("nome", ""),
                             email=contato_dict.get("email", ""),
                             telefone=contato_dict.get("telefone", ""))
                lista.append( c1 )
        return lista
