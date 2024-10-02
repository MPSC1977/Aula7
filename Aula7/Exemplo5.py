import os

os.system('cls')

lst_previsoes = ['Nublado', 'Chuvoso', 'Tempestade', 'Ensolarado', 'Ensolarado']
lst_dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']

lst_dias_ensolarados = []
lst_dias_sem_sol = []

# for p in lst_previsoes:
#     if p == 'Ensolarado':
#         lst_dias_ensolarados.append(p)
#     else:
#         lst_dias_sem_sol.append(p)

# print(f'Dias ensolarados {lst_dias_ensolarados}')

# print(f'Dias sem sol {lst_dias_sem_sol}')

#Enumerate utilizado para transformar as 
for i, v in enumerate(lst_dias):
    if lst_previsoes[i] == 'Ensolarado':
        lst_dias_ensolarados.append(v)
    else:
        lst_dias_sem_sol.append(v)

print(f'Dias ensolarados {lst_dias_ensolarados}')

print(f'Dias sem sol {lst_dias_sem_sol}')