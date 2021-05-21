#!/usr/bin/python3

'''
    DESAFIO!!!
    1) Implemente um algoritmo para trocar o conteudo de duas variáveis x e y.
    2) Agora faca sem utilizar uma terceira variavel temporaria.
    OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
'''

###
# Exercicios
###

# 1) Crie uma funcao que receba duas listas e verifique se elas são iguais. Cada elemento e sua ordem devem ser o mesmo. Retorne True ou False.
print('1) Crie uma funcao que receba duas listas e verifique se elas são iguais. Cada elemento e sua ordem devem ser o mesmo. Retorne True ou False.')

def comparaListas(a=[], b=[]):
	if(a[:] == b[:]):
		return True
	else:
		return False
	
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
print(f'Retorno função comparaListas: {comparaListas(lista1, lista2)}')

l1 = ['Daniel', 'Wzoreck']
l2 = ['Daniel', 'Wzoreck']
print(f'Retorno função comparaListas: {comparaListas(l1, l2)}')

l3 = ['Daniel', 'Wzorek']
l4 = ['Daniel', 'Wzoreck']
print(f'Retorno função comparaListas: {comparaListas(l3, l4)}')

print(f'Retorno função comparaListas: {comparaListas(l1, lista1)}')

# 2) Crie uma funcao que verifica se duas strings são palindromes perfeitas. Faca as 'limpeza'/sanitizacao necessarias.  Retorne True ou False.
print('2) Crie uma funcao que verifica se duas strings são palindromes perfeitas. Faca as limpeza/sanitizacao necessarias.  Retorne True ou False.')

def palindromePerfeita(a = str()):
	if(a.lower().replace(" ", "") == a.lower().replace(" ", "")[::-1]):
		return True
	else:
		return False

a = 'LUz AzuL'
print(f'Retorno função palindromePerfeita: {palindromePerfeita(a)}')

a = 'na na'
print(f'Retorno função palindromePerfeita: {palindromePerfeita(a)}')

# OBS.: Utilize apenas o que foi estudado ate agora
