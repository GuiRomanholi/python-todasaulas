contador = 1
class No:
    lista = [x for x in range(50000)]
    proximo = None

if __name__ == "__main__":
    raiz = No()
    temp = raiz
    while True:
        print("Contador: ", contador)
        contador = contador + 1
        outro = No()
        raiz.proximo = outro
        temp = outro