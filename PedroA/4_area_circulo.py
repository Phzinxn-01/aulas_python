#=======================================================
#Autor: João Henrique
#Data: 28/05/24
#Versão: 1.0
#Descrição:Faça um algoritmo que receba o raio em metros 
#          de um circulo oapresente a sua área
#       --------------------------------------------
#       Exemplo de execução:
#       Insira o raio em metros:5
#       Área do circulo: 78.5M^2
#       --------------------------------------------
#
#       A = área
#       pi = 3.14
#       r = raio
#       A = pi*(r^2)
#       
#       --------------------------------------------

#=======================================================
#inicio
#variaveis
area = 0
pi = 3.14
r = 0
#Entrada
r = float(input('Insira o valor do Raio: '))#cast
#Processamneto
a = pi *(r**2)
#saida
print('A área do circulo é', a,'m^2')
#=======================================================