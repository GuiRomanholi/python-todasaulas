
def digite_numero(texto = "Digite um número: "):
    """
        Função utilizada para pedir numero inteiro,
        e verifica se o valor digitado é um número válido
    """
    valido = False
    while not valido:
        digitado = input(texto)
        try:
            numero = int(digitado)
            valido = True
        except:
            print("Tá errado pae.")
    return numero

print("inicio programa")
n1 = digite_numero("Digite o 1 numero: ")
n2 = digite_numero("Digite o 2 numero: ")
soma = n1 + n2
print("A soma é ", soma)
print("Termino programa")