# print(" Problema do Triângulo: \n" +
#       " O programa deve ler três inteiros representando o tamanho dos lados de um triângulo; \n" 
#       " Qualquer dos lados deve ser menor que a soma dos outros dois; \n"
#       " São quatro as possíveis saídas produzidas pelo programa, com base nos valores de entrada: \n"
#       " 1. Equilátero - quando todos os lados do triângulo são iguais; \n"
#       " 2. Isósceles - quando dois lados do triângulo são iguais; \n"
#       " 3. Escaleno - quando nenhum dos lados do triângulo são iguais; \n"
#       " 4. Não é um triângulo - quando qualquer dos lados não for menor que a soma dos outros dois.")


class Triangulo():
    def __init__(self, num_1, num_2, num_3):
        self.num_1 = num_1
        self.num_2 = num_2
        self.num_3 = num_3

    def triangulo(self):
        soma_1_2 = self.num_1 + self.num_2 
        # print(soma_1_2)
        soma_1_3 = self.num_1 + self.num_3
        # print(soma_1_3)
        soma_2_3 = self.num_2 + self.num_3
        # print(soma_2_3)

        if(self.num_3 > soma_1_2 or self.num_2 > soma_1_3 or self.num_1 > soma_2_3):
            return f"4. Não é um triângulo - Qualquer dos lados não for menor que a soma dos outros dois. {self.num_1}; {self.num_2}; {self.num_3}"
        elif(self.num_1 == self.num_2 and self.num_1 == self.num_3):
            return f"1. Equilátero - todos os lados do triângulo são iguais:  {self.num_1}; {self.num_2}; {self.num_3}"
        elif (self.num_2 == self.num_1 or self.num_2 == self.num_3 or self.num_1 == self.num_3):
            return f"2. Isósceles - Dois lados do triângulo são iguais: {self.num_1}; {self.num_2}; {self.num_3}"
        elif (self.num_1 != self.num_2 and self.num_1 != self.num_3 and self.num_2 != self.num_3):
            return f"3. Escaleno - Nenhum dos lados do triângulo são iguais: {self.num_1}; {self.num_2}; {self.num_3}"

if __name__ == '__main__':
    num_1 = int(input("Digite o primeiro valor: "))
    num_2 = int(input("Digite o segundo valor: "))
    num_3 = int(input("Digite o terceiro valor: "))
    tri = Triangulo()
    result = tri.triangulo(num_1, num_2, num_3)
    print(result)