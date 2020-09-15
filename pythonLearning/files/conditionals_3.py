age = input('Qual a sua idade: ')
age = int(age)
print('Sua idade é %d' % (age))

# 0 <= idade < 18 - Criança
# 18 <= idade < 60 - Adulto
# 60 <= idade - Idoso

if 0 <= age < 18:
    print('Criança')
elif 18 <= age < 60:
    print('Adulto')
else:
    print('Idoso')