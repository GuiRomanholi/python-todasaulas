print("Inicio do programa")
lista = []

for i in range(3):
    dic = {}
    nome = input("Qual o nome do produto? ")
    cor = input("Qual a cor do produto? ")
    preco = float(input("Qual o preço do produto? "))
    unidade_medida = input("Qual a unidade de medida do produto? ")
    dic = {"Nome": nome, "Cor": cor, "Preço": preco, "Unidade de medida": unidade_medida}
    lista.append(dic)

for p in lista:
    print("Produto: ", p["nome"])
    print(f"Cor: {p['cor']}  Preço: {p['preco']}  Nome: {['nome']}")