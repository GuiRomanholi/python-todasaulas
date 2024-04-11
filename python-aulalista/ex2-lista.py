print("Program para calcular a média.")

lista = []

for i in range(5):
    print(f"por favor digite a {i+1} nota:")
    n = float(input())
    lista.append(n)

print("Lista:", lista)

soma = 0
for i in range(5):
    numero = lista[i]
    soma = soma + numero
    print("Numero: ", numero, "\tSoma: ", soma)
media = soma/3
print("Media:", media)