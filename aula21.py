# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  Â n g e l a
# -6-5-4-3-2-1

nome = 'Ângela'
print(nome[2]) # g
print(nome[-4]) # g

# (o Python itera em nome para encontrar)
print('Â' in nome) # True, pois está em nome 
print('zero' in nome) # False, pois não está em nome

print(10 * '-') # Negação
print('Âng' not in nome) # False
print('zero' not in nome) # True

print(10 * '-')
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')
if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')