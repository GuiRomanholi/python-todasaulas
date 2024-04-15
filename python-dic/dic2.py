d1 = {
    "alunos": 40,
    "professor": "Antonio",
    "computadores": 43,
    "cadeiras": 43,
    "monitores": 43,
    "perifericos": {"computtadores": 43, "monitores": 43}
}
d1["sala_aula"] = 201

if "sala_aula" in d1:
    print("Existe a sala")
else:
    print("não existe")


d1.keys() # retorna o nome das etiquetas do dicionario {"alunos", "computadores", "cadeiras"}

# for chave in d1:
#     print(chave)

# chaves = list(d1.keys())
# tamanho = len(d1.keys())
# for i in range(tamanho):
#     chave = d1.keys()[i]
#     print(chave)

# for chave in d1.keys():
#     print(chave)
for chave in d1.keys():
    print(chave, "==>", d1[chave])
