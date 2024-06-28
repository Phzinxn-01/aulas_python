'''Autor: João Henrique
Data: 14/06/24
Versão: 1.0
Descrição: faça um programa que voce selecione o numero da chamada do aluno, 
           e apresente o nome do aluno
'''

lista_chamada = ['Luana',
                'Gustavo',
                'Danielle',
                'Felipe',     
                'João mudou de lugar',
                'Thago',
                'Aldivan',
                'José',
                'Arthur',
                'Pedrão', 
                'Mauricio',
                'Davi',
                'Kawan',
                'Andrey',
                'Lucas',
                'Diego matrix',
                'João timao',
                'Ana',
                'Vinicius vascaino',
                'Adriel',
                'Patrick',
                'Brunão',
                'Professor girafalles mini'                 
                 ]
while True:
    print('Escolha um número entre 0 e 23!')
    num_chamada = int(input('Escolha um número da chamada: '))
    print(lista_chamada[num_chamada])

    continuar = input('Digite N para sair e S para continuar: ')
    if continuar == 'N':
        break