import os

alunos = []

while True:
    escolha = int(input("==SISTEMA SENAI==\nOpções:\n\n1-Adicionar alunos:\n2-Remover aluno\n3-Apresentar alunos\n4-Sair\n\nInsira a opção desejada: "))
    os.system('cls') or None
    if escolha == 1:
        nome = str(input("Digite o nome do aluno: "))
        alunos.append(nome)
        os.system('cls') or None
    elif escolha == 2:
        nome = str(input("Digite o nome do aluno que deseja remover: "))
        alunos.remove(nome)
        os.system('cls') or None

    elif escolha == 3:
        print("=======================")
        print(alunos)
        print("=======================")
        
    elif escolha == 4:
        break
    else:
        print("Escolha uma opção valida")