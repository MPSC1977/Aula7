import os

os.system('cls')

def par_impar(a):
    resposta = ''
    valor = a % 2
    if valor == 0:
        resposta = 'Par'
    else:
        resposta = 'Ímpar'
    
    return resposta


n = int(input('Informe um número: '))
resp = par_impar(n)
print(f'{n} é {resp}')
