def trava(profundidade):
    print("Executando a função trava", profundidade)
    if profundidade > 1:
        trava(profundidade - 1)

trava(10)