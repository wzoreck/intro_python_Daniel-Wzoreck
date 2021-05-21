#!/usr/bin/python3

weekdays = ['mon','tues','wed','thurs','fri']

days = weekdays[0]         # elemento 0
days = weekdays[0:3]       # elementos 0, 1, 2
days = weekdays[:3]        # elementos 0, 1, 2
days = weekdays[-1]        # ultimo elemento

test = weekdays[3:]        # elementos 3, 4

days = weekdays[-2]        # ultimo elemento (elemento 4
days = weekdays[::]        # all elementos
days = weekdays[::2]       # cada segundo elemento (0, 2, 4)
days = weekdays[::-1]      # reverso (4, 3, 2, 1, 0)

all_days = weekdays + ['sat','sun']     # concatenar

# Usando append
days_list = ['mon','tues','wed','thurs','fri']
days_list.append('sat')
days_list.append('sun')

list = ['a', 1, 3.14159265359]

# list.reverse()

#########
# Exercicios - Listas
# Faca sem usar loops
#########

# Como selecionar 'wed' pelo indice?
print()
print('Como selecionar (wed) pelo indice?')
print('Solução:')
print(weekdays[2])

# Como verificar o tipo de 'mon'?
print()
print('Como verificar o tipo de (mon)?')
print('Solução:')
print(type(weekdays[0]))

# Como separar 'wed' até 'fri'?
print()
print('Como separar (wed) até (fri)?')
print('Solução 1:')
print(weekdays[2:])
print('Solução 2:')
print(all_days[2:5])

# Quais as maneiras de selecionar 'fri' por indice?
print()
print('Quais as maneiras de selecionar (fri) por indice?')
print('Solução 1:')
print(weekdays[-1])
print('Solução 2:')
print(weekdays[4])

# Qual eh o tamanho dos dias e days_list?
print()
print('Qual eh o tamanho dos dias e days_list?')
print('Solução:')
print(len(days_list))

# Como inverter a ordem dos dias?
print()
print('Como inverter a ordem dos dias?')
print('Solução:')
print(days_list[::-1])

# Como inserir a palavra 'zero' entre 'a' e 1 de list?
print()
print('Como inserir a palavra (zero) entre (a) e 1 de list?')
print('Solução:')
list.insert(1, 'zero')
print(list)

# Como atribuir o ultimo elemento de list na variavel ultimo_elemento e remove-lo de list?
print()
print('Como atribuir o ultimo elemento de list na variavel ultimo_elemento e remove-lo de list?')
print('Solução:')
ultimo_elemento = list[-1]
list.remove(ultimo_elemento)
print(list)
print(ultimo_elemento)

# Como limpar list?
print()
print('Como limpar list?')
print('Solução:')
list.clear()
print(list)

# Como deletar list?
print()
print('Como deletar list?')
print('Solução:')
del list
print(list)
