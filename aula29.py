"""
# EXERCÍCIO 1
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')
print('Tipo do número antes do try/except:', type(numero))

try:
    numero = int(numero)
    verificar_numero = numero % 2 == 0

    if verificar_numero:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é ímpar.')
    
    print('Tipo do número depois do try/except:', type(numero))
except:
    # Se deixar espaço em branco, digitar caracteres ou qualquer outra coisa:
    print('Isso não é um número!')

########################################################
# Segunda opção de solução:
# entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'
#     if par_impar:
#         par_impar_texto = 'par'
#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')