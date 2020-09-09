'''
Lista: Coleção sequencial indexada
    Coleção: Armazena diversos tipos de itens (Vários tipos de dados podem ser guardados)
    Sequencial: Ordem importa (Diferente de dicionários onde a ordem não importa tanto)
    Indexada: Os elementos podem ser acessados por índices (por isso a ordem importa)
'''

guests = ['Marcos', 'Felipe', 'Gabriel', 'Lucas', 'Alex']

# Acessando guests por índice
# Indices: 0, 1, 2, 3, 4
print(guests[0])
print(guests[3])
print(guests[len(guests) - 1])

# Facilidade: Indexação reversa ou índices negativos
# Indices: --5, -4, -3, -2, -1
print(guests[-1])

# Outra facilidade: Slice em Listas
# Não modifica a lista original, cria outra lista
print(guests[0:2])
print(guests[-3: -1])
print(guests[1:])
print(guests[:2])

# Reverter lista
print(guests[::-1])

# Lista com diferentes tipos de dados
objects = ['Notebook', 'Smartphone']
data = ['Marcos', 23, objects, 80.5]
print(data)
age = data[1]
print('Idade %d'% age)
data[1] = 24
print(data)

# Operador 'in' e 'not in' de pertencimento
print(objects in data)
print(23 in data)
print('Card' not in objects)



# Built-in functions para gerenciar listas
numbers = [1, 3, 5, 7, 9, 11]
print(numbers)
print(type(numbers))
print(len(numbers))
print(max(numbers))
print(min(numbers))

guests = ['Marcos', 'Felipe', 'Gabriel', 'Lucas', 'Alex']
guests.append('João')
print(guests)
guests.insert(1, 'Maria')
print(guests)

# Deletar elementos de uma lista
del guests[0]
print(guests)
print(guests.pop(0))
print(guests)
guests.remove('Gabriel')
print(guests)

# Retorna index de um elemento
print(guests.index('Alex'))

# Contagens de frequencia de elementos
print(guests.count('Felipe'))

# Ordenação de elementos
guests.sort()
#guests.sort(key=len)
print(guests)

# Reversão de lista
guests.reverse()
print(guests)

# Cópia de listas
guests_copy = guests.copy()

# Extensão de listas
other = ['Pedro', 'Ricardo']
guests.extend(other)
#guests.append(other)
print(guests)

# Filtro em lista
n = [1, 1, 3, 4, 5, 6, 1]

def is_equal(e):
    return e != 1

new_list = filter(is_equal, n)
print(f'{list(new_list)}')




