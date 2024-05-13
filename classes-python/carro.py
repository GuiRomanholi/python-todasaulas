class Pneu():
    def __init__(self):
        self.marca = "Generico"
        self.aro = 14
        self.vida_util = 1000
    
    def usar(self):
        if self.vida_util > 100:
            self.vida_util = self.vida_util - 1
        else:
            print("Pneu deve ser trocado")


class Carro():

    def __init__(self, marca_parametro = "Generica",
                  modelo_parametro = "X"):
        self.ligado = False
        # self.marca = "Generica"
        # self.modelo = "X"
        self.marca = marca_parametro
        self.modelo = modelo_parametro

        self.velocidade = 0
        self.pneu = Pneu()
        print("Construtor Carro executado")


    def ligar(self):
        self.ligado = True
    

    def desligar(self):
        self.ligado = False

    def situacao(self):
        # if self.ligado:
        #     texto = "Ligado"
        # else:
        #     texto = "Desligado"
        texto = "Ligado" if self.ligado else "Desligado"
        print(f"O carro esta {self.modelo} da {self.marca} está {texto}")
    
    def acelerar(self):
        if self.ligado:
            self.velocidade = self.velocidade + 5
            self.pneu.usar()
            print(f"Acelerando para {self.velocidade} km/h")
        else:
            print("O carro precisa estar ligado para acelerar")




def main():
    c1 = Carro("Fiat", "Mobly")
    c2 = Carro("Citroen", "C3")
    c3 = Carro()

    c1.ligado = True
    # c1.marca = "Fiat"
    # c1.modelo = "Mobly"

    c2.ligado = False
    # c2.marca = "Citroen"
    # c2.modelo = "C3"

    print("Informe o modelo do carro")
    c3.marca = input()
    c3.ligado = False
    
    

    c1.pneu.marca = "Pirelli"
    c1.pneu.vida_util = 105
    c1.ligar()
    c1.acelerar()
    c1.acelerar()
    c1.acelerar()
    c1.acelerar()
    c1.acelerar()
    c1.acelerar()

    c2.ligar()
    c2.acelerar()
    c2.acelerar()
    c2.acelerar()

    c1.situacao()
    c2.situacao()
    c3.situacao()

# print("Modulo Carro: ", __name__)

if __name__ == "__main__":
    main()

