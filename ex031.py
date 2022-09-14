dis = int(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(dis))

precin = dis * 0.50
precao = dis * 0.45

if dis <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(precin))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(precao))
