texto = """
        public class TesteJava1 {
            public static void mais(String[] args) {
                System.out.println("Teste 1 feito em Java")
            }
        }
"""

arquivo1 = open("./TetsteJava1.java", "w") # Aqui vc ta criando um arquivo
arquivo1.write(texto)                      # Colocando o texto dentro dele
arquivo1.close()                           # E aqui está fechando

"""-----------------------------------------------------------------------------------------"""

arquivo2 = open("./nomes.txt", "w", encoding="utf-8")
# Não esqueça das aspas com "./" e o "w" <-- para abri-lo, utf-8 é para aparecer acentos
arquivo2.write("Guilherme\n")
arquivo2.write("João\n")
arquivo2.write("José\n")
arquivo2.close()

