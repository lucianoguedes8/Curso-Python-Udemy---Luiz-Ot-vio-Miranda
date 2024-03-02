# Operadores Lógicos - and

'''É um operador utilizado para adicionar informações
independentes, de maneira coordenativa ADITIVA.
Bastante utilizada em situações de operações condicionais.'''

'''Veremos que quando utilizamos o operador lógico and para
examinarmos uma situação condicional, todas as condições
precisam ser verdadeiras. Se não, o uso do and retornará
o resultado de uma condição falsa.'''

'''Se qualquer valor for considerado falso, a 
expressão inteira será avaliada naquele valor.'''

'''São considerados falsy: 0, 0.0,''(string vazia) e False.'''

'''Também existe o tipo None que é usado para 
representar um não-valor. Ou seja: None = não-valor.'''

# Aplicação do operador lógico and:

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
# Aqui o usuário deve digiar S ou E (maiúsculo).

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
print('\n')
'''Ou seja, o operador lógico and foi utilizado para
o programa checar duas coisas: o input [E] e se a
senha digitada == senha permitida.'''
'''Lembra que todas as expressões precisam ser verdadeiras?
Pois é. Isso acontece porque, apesar desta aula ser voltada
para um operador lógico que cumpre um papel aditivo de
informação, estamos também aplicando operações condicionais.
OPERAÇÕES CONDICIONAIS RETORNAM VALORES BOOLEANS.'''

'''Lembra que o intérprete lê da esquerda pra direita e de
cima para baixo? Pois bem.
O programa irá checar os blocos associados a if e else.
Se a primeira condição chegada for verdadeira, o programa
checará a próxima condição adicionada por meio do
operador lógico and.'''
'''Se qualquer uma das condições checadas for falsy, o 
intérprete retornará o valor associado ao bloco de códigos
da condição falsa (no caso, retornará o que está programado
 no else).'''

# O mesmo pode ser avalidado na função print.
# Esta avaliação é conhecida como avaliação de curto circuito.
'''Ou seja, um valor falsy provoca um curto circuito, reduzindo
toda a informação de um conjunto de booleans a um valor falsy,
mesmo que hajam valores verdadeiros.'''
print('Avaliação de Curto Circuito:')
print(True and False and True)
print(True and 0 and True)
print('Desodorante' and True and False and True)
'''Diante de somente a presença de operadores lógicos and,
quando qualquer valor confrontado com valores falsy
ocorrerá sempre o retorno do primeiro valor falsy dentro 
da expressão em que ocorreu o confronto (SOMENTE QUANDO 
SÓ TIVER AND).'''

'''IMPORTANTE: se na operação condicional ocorrer um
valor falsy, não será executada a operação. Isso acontece 
porque as operações condicionais retornam valores booleans 
que impedem ou não que a operação aconteça. Se retornar
True, a condição da operação é aplicada e o resto
do bloco é executado. Se retornar False, a operação
não ocorerrá. Exemplo:'''
if 0 and 1:
    print(True and 1)
'''O 0 (zero) de 0 and 1 avalia como falsy. 
O corpo do if não será executado.'''