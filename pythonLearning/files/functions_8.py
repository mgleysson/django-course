'''
def <nome_funcao>(<arg1>, <arg2>, ..., <argN>):
    <corpo da funcao>
'''


# O nome do padrão segue o mesmo padrão snake_case de criação de variáveis

# Funcoes sem argumento
def print_hello():
    print('Hello')


print_hello()


# Funcoes com um argumento
def print_greetings(name):
    print('Hello %s!' % (name))


print_greetings(name='Marcos')


# Funções com n argumentos posicionais
def print_numbers(n1, n2):
    print('Num. 1: %.2f, Num. 2: %.3f' % (n1, n2))


print_numbers(n1=5.4, n2=5)


# Funcoes com argumento default
def print_greetings_2(name, upper_case=False):
    if upper_case:
        name = name.upper()
    print('Olá %s' % name)


print_greetings_2('Marcos', upper_case=True)

# Uso de funcoes para organizar código e evitar duplicações

# Sem funcao
lista1 = [1, 2, 3]
sum_list = sum(lista1)
size = len(lista1)
avg = sum_list / size
print('A média dos elementos é: ', avg)

lista2 = [4, 5, 6]
sum_list = sum(lista2)
size = len(lista2)
avg = sum_list / size
print('A média dos elementos é: ', avg)


# Com funcao
def calculate_avg(list_num):
    sum_list = sum(list_num)
    size = len(list_num)
    avg = sum_list / size
    print('A média dos elementos é: ', avg)


lista1 = [1, 2, 3]
calculate_avg(lista1)

lista2 = [4, 5, 6]
calculate_avg(lista2)

print('------------')


# Escopo de funções

# 1: Dentro da função, pode acessar variávels locais (analogia do vidro fumê)
def my_func():
    # escopo local
    print('Variável global:', x)


# escopo global
x = 20
my_func()
print('Valor fora da função:', x)

print('-----------')

# 2: Embora com o mesmo nome, váriaveis declaradas dentro de funções (locais) são diferentes das declaradas fora (globais).
def my_func():
    # 2: escopo local
    x = 10
    print('Valor dentro da função:', x)


# 1: escopo global
x = 20
my_func()
print('Valor fora da função:', x)

print('-----------')

# 3: Pode se referir a uma variável global e alterá-la diretamente com  a palavra-chave 'global'
def my_func():
    # 2: escopo local
    global x
    x = 10
    print('Valor dentro da função:', x)


# 1: escopo global
x = 20
my_func()
print('Valor fora da função:', x)
