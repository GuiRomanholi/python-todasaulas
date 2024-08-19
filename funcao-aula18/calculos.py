def somar(n1, n2):
    soma = n1 + n2
    print("Soma Realizada")
    return soma


def subtrair(n1, n2):
    subtracao = n1 - n2
    print("Subtracao realizada")
    return subtracao


if __name__ == "__main__":
    print("Digite um numero: ")
    num1 = float(input())
    print("Digite segundo numero: ")
    num2 = float(input())
    resultado_soma = somar(num1,num2)
    print("O resultado é: ", resultado_soma)
