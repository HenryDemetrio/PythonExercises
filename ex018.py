from math import sin, cos, tan, radians
print('Exercicio 18\nHenry Demétrio')


a = float(input('Digite um ângulo que você deseja: '))

s = sin(radians(a))
c = cos(radians(a))
tg = tan(radians(a))


print('o angulo de {} tem o Seno de {:.2f}'.format(a, s))
print('o angulo de {} tem o Cosseno de {:.2f}'.format(a, c))
print('o angulo de {} tem a Tangente de {:.2f}'.format(a, tg))

