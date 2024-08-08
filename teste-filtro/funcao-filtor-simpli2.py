lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]


filtro = lambda numero : numero % 3 == 0 or numero % 4 == 0
print("-"*50)
print("Teste do filtro com o numero 16: ", filtro(16))
print("-"*50)

nova_lista = filter( filtro, lista)

print("Lista Principal: ")
print(lista)
print("-"*50)
print("Nova Lista: ")
print(list(nova_lista))