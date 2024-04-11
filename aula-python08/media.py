print("Bom dia, hoje vamos calcular a média do aluno. Por favor responda as seguintes questões.")
while True:
    print("Qual o nome do aluno?")
    nome = input()
    print("Qual a primeira nota do aluno?")
    n1 = float(input())
    print("Qual a segunda nota do aluno?")
    n2 = float(input())
    print("Qual a terceira nota do aluno?")
    n3 = float(input())
    media = (n1 + n2 + n3)/3
    print(f"A média do aluno é {media}, e seu nome é {nome}.")
    print("Deseja repetir a pergunta? (S/N)")
    if input() == "N":
        break
print("Fim do programa")


