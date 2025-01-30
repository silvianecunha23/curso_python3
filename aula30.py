"""
# EXERCÍCIO 2
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite a(as) hora(s) atual (entre 0h e 23h): ')
minuto = input('Digite o(os) minuto(s) atual (entre 0min e 60min): ')
#print('Tipo do número antes do try/except:', type(hora))

try:
    hora = int(hora)
    minuto = int(minuto)

    dia = hora >= 0 and hora <= 11
    tarde = hora >= 12 and hora <= 17
    noite = hora >= 18 and hora <= 23

    hora_2 = hora >= 0 and hora <= 23
    minuto_2 = minuto >= 0 and minuto <= 60
    
   
    if hora_2 and minuto_2:

        if dia:
            print(f'Bom dia, a hora atual é {hora}:{minuto}.')

        elif tarde:
            print(f'Boa tarde, a hora atual é {hora}:{minuto}.')
            
        elif noite:
            print(f'Boa noite, a hora atual é {hora}:{minuto}.')

    else:
        print(f'A hora fornecida está fora do range.')
    
except:
    print('Dados faltantes ou não é um número!')