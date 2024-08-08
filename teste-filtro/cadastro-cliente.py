clientes = [
    {"nome": "João Silva", "idade": 24, "genero": "M"},
    {"nome": "Maria Silva", "idade": 25, "genero": "F"},
    {"nome": "Alberto", "idade": 30, "genero": "M"},
    {"nome": "Iracema", "idade": 23, "genero": "F"}
]



filtro_homens = lambda dicionario : dicionario['genero'] == "M"

filtro_mulheres = lambda dicionario : dicionario['genero'] == "F"

homens = filter(filtro_homens, clientes)
mulheres = filter(filtro_mulheres, clientes)


print("Todo Mundo: ")
print(clientes)

print("Apenas Homens: ")
print(list(homens))

print("Apenas Mulheres: ")
print(list(mulheres))
