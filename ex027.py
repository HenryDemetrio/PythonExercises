n = str(input('Digite seu nome completo: ')).strip()
s = n.split()

print('Muito prazer em te conhecer')
print('Seu primeiro nome é {}'.format(s[0]))
print('Seu ultimo nome é {}'.format(s[len(s)-1]))


