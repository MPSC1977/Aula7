import os

os.system('cls')

def decoracao():
    print()
    print(30*'=')


def saudacao(txt):
    print(f'Olá {txt}')

    
def somar_valores(a, b):
    total = a + b
    med = (a + b) / 2
    # print(f'O total é: {total}')
    return total, med

# decoracao()
# print('iniciando programa')
# print('nome: ')
# print('idade: ')
# print('cidade: ')

# decoracao()
# print('Dados pessoais: ')
# print('CPF: ')
# print('RG: ')

# decoracao()
# print('Rede social: ')
# print('Linkedin: ')
# print('GitHub: ')
    
# print('INICIANDO O PROGRAMA')
# nome = input('Informe seu nome: ')

# saudacao(nome)
    
n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))

valor, media = somar_valores(n1, n2)

print(f' A soma é igual a {valor} e a média igual a {media}')
