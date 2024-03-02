# Interpolação básica de strings:
'''A função de interpolação é bem similar ao método .format, que é uma
subfunção utilizada para formatar algo e inserir num espaço reservado.
No entanto, para esta aula, a função de interpolação é utilizada
para inserir objetos em uma string, sendo representada pelo
caractere % e acompanhada por um argumento entre parênteses.
Dessa forma, sua anatomia é descrita como:
% (argumento, argumento, argumento).
Além disso, a interpolação deve ser descrita depois da string em questão
e sempre deve haver um espaço entre o símbolo % e os argumentos entre
parênteses.'''

"""No entanto, além do caractere %, é necessário utilizar outros caracteres
dentro da string para que a interpolação possa realizar a inserção, 
reconhecendo qual o TIPO de objeto. Esse carectere %, em conjunto com
o caractere do TIPO, agirá como um espaço reservado. No caso, este
suposto espaço pode ser chamado de PLACEHOLDER.:

s - string
d e i - int      # É como se fosse uma typeconversion dentro da interpolação.
f - float
x e X - Hexadecimal (ABCDEF0123456789)

No caso, esses caracteres também devem ser acompanhados por % na string
em que será inserido o objeto!
O %d é um PLACEHOLDER (marcador de posição). Ele é usado para reservar 
números inteiros. Neste caso, numa string.
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('\n')
# Note que os objetos inseridos na string (variavel) podem não ser strings!
'''Lembre que, assim como no método .format, para inserir floats e 
controlar suas casas decimais, antes da letra f deve ser posto um ponto e um
número para definir a quantidade de casas decimais desejadas.
   No caso, o exemplo de inteporlação acima utiliza duas casas decimais,
expresso pelo termo %.2f'''

'''Hexadecimais são números formados por letras de A até F e algarismos de
0 a 9. São números descritos pela seguinte configuração: ABCDEF0123456789.
Logicamente, cada letra ou algarismo dessa configuração pode variar segundo
o alfabeto ou o conjunto de algarismos naturais.
Isso não é específico do Python, isso vem da matemática.'''

print('O hexadecimal de %d é %08X' % (1500, 1500))
print('\n')


# Um exemplo de programa para criar hexadecimais:
print('Bem-vindo(a) ao gerador de hexadecimais do Rocky.')
strnumero = input('Insira um número aqui: ')
numero = int(strnumero)
print('O hexadecimal do %d é %04x!' % (numero, numero))


