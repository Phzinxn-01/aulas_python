#================================================================================#
#Autor: João Henrique                                                            #
#Data:24/05/24                                                                   #
#Versão: 1.0                                                                     #
#Descrição:  Faça um algoritmo que receba 5 notas e imprima                      #
#            a média final do aluno                                              #
#          ------------------------------                                        #
#             Exemplo de execução                                                #
#             nota 1: 10                                                         #
#             nota 2: 10                                                         #
#             nota 3: 10                                                         #
#             nota 4: 10                                                         #
#             nota 5: 10                                                         #
#             Média final: 10                                                    #
#================================================================================#
#Início                                                                          #
#                                                                                #
#Entrada:O usuario seleciona suas 5 notas.                                       #
n1 = int(input('Digite a nota 1:'))                                              #
n2 = int(input('Digite a nota 2:'))                                              #
n3 = int(input('Digite a nota 3:'))                                              #
n4 = int(input('Digite a nota 4:'))                                              #
n5 = int(input('Digite a nota 5:'))                                              #
#Processamento:Para achar a media final, some as 5 notas, e divida pela          #
#              quantidade de notas digitadas                                     #
media = (n1 + n2 + n3 + n4 + n5)/ 5                                              #
#Saída: Média final                                                              #
print('A media final do aluno é', ' = ', media)                                  #
#fim                                                                             #
#================================================================================#