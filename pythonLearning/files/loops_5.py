# Estruturas de repetição:
# for e while

for i in [1, 2, 3, 4]:
    print(i)

print('-------')

for i in range(1, 5):
    print(i)

print('-------')

element = 1
while element < 5:
    print(element)
    element += 1

print('-------')

# Outros Comandos
element = 1
while element < 5:
    print(element)
    if element == 3:
        break
    element += 1

print('-------')

element = 1
while element < 5:
    element += 1
    if element == 3:
        continue
    print(element)
