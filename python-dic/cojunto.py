# c1 = {5, 5, 4, 3, 2, 1}
# print(c1)

li = [1, 2, 2, 3, 3, 4, 5, 5]
# print(li)

c2 = set(li)
print(c2)

for i in range(2):
    n = int(input("Qual o numero vc quer procurar?"))
    if n in c2:
        print("Tem o numero", n)
    else:
        print("Não tem o numero", n)