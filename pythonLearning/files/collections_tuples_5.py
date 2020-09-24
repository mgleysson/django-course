'''
    Uma tupla é uma coleção de objetos ordenados e imutáveis.
     Tuplas são sequências, assim como listas. A principal diferença entre as tuplas e as listas é que as tuplas não podem ser alteradas ao contrário das listas.
     As tuplas usam parênteses, enquanto as listas usam colchetes.
'''

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = 'a', 'b', 'c', 'd'

print(tup1)
print(tup2)
print(tup3)

# tupla vazia
tup1 = ()
print(tup1)

# tupla com elemento único: deve-se incluir uma vírgula
tup1 = (50,)
print(tup1)

# Como os índices de string, os índices de tupla começam em 0 e podem ser fatiados, concatenados e assim por diante.

# Acessando valores em tuplas
# Para acessar valores na tupla, use os colchetes para dividir junto com o índice
# ou índices para obter o valor disponível naquele índice. Por exemplo

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

# Atualizando tuplas
# As tuplas são imutáveis, o que significa que você não pode atualizar ou alterar os valores dos elementos da tupla.
# Você é capaz de pegar partes das tuplas existentes para criar novas tuplas como o exemplo a seguir demonstra
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Following action is not valid for tuples
# tup1[0] = 100

# So let's create a new tuple as follows
tup3 = tup1 + tup2
print(tup3)

# Excluir elementos de tupla
# A remoção de elementos individuais da tupla não é possível.
# É claro que não há nada de errado em juntar outra tupla com os elementos indesejáveis ​​descartados.

tup = ('physics', 'chemistry', 1997, 2000)

print(tup)
# del tup
print("After deleting tup : ")
print(tup)

# Operações básicas de tuplas

print(len((1, 2, 3)))  # tamanho
print((1, 2, 3) + (4, 5, 6))  # concatenação
print(('Olá!',) * 4)  # Repetição
print(3 in (1, 2, 3))  # Pertencimento
for x in (1, 2, 3): print(x, end=' ')  # Iteração
print('\n')
# Indexação, divisão e matrizes
# Uma vez que as tuplas são sequências, indexação e divisão funcionam da mesma forma para tuplas e strings,
# assumindo a seguinte entrada
T = ('C++', 'Java', 'Python')
print(T[2])
print(T[-2])
print(T[1:])

# Funções de tupla integradas
tup1 = (1, 2, 3)
tup2 = (3, 4, 5)
list1 = [2, 3, 4]

print(max(tup1))
print(min(tup1))
print(tuple(list1))


