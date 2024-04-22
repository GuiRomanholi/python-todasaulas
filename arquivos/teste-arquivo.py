arq1 = open("./nome.txt", "r", encoding="utf-8")
texto = arq1.readline()
print(texto)

arq1.close()