"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::] [início:fim:passo]
Obs. 1: a função len retorna a qtd de caracteres da str
Obs. 2: em Python normalmente o índice final não é incluído,
dessa forma para ir até o final deve omitir o fim [i:].
Obs.: qtd de caracteres é diferente de índices.
"""
variavel = 'Olá mundo'
print(variavel[4:7]) # mun
print(variavel[-5:-2]) # mun
print(variavel[::2]) # passo de 2 em 2
print(len(variavel))