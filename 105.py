#!/usr/bin/python3

# Importacao do modulo sys
import sys

'''
    DESAFIO!!!
    1) Crie uma lista com os 1000 primeiros numeros pares. Não use loop!
    2) Crie uma lista com os numeros de 0 ate 99999999999999999999999999. Depois crie um loop para percorrer a lista ateh encontrar o primeiro multiplo de 5.
    OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
'''

###
# Exercicios
###

## Usando a lista: ['a','b','c']
# 1) Faca um loop dentro de uma funcao que irah retornar: ['A','B','C']
print('1) Faca um loop dentro de uma funcao que irah retornar: [A,B,C]')
lista = ['a', 'b', 'c']

def upperCase(lista = []):
    for i in range(len(lista)):
        #print(lista[i].upper(), end=" ")
	    lista[i] = lista[i].upper()
    return lista

lista = upperCase(lista)
print(lista)

## Usando a lista: [0, 1, 7, 4, 5]
# 2) Faca um loop dentro de uma funcao para retornar a soma de todos os elementos da listas. A funcao deve receber a lista como parametro.
print()
print('2) Faca um loop dentro de uma funcao para retornar a soma de todos os elementos da listas. A funcao deve receber a lista como parametro.')

num = [0, 1, 7, 4, 5]
def somaLista(lista = []):
    count = 0
    for i in range(len(lista)):
	    count += lista[i]
    return count

print(somaLista(num))

# 3) Crie uma funcao que receba uma lista e retorne outra lista composta pelos os numeros impares da lista recebida
print()
print('3) Crie uma funcao que receba uma lista e retorne outra lista composta pelos os numeros impares da lista recebida')

def impares(a = []):
	b = []
	for i in a:
		if i%2 != 0:
			b.append(i)
	return b

aa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(impares(aa))

## usando a string: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
# 4) Conte quantas palavras de tamanho >= 5 existe nessa string. Faca uma vez sem usar list comprehension e depois usando list comprehension.
print()
print('4) Conte quantas palavras de tamanho >= 5 existe nessa string. Faca uma vez sem usar list comprehension e depois usando list comprehension.')

lorem = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
lorem = lorem.replace(",", " ")
lorem = lorem.replace(".", " ")

count = 0 
for i in lorem.split():
	if len(i) >= 5:
		count += 1

print(f'Número de palavras >= 5 sem list comprehension: {count}')

lorem = lorem.replace(",", " ").replace(".", " ").split()
lorem2 = [i for i in lorem if len(i) >= 5]
print(f'Número de palavras >= 5 com list comprehension: {len(lorem2)}')


# 5) Usando list comprehension, crie uma lista com os multiplos de 3 de 0 ate 100


# 6) Faca uma funcao para encontrar os numeros primos no intervalo [2, 10), mas nao utilize a clausula else do for
