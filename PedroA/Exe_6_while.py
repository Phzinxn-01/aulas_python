'''
Autor: João Henrique
Data: 07/06/24
Versão: 1.0

Descrição: Estudo da estrutura de repetição "while"


'''
#====================================
indice = 1
while indice < 17:
    print(indice)
    indice = indice + 1
print('=========================')
#====================================
indice_2 = 10
while indice <= 6:
    print(indice_2, 'João' )
    indice_2 = indice_2 - 1
print('=========================')
#====================================
indice_3 = 1
while True:
    print(indice_3)
    indice_3 = indice_3 + 1
    if indice_3 == 5:
        break 
print('=========================')
#====================================
while True:
    opcao = input('Digite S para finalizar o programa: ')
    #indice_4 = indice_4 + 1
    if opcao == 'S':
        break
print('====================================')
