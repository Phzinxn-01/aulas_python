#=======================================================================
#autor: João Henrique
#data: 23/05/24
#versao: 1.0
#descrição: algoritmo que recebe o nome do usuario
#           e exive uma frase de saudação concatenada com
#           a entrada do usuario.
#=======================================================================
#observações:
#            a) para iniciar um comentario utiliza-se "#"
        #    b) no visual studio utilizar o comando ctrl+;
#               para comentar um bloco de código

#=======================================================================
#inicio

var_vazia = ''#var atribuida com um valor vazio
#entrada
nome = input("qual o seu nome?")
#processamneto
mensagem = 'olá, seja bem-vindo!'
frase = mensagem + nome
#saída
print(frase)


#fim
#=======================================================================