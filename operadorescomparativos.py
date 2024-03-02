# Operadores Relacionais (Comparativos)

'''Sempre que igualamos uma variável a uma operação comparativa,
será atribuído à variável um valor boolean.
Ex: variável = 2 > 1 → Ou seja, variável passa a ser True, variável = True.'''
'''Este sinal de igual (=) é um operador de atribuição. É um operador
que atribui um valor algo. No caso da explicação acima, variável.'''
'''Portanto, (=) NÃO É um operador comparativo. O operador comparativo
da explicação acima é (>), que compara os valores de 2 e 1.'''



'''Os operadores >, >=, <, <= são utilizados para comparar ints e floats.'''
'''Os operadores == e != são usados para comparar qualquer dado (int, float, bool, str)'''


# Vejamos o que são operadores comparativos:
"""
Operadores de comparação (relacionais):
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
"""
maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'
print('Olha meu print aqui')

'''Podemos ler as variáveis no terminal através do Shell do Python.
Isso pode ser útil caso queiramos ler individualmente, sem a necessidade
de executar a função print.'''
'''Para isso, vamos utilizar as funções básicas que vimos no início do curso.
Digite no terminal:

pwd → Para mostrar o path do arquivo que você está manusando (pode ser
este arquivo "operadorescomparativos.py")

lf → Para mostrar o que tem na pasta do curso e datar os últimos acessos.

python -i operadorescomparativos.py → Para abrir o Shell e este arquivo
no terminal do VSCode.'''

# Agora digite os nomes das variáveis depois do símbolo (>>>) no terminal.