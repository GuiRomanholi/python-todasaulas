
print("Quantas linhas?")
linha = int(input())

print("Quantas colunas?")
coluna = int(input())

for l in range(0, linha):
    for c in range(0, coluna):
        print(c + 1, end="")
    print("")
