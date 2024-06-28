#======================================================
#Autor: João Hnrique
#Data: 28/05/24
#Versão: 1.0
#Descrição: faça um algoritmo que receba a temperatura em 
#           ºC e converta para ºF e K
#       -----------------------------------------
#       Exemplo de execução:
#       Insira a temperatura em Celcius: 0
#       Fahrenheit: 32ºF
#       Kelvin: 273,15 K
#       ----------------------------------
#
#======================================================
#variaveis
celcius = 0
fahreinheint = 0
kelvin = 0
#entrada
celcius = float(input('Insira uma temperaura em Graus Celcius: '))
#Processamento
fahreinheint = (celcius * (9/5)) + 32
kelvin = celcius + 273,15
#saida
print(celcius,'ºC equivalem', fahreinheint,'ºF')
print(celcius,'ºC equivalem', kelvin, 'K')






















