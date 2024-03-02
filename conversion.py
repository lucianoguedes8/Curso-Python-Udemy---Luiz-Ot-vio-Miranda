# Conversão de tipos, coerção.
# Também chamada de type convertion, typecasting, coercion.
# É o ato de converter um tipo em outro.

# Tipos imutáveis e primitivos:
# str, int, float, bool

# Uma str não é possível ser somada com um int:
# Por exemplo: print(1 + '1')
# Se o código for escrito desta forma, dará problema no programa.

# Classes de conversão (que parecem ser funções, mas não é):
# str(), int(), float(), bool()  
print(int('1'), type(int('1')))
print(end='\n')
# Aqui a string 1 foi convertida no int 1 e foi solicitada o tipo desta classe.
# O nome desta operação é coerção.

# Se somarmos um número float com um número int, o resultado será um número float.
print(float('1') + 1)
print(type(float('1') + 1), end='\r\n')
print(end='\n')
'''Note o resultado da função print, onde 2.0 ocorre com casa decimal, portanto
este número é um float.'''


# Todo bool que é algo vazio é dito como False.
print(bool(''))
# Todo bool que tem alguma coisa dentro é dito como True, mesmo que seja espaço.
print(bool(' '))

# A soma de duas strings corresponde a uma concatenação, ou seja, é juntado.
print(str(11) + 'b')

# O ato que todas essas classes representam (int(), float(), str(), bool()) é
# chamado de convertion, coercion, type casting, type convertion.