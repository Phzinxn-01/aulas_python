'''
Autor: João Henrique 
Data: 04/06/24
Versão: 1.0

Descição: Escreva um programa que leia a idade de um individuo e
          escreva a faixa etaria a que pertence, de acordo com a tabela abaixo.

          faixa etaria              classificação
          <12                       criança
          13~17                     Adolescente
          18~59                     Adulto

'''
#================================================
#variaveis
idade = 0
#entrada
idade = int(input('Digite sua idade: '))
#processamento
if idade < 12:
    print('criança')
elif idade >= 13 and idade <= 17:
    print('Adolescente')
elif idade >= 18 and idade <= 59:
    print('Adolescente')
else:
    print('Idade Inválida')



#================================================