#Faça um programa usando laços para desenhar um retangulo na tela
print("-----------------------")
for i in range(0, 5, 1):
    print("######")
print("-----------------------")

#Faça um programa usando laços para desenhar um retangulo na tela solicitando que o usuario informe#

print("Quantas linhas?")
linha = int(input())

print("Quantas colunas?")
coluna = int(input())

for i in range(0, linha, 1):
    print("#"*coluna)
