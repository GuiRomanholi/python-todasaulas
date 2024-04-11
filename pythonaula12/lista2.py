
try:
    n1 = float(input("Digite um numero: "))
    n2 = float(input("Digite outro numero: "))
    resultado = n1/n2
    print(f"O resultado de {n1} e {n2} é = {resultado}")
except ValueError as err:
    print("Erro! Digite um numero válido.")
except ZeroDivisionError as err:
    print("Erro! Informe um número diferente de zero.")
except:
    print("ERRO! Não foi possivel executar a divisão")