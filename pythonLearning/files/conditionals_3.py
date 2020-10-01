age = input('Qual a sua idade: ')
age = int(age)
print('Sua idade é %d' % age)

# 0 <= idade < 18 - Criança
# 18 <= idade < 60 - Adulto
# 60 <= idade - Idoso

if 0 <= age < 18:
    print('Criança')
elif 18 <= age < 60:
    print('Adulto')
else:
    print('Idoso')

print('------------------')

weight = input('Qual o seu peso: ')
weight = float(weight)

height = input('Qual a sua altura: ')
height = float(height)

imc = weight/(height**2)
print('Seu imc é %.2f' % imc)
print('Seu imc é', round(imc, 2))

category = 'Não-Magreza'
if imc < 18.5:
    category = 'Magreza'

print('Classificação: %s' % category)
