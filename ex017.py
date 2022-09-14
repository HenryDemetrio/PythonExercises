print('Exercicio 17\nHenry Demétrio')

from math import sqrt
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
h = ca ** 2 + co ** 2
print('A hipotenusa vai medir {:.2f}'.format(sqrt(h)))

