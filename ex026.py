f = str(input('Digite uma frase: ')).strip().upper()
n = f.count('A')
p = f.find('A')+1
u = f.rfind('A')+1
print('A letra a aparece {} vezes na frase.'.format(n))
print('A primeira letra A apareceu na posição {}.'.format(p))
print('A ultima letra A apareceu na posição {}.'.format(u))


