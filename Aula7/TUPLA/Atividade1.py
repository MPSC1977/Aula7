import os

os.system('cls')

nome = input('Informe o nome do funcionário: ')
cargo = input('Informe o cargo: ')
salario = float(input('Informe o salário: '))
idade = int(input('Informe a idade: '))

tupla_cadastro_funcionario = (nome, cargo, salario, idade)

print(tupla_cadastro_funcionario)