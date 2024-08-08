lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

def divisiveu(numero):
    return numero % 3 == 0 or numero % 4 == 0

nova_lista = filter( divisiveu, lista)

print("Lista Principal: ")
print(lista)
print("Nova Lista: ")
print(list(nova_lista))