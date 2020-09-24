'''
Cada chave é separada de seu valor por dois pontos (:),
 os itens são separados por vírgulas e tudo está entre colchetes.
 Um dicionário vazio sem nenhum item é escrito com apenas duas chaves, como este: {}.

As chaves são exclusivas em um dicionário, enquanto os valores podem não ser.
 Os valores de um dicionário podem ser de qualquer tipo,
  mas as chaves devem ser de um tipo de dados imutável, como strings, números ou tuplas.
'''

data = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print("dict['Name']: ", data['Name'])
print("dict['Age']: ", data['Age'])

# Se tentarmos acessar um item de dados com uma chave, que não faz parte do dicionário, obteremos um erro da seguinte
# forma
# data = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# print ("dict['Alice']: ", data['Alice'])

data = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
data['Age'] = 8 # update existing entry
data['School'] = "DPS School" # Add new entry

print("dict['Age']: ", data['Age'])
print("dict['School']: ", data['School'])
print("dict: ", data)

data = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del data['Name'] # remove entry with key 'Name'
# data.clear()     # remove all entries in dict
# del data         # delete entire dictionary

print("dict['Age']: ", data['Age'])
# print("dict['School']: ", data['School'])

data = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print(data.get('Name', 'Default'))
print(data.get('Name2', 'Default'))
print(data.items())
print(data.keys())
print(data.values())
