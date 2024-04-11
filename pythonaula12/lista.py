lista = ["João", "Maria", "Pedro"]
print(lista)

lista.append("josé")
lista.insert(1, "Matheus")
print("Lista com Matheus: ", lista)

lista.remove("Pedro")
print("Lista sem o Pedro: ", lista)

lista.append("Luís")
print(f"Lista com Luís: {lista}")

tamanho = len(lista)
print(f"O tamanho é {tamanho}")

lista.pop(3)
print(f"Lista sem o José: {lista}")

try:
    onde_esta_maria = lista.index("Maria")
    print(f"A Maria está na posição {onde_esta_maria}")
except ValueError:
    print("Elemento não encontrado")

