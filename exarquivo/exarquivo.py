arq1 = open("./nomes-idade.txt", "w")

arq1 = open("./nomes-idade.txt", "a+")

arq1.write("Roger idade: 23")
arq1.write("\nMaria idade: 32")

arq1.close()