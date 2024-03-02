# Operadores Aritméticos
'''São os operadores matemáticos utilizados para realizar contas'''
print(end='\n')

# Os mais complicados são os operadores de divisão. Portanto, preste atenção neles.

# Operador de adição (+):
resultado_adicao_1 = 10 + 10
resultado_adicao_2 = 10 + 10
print('Adição 10 + 10:', resultado_adicao_1)
print('Adição 10 + 5:', resultado_adicao_2)
print(end='\n')
# Note que foi escrito um código de uma variável para exemplificar uma adição.

# Operador de subtração (-):
resultado_subtracao_1 = 10 - 5
resultado_subtracao_2 = 10 - 2
print('Subtração 10 - 5:', resultado_subtracao_1)
print('Subtração 10 - 2:', resultado_subtracao_2)
print(end='\n')

# Operador de multiplicação (*):
resultado_multiplicacao_1 = 10 * 10
print('Multiplicação 10 * 10:', resultado_multiplicacao_1)
print(end='\n')

# Operador de divisão (/):
resultado_divisao_1 = 10 / 2  # Toda operação de divisão retorna um float como
resultado_divisao_2 = 10 / 3  # resultado, independente se for uma divisão de int.
print('Divisão 10 / 2:', resultado_divisao_1)
print('Divisão 10 / 3:', resultado_divisao_1)
'''Portanto, note que o resultado desta operação 
sempre apresentará casas decimais.'''
print(end='\n')

# Operador de divisão inteira (//):
# É chamado de divisão inteira porque retorna números com casas decimais zeradas.
# NO ENTANTO, o resultado pode ser um float também.
divisao_inteira_1 = 10 // 3
divisao_inteira_2 = 10 // 3.2
divisao_inteira_3 = 10 // 2
print('Divisão Inteira 10 // 3:', divisao_inteira_1)
print('Divisão Inteira 10 // 3.2:', divisao_inteira_2)
print('Divisão Inteira 10 // 2:', divisao_inteira_3)
'''Portanto, note que o resultado da variável divisao_inteira_2
é um float de casas decimal zerada.'''
print('\n')

# Operador de exponenciação (**):
exponenciacao_1 = 2 ** 10
print('Exponenciação 2 ** 10:', exponenciacao_1)
# Tome cuidado para este operador não gerar resultados muito grandes.
print('\n')

# Operador de módulo (%), utilizado para definir o resto de divisões:
modulo_1 = 55 % 2
modulo_2 = 10 % 5
modulo_3 = 10 % 3
'''Quando o código é escrito 'x % y', este quer encontrar 
o resto da divisão de x por y.'''
print('Módulo 55 % 2:', modulo_1)
print('Módulo de 10 % 5:', modulo_2)
print('Módulo de 10 % 3:', modulo_3)
# Esta operação é muito útil para saber se um número é múltiplo de outro.
print('\n')


'''A partir desses operadores (na verdade, do resultado dessas operações),
podemos definir booleans utilizando o operador de afirmação de igualdade (==).'''
print(10 % 8 == 0)
'''Lê-se o argumento como: afirmo que 10 % 8 é igual a 0.
Ou seja, afirmo que o resto da divisão de 10 por 8 é igual a zero.
Se esta afirmação for verdade, então retornará a bool True.
Porém, se for mentira, então retornará a bool False.'''
print(16 % 8 == 0)
# Lembre-se que toda bool tem letra maiúscula no início.
print(10 % 4 == 2)
print(15 % 2 == 0)
print(16 % 2 == 0)

