#!/usr/bin/python3

###
# Exercicio
###

# 1) Imprima os metodos disponiveis para uma lista e para uma tupla
print('# 1)')
print()
print(dir(list))
print()
print(dir(tuple))

# 2) Faca um metodo para retornar apenas as diferencas entre as duas de metodos
# Não entendi o enunciado!

# 3) Adicione as coordenadas (latitude, longitude) para os dicts professor1, professor2 e professor3. Copie os dicts do arquivo 106.py. As coordenadas precisam ser inseparaveis e imutaveis.
print()
print('# 3)')

print()
professor1 = {'id': 42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Minas Gerais', 'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I', 'Programação para Internet II'], 'latitude':('234.4534.5464'), 'longitude':('5436.57568.46')}

professor2 = {'id': 37, 'name': 'Denilson Barbosa', 'age': 40, 'state_origin': 'Paraná', 'courses': ['Inteligência Artificial', 'Banco de Dados I', 'Banco de Dados II', 'Programação para Internet I'], 'laitude':('123421.43534.4'), 'longitude':('32423.235346.54')}

professor3 = dict(id=28, name='Jorge Armino', idade=37)
professor3['state_origin'] = 'Rio Grande do Sul'
professor3['courses'] = ['Filosofia', 'Informática e Sociedade']
professor3['latitude'] = ('234.4534.5464')
professor3['longitude'] = ('5436.57568.46')

print(professor1)
print(professor2)
print(professor3)