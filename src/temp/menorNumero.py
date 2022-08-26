# print("Problema do Menor número: \n" +
#       " O programa deve ler 3 números inteiros e exibir o menor deles.")

def menorNumero(num_1, num_2, num_3):
    if(num_1 < num_2 and num_1 < num_3):
        return f"O menor numero digitado foi: {num_1}"
    elif (num_2 < num_1 and num_2 < num_3):
        return f"O menor numero digitado foi: {num_2}"
    elif (num_3 < num_1 and num_3 < num_2):
        return f"O menor numero digitado foi: {num_3}"
    else:
        return f"Todos os numeros sao iguais:  {num_1}; {num_2}; {num_3}"

if __name__ == '__main__':
    num_1 = int(input("Digite o primeiro valor: "))
    num_2 = int(input("Digite o segundo valor: "))
    num_3 = int(input("Digite o terceiro valor: "))
    print(menorNumero(num_1, num_2, num_3))
