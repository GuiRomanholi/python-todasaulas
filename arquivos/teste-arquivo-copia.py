arq1 = open("./nome.txt", "r", encoding="utf-8")

arq2 = open("./nome-copia.txt", "w", encoding="utf-8")

texto = " "
while texto != "":
    texto = arq1.readline()
    arq2.write(texto)

# arq2.write(arq1.readline())
# arq2.write(arq1.readline())
# arq2.write(arq1.readline())

arq1.close
arq2.close
