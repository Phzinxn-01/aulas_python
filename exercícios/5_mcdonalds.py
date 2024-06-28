'''
Descrição: Escreva um algoritmo para exibir o nome do lanche de acordo
           do número inserido pelo usuario, seguindo a tabela abaixo:

                    Nr.     Lanches
                    1       Big Mac
                    2       Quarteirão
                    3       McChicken
                    4       Cheddar McMelt
                    5       McFish

'''
lanche = 0

print('1 Big MAC')
print('2 Quarteirão')
print('3 McChicken')
print('4 Cheddar McMelt')
print('5 McFish')

lanche = int(input('escolha um lanche 1-5: '))

if lanche == 1:
    print('sua escolha é Big mac')
elif lanche == 2:
    print('sua escolha é Quarteirão')
elif lanche == 3:
    print('sua escolha é McChicken')
elif lanche == 4:
    print('sua escolha é Cheddar McMelt')    
elif lanche == 5:
    print('sua escolha é McFish')  
else:
    print('Opção inválida!!')    
