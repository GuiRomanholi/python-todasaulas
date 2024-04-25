lista = [
    {"nome": "joao silva", "tel": "11111", "email": "joaogamer@gmail.com"},
    {"nome": "maria silva", "tel": "222222", "email": "mariagamer@gmail.com"},
    {"nome": "rodrigo silva", "tel": "33333", "email": "rodrigogamer@gmail.com"}
]

arq1 = open("./contatos.csv", "w", encoding="utf-8")

for contato in lista:
    arq1.write(contato["nome"] + ", " + contato["tel"] + ", " + contato["email"])
    arq1.write("\n")

arq1.close()