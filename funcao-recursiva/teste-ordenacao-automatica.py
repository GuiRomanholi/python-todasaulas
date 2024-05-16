from random import sample, randrange
#         0 1 2 3 4 5
#cartas = [6,4,3,1,5,2]
cartas = sample(range(0,1000), 10)
print(cartas)
# ajuda = 6
for j in range(len(cartas)):
    for i in range(0,len(cartas) - 1):
        if cartas[i] > cartas[i + 1]:
            #Trocar o valor de cartas[0] por cartas[1]
            ajuda = cartas[i]
            cartas[i] = cartas[i + 1]
            cartas[i + 1] = ajuda
    print(cartas)
