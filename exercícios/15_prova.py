'''
Descrição: Faça um programa que receba dois valores, sendo que o
           primeiro deve ser menor que o segundo.
           O programa deve apresentar todos os números impares
           contido nesta sequência>
           (modulo %. Exemplo: 7%2 = 1)
'''
#================================================
print('O primeiro número terá que ser maior que o segundo!!')
num1 = int(input('Digite o 1° valor: '))
num2 = int(input('Digite o 2° valor: '))

for number in range(num1 , num2 + 1):
    if number % 2 == 1:
        print(f'{num1} % {num2} = {number}')


#================================================







