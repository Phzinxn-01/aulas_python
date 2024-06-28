'''Autor: João Henrique
Data: 13/06/24
Versão: 1.0
Algoritmo: "tabuada 1 ao 9"
Descrição: faça um programa que apresente a tabuada 1 ao 10;
'''

#==========================================
print('-------------------------------------')
for l in range(11): #0 ->1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
    for c in range(11): # 0 -> 10
        print(f'{l} X {c} = {l * c} ')
    print('-------------------------------')

#==========================================