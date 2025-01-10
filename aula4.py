# Tipos int e float
# int -> número inteiro
# o tipo int representa qualquer número positivo ou negativo
# int sem sinal é considerado positivo
print(11)
print(-11)
print(0)

# float -> número com ponto flutuante
# o tipo float representa qualquer número positivo ou negativo com ponto flutuante
# float sem sinal é considerado positivo
print(1.1, 2.2)
print(11.12, 23.23)

# a classe type mostra o tipo que o Python inferiu ao valor.
# pq a classe type inicia com letra minúscula??
# TUDO em Python é um objeto!
print(type(-2.1)) # float
print(type('-2.1')) # str
print(type(21)) # int