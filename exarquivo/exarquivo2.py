arq1 = open("./nomes-idade.csv", "w", encoding="utf-8")

arq1.write("João; 28; 111-11111\n")
arq1.write("Maria; 19; 222-2222\n")
arq1.write("José; 52; 333-3333")

arq1 = open("./nomes-idade.csv", "r")
ler = arq1.readlines()
print(ler)


arq1.close()