clientes = [
    {"nome": "João Silva", "idade": 24, "genero": "M"},
    {"nome": "Maria Silva", "idade": 25, "genero": "F"},
    {"nome": "Alberto", "idade": 30, "genero": "M"},
    {"nome": "Iracema", "idade": 23, "genero": "F"}
]

tranforma_nome = lambda d : d["nome"]

nomes_clientes = map(tranforma_nome , clientes)

print("Lista clientes: ")
print(clientes)
print("Só os nomes na lista: ")
print(list(nomes_clientes))