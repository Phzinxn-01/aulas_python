'''
nome: João Henrique
Data: 11/06/24
Versão: 1.0
Algoritmo: senha
Descição: Faça um programa que receba duas notas de seis alunos.
          Calcule e mostre:
          A media aritmetica das duas notas de cada aluno; e
          A mensagem que esta na tabela a seguir:
            Media aritmetica            mensagem
            ate 3                       Reprovado
            entre 4 e 7                 Exame
            de 8 pra cima aprovado      Aprovado


            O total de alunos aprovados;
            O total de alunos de exame;
            O total de alunos reprovados;
            A media da classe.

'''
#==================================================
#variaveis
somaMedia = 0
Qntdalunos = 6
alunosAprovados = 0
alunosExames = 0
AlunosReprovados = 0
aluno = 0
reprovado = 'reprovado'
exame = 'exame'
aprovado = 'aprovado'



while aluno < Qntdalunos:
    aluno += 1
    nota1 = float(input(f'Digite a 1° nota do aluno {aluno}: '))
    nota2 = float(input(f'Digite a 2° nota do aluno {aluno}: '))

    media = (nota1 + nota2) / 2
    somaMedia = somaMedia + media 
    

    if media > 7 and media <= 10:  
        print(f'Aluno {aluno}:', aprovado,'\nMédia:',media)
        alunosAprovados += 1
        

    elif media > 3:
        print(f'Aluno {aluno}: precisará fazer:',exame,'\nMédia:',media)
        alunosExames += 1
        
    else:
        print(f'Aluno {aluno}: está:',reprovado,'\nMédia:',media)
        AlunosReprovados += 1




mediaFinal = round(somaMedia / Qntdalunos)    
print(f'Média de classe : {mediaFinal} ')  
print(f'Quantidade de alunos Aprovados : {alunosAprovados} ') 
print(f'Quantidade de alunos de Exames : {alunosExames} ') 
print(f'Quantidade de alunos reprovados : {AlunosReprovados} ')      






#==================================================
