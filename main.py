#Exercícios: Funções

#1Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

arg1 = 1
arg2 = 2
arg3 = 3

def soma (arg1, arg2, arg3):
    calculo = arg1 + arg2 + arg3
    print (f'O resultado da soma é: {calculo}')
soma (arg1, arg2, arg3) 

#2. Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

n= 51
def reverso (n):
    inverter = str(n) #converter o numero em string antes de fazer o inverso
    rev = inverter [::-1]
    print (f'O número invertido é: {rev}')
reverso(n)

#3. Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para cada opção, crie uma função. Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversão correta.
#F = 1.8 × C + 32 e C é a temperatura em Celsius e F é a temperatura correspondente em Fahrenheit.

print("Bem vindo ao convertor de temperatura!")
temp = int (input('Digite a temperatura desejada e em seguida escolha para que tipo deseja :'))

def C_para_F(temp):
    F = (temp*9/5) + 32
    return F

def F_para_C(temp):
    C= (temp -32)*5/9
    return C

def menu():
    while True:
        op = int(input('Escolha 1 se quer Celsius para Farenheit: \n' +
                       'Escolha 2 se quer Farenheit para Celsius: \n'))

        if op== 1:
            print('Convertido: ', C_para_F(temp),' graus Farenheit\n')
        elif op== 2:
              print('Convertido: ', F_para_C(temp),' graus Celsius\n')
        else:
            print('Opção inválida')
menu()
