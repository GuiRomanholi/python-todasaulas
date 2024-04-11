print("Bom dia, hoje descobriremos cê voce está ou não com sobrepeso, para isso por favor informe as seguintes questões.")
print("Qual a sua altura?")
altura = float(input())
print("Qual o seu peso?")
peso = float(input())
imc = peso/(altura**2)
if imc>= 25:
    print("Vocé está com soprepeso, por favor tente se cuidar")
else:
    print("Você não está com sobrepeso, continue ce cuidando.")


