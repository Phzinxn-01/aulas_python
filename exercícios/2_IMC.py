'''
Autor: João Henrique
Data: 07/06/24
Versão: 1.0

Descrição: Faça um algoritmo que receba a altura e o peso da pessoa e calcule o IMC.


'''
#==============================================
#variaveis
peso = 0
altura = 0
#entrada
peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura: '))
#processamento
imc = peso /(altura * altura)

if imc >= 16 and imc < 17:
    print('======================')
    print('Muito abaixo do peso!!')
    print('======================')
elif imc >= 17 and imc < 18.5:
    print('======================')
    print('Abaixo do peso!!')
    print('======================')
elif imc >= 18.5 and imc < 25:
    print('======================')
    print('Peso normal!!')
    print('======================')
elif imc >= 25 and imc < 30:
    print('======================')
    print('Acima do peso!!')
    print('======================')
elif imc >= 30 and imc < 35:
    print('======================')
    print('Obesidade grau I!!')
    print('======================')
elif imc >= 35 and imc <= 40:
    print('======================')
    print('Obesidade grau II!!')
    print('======================')
else:
    print('======================')
    print('Obesidade grau III!!')
    print('======================')
#saida
print('Seu imc é:', imc)
#==============================================