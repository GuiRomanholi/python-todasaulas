s = "Ola Mundo !!!"
print(" Texto: " + s)

s_minusculo = s.lower()  # "ola mundo !!!"
print("Texto Minusculo: " + s_minusculo)

s_maiusculo = s.upper()
print("Texto Maiusculo: " + s_maiusculo)

tamanho = len( s )  # int    13
print("Tamanho da string: ", tamanho)
print("Tamanho da string: " + str(tamanho))
#        01234567890123456789012345678901
texto = "A FIAP é uma faculdade bem legal"
tam = len(texto)
print("Tamanho: ", tam)
letra = texto[17]
print("Letra na posicao 17: " + letra)
letra = texto[20]
print("Letra na posicao 20: " + letra)

pos = texto.find( "legal" )
print("O texto possui a palavra", 
      "legal na posicao: ", pos)

pos = texto.find( "FIAP" )
print("O texto possui a palavra", 
      "FIAP na posicao: ", pos)

pos = texto.find( "manhã" )
print("O texto possui a palavra", 
      "manhã na posicao: ", pos)

pos = texto.find( "m" )
print("O texto possui a letra m ",
      "na posição: ", pos)

pos = texto.find( "m", 11 )
print("O texto possui outra letra m ",
      "na posição: ", pos)

pos = texto.find( "m", 26 )
print("O texto possui outra letra m ",
      "na posição: ", pos)


a = len("Ola mundo")
print(a)

f= "PROVA PROGII"
h = f.find("P" , 5)
print(h)

#a= 20 + 30 #50
#b="blbala" + str(30) 
#c=hex(898908) #DB75C
#d= len("ola mundo") #9
#e=int("153") + 160 resposta = 313
#f= "PROVA PROGII"
#f.find("P", 1) #6
