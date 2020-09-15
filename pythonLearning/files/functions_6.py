'''
def <nome_funcao>(<arg1>, <arg2>, ..., <argN>):
    <corpo da funcao>
'''


# O nome do padrão segue o mesmo padrão snake_case de criação de variáveis

# Funcoes sem argumento
def print_hello():
    print('Hello')


ret = print_hello()
print(ret)


# Funcoes com um argumento
def print_greetings(name):
    print('Hello %s!' % (name))


print_greetings(name='Marcos')


# Funções com n argumentos posicionais
def print_numbers(n1, n2):
    print('Num. 1: %f, Num. 2: %f' % (n1, n2))


print_numbers(n1=5.4, n2=5)


# Funcoes com argumento default
def print_greetings_2(name, upper_case=False):
    if upper_case:
        name = name.upper()
    print('Olá %s' % name)


print_greetings_2('Marcos', upper_case=True)

# Escopo de funções
var_1 = 5


def local_scope():
    var_2 = 6
    print('Var 2 Local', var_2)
    # print(var_1)
    global var_1
    var_1 = 50
    print('Var 1 Local', var_1)


print('Var 1 Global', var_1)
local_scope()
print('Var 1 Global', var_1)