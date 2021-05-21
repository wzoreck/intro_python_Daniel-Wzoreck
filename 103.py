#!/usr/bin/python3

'''
    DESAFIO!!!
    Implemente um algoritmo para inverter a ordem de uma string em sua
    linguagem de programacao favorita. Nao use funcoes/metodos prontos.
'''

###
# Exercicios
###

# 1) Extraia o titulo do livro da string
# 2) Salve o titulo de cada livro em uma variável
# 3) Quantos caracteres cada título tem?
# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}


book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'

print()
print('# 1)')
print(book1[:book1.find('by')-1])
print(book2[:book2.find('by')-1])
print(book3[:book3.find('by')+13])

print()
print('# 2)')
t1 = book1[:book1.find('by')-1]
t2 = book2[:book2.find('by')-1]
t3 = book3[:book3.find('by')+13]

print(f'{t1}')
print(t2)
print(t3)

print()
print('# 3)')
print(f'{len(t1)}')
print(len(t2))
print(len(t3))

print()
print('# 4)')
autor = book1[book1.find('by')+3 : book1.find(',')]
print(t1+' - '+autor+', '+book1[-4:])

autor = book2[book2.find('by')+3 : book2.find(',')]
print(t2+' - '+autor+', '+book2[-4:])

autor = book3[book3.find('by')+17 : book3.find(',')]
print(t3+' - '+autor+', '+book3[-4:])

# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta

palindrome_one = 'ovo'
palindrome_two = 'Natan'
palindrome_three = 'luz azul'
palindrome_four = 'caneta azul'

print()
print('# 5)')
if(palindrome_one == palindrome_one[::-1]):
	print(f'{palindrome_one} é palindrome perfeita')
else:
	print(f'{palindrome_one} não é palindrome perfeita')

palindrome_two = palindrome_two.lower()
if(palindrome_two == palindrome_two[::-1]):
	print(f'{palindrome_two} é palindrome perfeita')
else:
	print(f'{palindrome_two} não é palindrome perfeita')

palindrome_three = palindrome_three.lower()
if(palindrome_three.replace(" ", "") == palindrome_three.replace(" ", "")[::-1]):
	print(f'{palindrome_three} é uma palindrome perfeita')
else:
	print(f'{palindrome_three} não é uma palindrome perfeita')

if(palindrome_four.replace(" ", "") == palindrome_four.replace(" ", "")[::-1]):
	print(f'{palindrome_four} é uma palindrome perfeita')
else:
	print(f'{palindrome_four} não é uma palindrome perfeita')