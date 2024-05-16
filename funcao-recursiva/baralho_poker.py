from random import sample

baralho_poker = list(range(1, 14))
print("Monte: ",baralho_poker)
print("Mão: ", sample(baralho_poker,5))