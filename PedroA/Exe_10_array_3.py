'''
autor: João henrique
Data: 25/06/24
Descrição: Estudo do tipo de dado Array(Vetor)

'''
alunos_sala = ['luana','Gustavo', 'Danielle']

alunos_sala.append('Felipe')
print(alunos_sala)

print(alunos_sala[2])

for indice in range(4):
    print(alunos_sala[indice])

for aluno in alunos_sala:
    print(aluno)

cabecalho = ['nome','idade','Matricula']
dado_um = ['Pele','Eterno','10']

print(dado_um[0])

tabela = [cabecalho, dado_um]
print(tabela[1][0])

#[
#   ['Nome','Idade','Matricula']
#    ['Pele','Eterno','   10   ']
#]

print(tabela[0][1])
print(tabela[1][2])
