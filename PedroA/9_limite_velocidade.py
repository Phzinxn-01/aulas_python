'''
Autor: João Henrique
Data:06/06/24
Versão: 1.0

Descrição: Escreva um programa que leia a velocidade maxima permitida em 
           uma avenida e velocidade com que o motorista estava dirigindo
           nela e calcule a multa que uma pessoa vai receber:

           velocidade ultrapassada              valor da multa
           Até 10km\h                           R$50,00
           11 a 30km\h                           R$100,00
           Mais 31km\h                           R$200,00

'''
#============================================================
#variaveis
velocidade = 0
velocidade_max = 0

#entrada
velocidade_max = float(input('Digite a velocidade maxima da Via: '))
velocidade = float(input('Digite a velocidade do seu veículo: '))

#Processamento
diferenca = velocidade - velocidade_max

#saida
if diferenca <= 10:
    print('Você ultrapassou a velocidade maxima permitida em:', diferenca,'km', '\nSua multa é de R$50,00') 
elif diferenca >= 11 and diferenca <= 30:
     print('Você ultrapassou a velocidade maxima permitida em:', diferenca,'km', '\nSua multa é de R$100,00')
else:
      print('Você ultrapassou a velocidade maxima permitida em:', diferenca,'km', '\nSua multa é de R$200,00')  

#============================================================