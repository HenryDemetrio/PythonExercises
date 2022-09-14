v = int(input('Digite a velocidade atual do carro: '))
m = 80
multa = (v-80) * 7
if v > m:
    print('MULTADO! Você excedeu o limite permitido de 80km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um Bom Dia! Dirija com segurança!')


