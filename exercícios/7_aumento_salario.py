'''
Autor: João Henrique 
Data: 04/06/24
Versão: 1.0
Algoritmo: Multa velocidade
Descição: faça um programa que receba o salario de um funcionario, calcule e mostre o novo salario, sabendo-se que:
          Salario < R$ 1000,00 aumento de 25%
          Salario >= R$ 1000,00 e < R$ 2000,00 aumento de 15%
          Salario >= R$ 2000,00 aumento de 10%

'''
#================================================
#variaveis
salario = 0
salario_aumentado = 0
#entrada
salario = int(input('O seu salário é: '))

#saida

if salario < 1000.00:
    novo_salario = salario + ((salario * 25) / 100)
    aumento_salario = novo_salario - salario
    print("Aumento de 25% \n O funcionario pássara a receber {} \n O aumento foi de {}".format(novo_salario, aumento_salario))
elif salario >= 1000.00 and salario < 2000.00:
    novo_salario = salario + ((salario * 15) / 100)
    aumento_salario = novo_salario - salario
    print("Aumento de 15% \n O funcionario pássara a receber {} \n O aumento foi de {}".format(novo_salario, aumento_salario))
elif salario >= 2000.00:
    novo_salario = salario + ((salario * 10) / 100)
    aumento_salario = novo_salario - salario
    print("Aumento de 10% \n O funcionario pássara a receber {} \n O aumento foi de {}".format(novo_salario, aumento_salario))
  


