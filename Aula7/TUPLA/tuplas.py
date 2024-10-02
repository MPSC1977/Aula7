import os

os.system('cls')

tuplas_vazias = ()

# Tupla de um elemento
tupla_um_elemento = (10,)
# print(tupla_um_elemento)
# print(type(tupla_um_elemento))

tupla_varios_elementos = (7, 13, 8, 25)
# print(tupla_varios_elementos[1:3])

tupla_um_elemento = tupla_um_elemento + tupla_varios_elementos
# print(tupla_um_elemento)

# print(30 in tupla_varios_elementos)

# Sorted organiza os elementos da tupla em ordem crescente e transforma em lista
# print(sorted(tupla_varios_elementos))

nome = input('Informe o seu nome: ')
nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))

tupla_notas = (nome, nota1, nota2)

print(f'Dados do usuário: {tupla_notas}')