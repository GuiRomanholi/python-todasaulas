from random import shuffle

class Carta():
    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor
    
    def __str__(self):
        return self.naipe + "_" + str(self.valor)
    def __repr__(self):
        return self.__str__()



class Jogo():
    def __init__(self):
        self.monte = []
        self.naipes = ["ouros", "espadas", "copas", "paus"]
        for naipe in self.naipes:
            for i in range(1, 14):
                carta = Carta(naipe, i)
                self.monte.append(carta)
    

    def embaralhar(self):
        shuffle(self.monte)
    
    def dar_cartas(self, quantidade):
        mao = []
        for i in range(quantidade):
            mao.append(self.monte.pop(i))
        return mao


jogo = Jogo()
jogo.embaralhar()
print("Monte tem: ", len(jogo.monte))


jogador1 = jogo.dar_cartas(5)
print("Monte tem: ", len(jogo.monte))

jogador2 = jogo.dar_cartas(5)
print("Monte tem: ", len(jogo.monte))


print("Cartas jogador 1: ", jogador1)
print("Cartas jogador 2: ", jogador2)

        
