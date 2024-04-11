lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for item in lista:
    if item % 3 == 0:
        lista.remove(item)
print(lista)