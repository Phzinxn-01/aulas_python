#================================================================================
#Autor: João Henrique                                                            
#Data:24/05/24                                                                   
#Versão: 1.0                                                                     
#Descrição: faça um algoritmo que converta do real para o dolar 
#==============================================================================
#inicio
#variaveis
real = 0
cotacao = 0
dolar = 0
#entrada
print('==============================================')
real = float(input('digite o valor em reais (R$): '))
cotacao = float(input('digite o valor da cotação: '))
#Processamento
dolar = real/cotacao
#saida
print('R$',real,' equivalem', '$',dolar)
print('==============================================')
