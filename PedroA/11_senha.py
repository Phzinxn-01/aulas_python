'''
Autor: João Henrique 
Data: 04/06/24
Versão: 1.0
Algoritmo: senha
Descição: Faça um programa que solicite para o usuário a senha de acesso
          ao sistema, ele tera no maximo três tentativas para inserir a senha 
          cadastrada (senai115), caso passe desse limite uma mensagem de erro deve
          aparecer. 

'''
#====================================
login = ''
loginPadrao = 'JOAO'
senha = ''
senhaPadrao = 'senai115'
tentativas = 3


while True:
    print('===============================================')
    print(              '                Sistema de Login')
    login = input('Digite o Login correto para liberar a senha: ')
    if login == loginPadrao :
       print('Login correto!')
       break
    else:
        tentativas = tentativas - 1
        print('Você só pussui mais', tentativas,'tentativas')
        
    if tentativas <= 0:
        print('Tentativas Esgotadas')
        break

    
        
        
while True:
    senha = input('Digite a senha de acesso: ')
    if senha == senhaPadrao:
        print('Acesso liberado!')
        break
    else:
        tentativas = tentativas - 1
        print('Você só pussui mais', tentativas, 'tentativas')
        print('===============================================')
#====================================