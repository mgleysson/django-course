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

# Outros Comandos: Break
'''
O uso mais comum para break é quando alguma condição externa é acionada exigindo uma saída rápida de um loop.
A instrução break pode ser usada em loops while e for.

Se você estiver usando loops aninhados, a instrução break interrompe a execução do loop mais interno
e começa a executar a próxima linha de código após o bloco.
'''

print('---- Início do Loop')
for letter in 'python':
    if letter == 'h':
        break
    print('Letra corrente :', letter)
print('---- Fim do Loop')

print('-------')

element = 1
while element < 5:
    print(element)
    if element == 3:
        break
    element += 1

print('-------')

# Outros comandos: Continue
'''
Ele retorna o controle para o início do loop while. 
A instrução continue rejeita todas as instruções restantes na iteração atual do loop e move o controle de volta para o topo do loop.

A instrução continue pode ser usada em loops while e for .
'''

element = 0
while element < 5:
    element += 1
    if element == 3:
        continue
    print(element)
