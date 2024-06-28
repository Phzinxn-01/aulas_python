'''
Autor: João Henrique
Data: 13/06/24
Versão: 1.0
Algoritmo: "tabuada"
Descrição: faça um programa que calcule a tabuada de um número digitado pelo usuario;
'''
#=======================================
#variaveis
numDigitado = 0

num = 0
#entrada
numDigitado = int(input('Digite um número: '))
#processamento
for num in range(11):
    result = numDigitado * num
    print(f'{numDigitado} X {num} = {result}')

#=======================================