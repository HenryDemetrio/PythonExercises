import random
n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quarto aluno: '))

alunos = [n1, n2, n3, n4]
sorte = random.choice(alunos)
print('o aluno sorteado foi {}'.format(sorte))


