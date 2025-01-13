# Conversão de tipos, coersão (concatenar)
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float e bool

print(int('1'), type(int('1')))
print(type((float('1')) + 1.0), (float('1')) + 1.0)
print(bool('')) # vazio = False
print(bool(' ')) # com espaço = True
print(str(11) + 'b')