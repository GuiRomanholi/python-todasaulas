print("program para calcular a média de crescimento anual de uma planta.")

lista = []
print("Foram quantos meses de pesguisa?")
qtd_meses = int(input())

for i in range(qtd_meses):
    print(f"Qual a altura da planta no {i+1} mês?")
    altura = float(input())
    lista.append(altura)
print("lista:", lista)

soma = 0
for i in range(qtd_meses):
    numero = lista[i]
    soma = soma + numero
    print("No mês", numero, "\t a soma é ", soma)
media = soma/qtd_meses
print("A média é", media)

