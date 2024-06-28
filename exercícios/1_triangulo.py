'''
Autor: João Henrique
Data: 06/06/24
Versão: 1.0

Descrição: Faça um programa que recebe três valores e verifique se eles 
           podem representar os lados em um triangulo
           1- Triângulo escaleno: triângulo que possui todos os lados com medidas diferentes.

           2- Trinâgulo isóseles: triângulo que possui dois lados com medidas iguais.

           3- Triângulo equilátero: triângulo que possui todos os lados com medidas iguais 

'''
#===========================================
#variavel 
ladoA = 0
ladoB = 0
ladoC = 0
#entrada
ladoA = int(input('Digite a medida do lado A: '))
ladoB = int(input('Digite a medida do lado B: '))  
ladoC = int(input('Digite a medida do lado C: '))    
#Processamento

if((ladoA + ladoB) > ladoC and
     (ladoA + ladoC) > ladoB and
     (ladoB + ladoC) > ladoA and
       ladoA > 0 and ladoB > 0 and ladoC > 0):
      print('=============================') 
      print('Esse Triângulo existe!!')  
      print('=============================') 
      if (ladoA == ladoB and ladoB == ladoC):
            print('=============================') 
            print('triângulo Equilátero!!') 
            print('=============================')
      elif (ladoA == ladoB or ladoB == ladoC or ladoA == ladoC):
            print('=============================')
            print('triângulo Isósceles!!') 
            print('=============================')  
      elif (ladoA != ladoB and ladoB != ladoC and ladoC != ladoA):
            print('=============================') 
            print('triângulo Escaleno!!') 
            print('=============================')
else:
      print('=============================')
      print('Triângulo não existe')
      print('=============================')
      
#saida

#===========================================
