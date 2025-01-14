# Placeholder (...) espaço reservado para um código que ainda vou escrever.
# # f-strings: formatação de strings.
# Cálculo do IMC
nome = 'Ângela'
altura = 1.61
peso = 62.4

print()
print('1ª opção:')
imc = peso / (altura * altura)
print(nome, 'tem', altura, 'm de altura, seu peso é de', peso, 'kg e seu IMC é de', imc)

print()
print('2ª opção: usando f-strings')
formatado_f = f'{nome} tem {altura:.2f}m de altura, seu peso é de {peso}kg e seu IMC é de {imc:.2f}'
print(formatado_f)

print()
print('3ª opção: usando o método format')
a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c)
print(formato)