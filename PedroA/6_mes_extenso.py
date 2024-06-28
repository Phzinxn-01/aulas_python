'''
Autor: João Henrique
Data: 04/06/24
Versão: 1.0


Descrição:Escreva um algoritmo para exibir o nome do mês por extenso
                de acordo com o número que o representa:
                        1	    Janeiro
                        2	    Fevereiro
                        3	    Março
                        4	    Abril
                        5	    Maio
                        6	    Junho
                        7	    Julho
                        8	    Agosto
                        9	    Setembro
                        10	    Outubro
                        11	    Novembro
                        12	    Dezembro
'''
#================================================================
#variaveis
mes = 0

#entrada
print('***********************************************')
print('Nr. Mês \n 1. janeiro \n 2. Fevereiro \n 3. Março \n 4. Abril \n 5. Maio \n 6. Junho \n 7. Julho \n 8. Agosto \n 9. Setembro \n 10. Outubro \n 11. novembro \n 12. Dezembro')
mes = int(input('Insira o número do mês desejada: '))

#processamento

if mes == 1:
    print('O mês escolhido é Janeiro')
elif mes == 2:
    print('O mês escolhido é Fevereiro')
elif mes == 3:
    print('O mês escolhido é Março')
elif mes == 4:
    print('O mês escolhido é abril')
elif mes == 5:
    print('O mês escolhido é Maio')
elif mes == 6:
    print('O mês escolhido é Junho')
elif mes == 7:
    print('O mês escolhido é Julho')
elif mes == 8:
    print('O mês escolhido é Agosto')
elif mes == 9:
    print('O mês escolhido é Setembro')
elif mes == 10:
    print('O mês escolhido é Outubro')
elif mes == 11:
    print('O mês escolhido é Novembro')
elif mes == 12:
    print('O mês escolhido é Dezembro')
else:
    print('Opção inválida')


#saida
print('***********************************************')

#================================================================