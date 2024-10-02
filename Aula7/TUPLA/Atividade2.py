import os

os.system('cls')

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe outro número: '))
n3 = int(input('Informe outro número: '))
n4 = int(input('Informe outro número: '))
n5 = int(input('Informe outro número: '))

tupla_numeros = (n1, n2, n3, n4, n5)

maior_numero = max(tupla_numeros)
menor_numero = min(tupla_numeros)
total = sum(tupla_numeros)
numeros_ordenados = sorted(tupla_numeros)

print(f'O maior número é: {maior_numero}')
print(f'O menor número é: {menor_numero}')
print(f'A soma dos valores é igual a: {total}')
print(f'Aqui estão seus números em ordem crescente: {numeros_ordenados}')
