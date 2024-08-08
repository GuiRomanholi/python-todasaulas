lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

def divisiveu(numero):
    if numero % 3 == 0:
        return True
    elif numero % 4 == 0:
        return True
    else:
        return False



nova_lista = filter( divisiveu, lista)

print("Lista Principal: ")
print(lista)
print("Nova Lista: ")
print(list(nova_lista))