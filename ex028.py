from time import sleep


print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
num = (int(input('Em que número eu pensei?: ')))
from random import randint
s = randint(0, 5)
print('Processando...')
sleep(3)
if num == s:
    print('Você acertou')
else:
    print('Você errou, tente novamente')
print('eu pensei no número {}'.format(s))
