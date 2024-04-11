print("Inicio do programa")
num = int(input("Digite quantos nomes devem ser armazenados na lista: "))
lista = []
for i in range(num):
    nome = input("Digite qual o nome: ")
    lista.append(nome)
print(f"Os nomes são: {lista}")

for k in range(-1, -num-2, -1):
    print(lista[k])
print("Fim do programa")


