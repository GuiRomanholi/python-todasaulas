#crie um programa que calcule a média das notas de um aluno, o resto ele botou la e eu fiz
print("Program para calcular a média.")

lista = []

print("por favor digite a primeira nota")
n = float(input())
lista.append(n)

print("Digite a segunda nota")
n = float(input())
lista.append(n)

print("Digite a terceira nota")
n = float(input())
lista.append(n)

media = (lista[0] + lista[1] + lista[2])/3.0
print(media)