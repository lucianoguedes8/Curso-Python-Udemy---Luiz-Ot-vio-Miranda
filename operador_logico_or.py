# Operadores Lógicos - or

'''É um operador utilizado para adicionar informações
independentes, de maneira coordenativa ALTERNATIVA.
Bastante utilizada em situações de operações condicionais.'''

'''Se qualquer valor for considerado verdadeiro, a 
expressão inteira será avaliada como verdadeira!
Isso já difere bastante o operador lógico or do and.'''

'''São considerados truthy qualquer valor do Python,
exceto os valores falsy: 0, 0.0,''(string vazia) e False.'''

'''Lembrando que None = não-valor. Mas isso será usado
mais para frente...'''

# Aplicação do operador lógico or:

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
# Aqui o usuário pode imaginar que deve digitar 'E' ou 'e').
# Por isso, a operação condicional deve auxiliar este sistema.

senha_permitida = '123456'

'''Na condicional abaixo, é necessário que utilizemos os 
parenteses para que a operação condicional não tenha nenhuma
ambiguidade. Isso facilitará o intérprete e até mesmo 
qualquer outro programador que leia o código.
Lembra a precedência dos operadores aritméticos?
Tudo que estiver dentro de () será resolvido primeiro!'''
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
print('\n')
'''Ou seja, o operador or foi utilizado para promover
alternativas de condições (no caso, a resposta do usuário).'''

'''Depois de checada a primeira condição, através da
interpretação das alternativas, será checado resto do código
conforme o padrão de leitura do intérprete. Afinal, ainda
tem um operador aditivo no bloco de código do if.
Lembrando que OPERAÇÕES CONDICIONAIS RETORNAM VALORES BOOLEANS.'''

'''Se qualquer uma das condições checadas, diante do padrão
de alternativas for truthy, o intérprete retornará o valor 
associado ao bloco de códigos do if.'''

# O mesmo pode ser avalidado na função print.
# Esta avaliação é conhecida como avaliação de curto circuito.
'''Um valor truthy também provoca um curto circuito, reduzindo
toda a informação de um conjunto de booleans ao primeiro valor
truthy no código, mesmo que hajam valores falsy.'''
print('Avaliação de Curto Circuito:')
print(True or False)
print('ABC' and 0 or True or 0.0)
# Note que 'ABC' não está sendo confrontado através do operador or.
print(False or 'Desodorante' or True or False or True)
'''Quando qualquer valor confrontado com valores truthy,
através do operador or, ocorrerá sempre o retorno do primeiro
valor truthy dentro da expressão em que ocorreu o confronto
(SOMENTE QUANDO O CONFRONTO É ATRAVÉS DO OPERADOR OR).
Claro, primeiro segundo a ordem de interpretação do código.'''

'''IMPORTANTE: se na operação condicional ocorrer um
confronto pelo operador or e houver um valor truthy,
a operação SERÁ executada. Isso acontece porque
as operações condicionais retornam valores booleans que
impedem ou não que a operação aconteça. Se retornar
True, a condição da operação é aplicada e o resto
do bloco é executado. Se retornar False, a operação
não ocorerrá. Exemplo:'''
if 0 or 1:
    print(True or 1) # True é o primeiro, então este será impresso.
    print(True and 1) # Aqui, como tem and, retornará o último.

# Um exemplo curioso...
senha = input('Senha: ') or 'Sem senha'
print(senha)
'''Se o usuário não digitar nada, será um valor falsy.
Então será impresso no terminal a string 'Sem senha'.
Isso porque o input é um valor falsy. Logo, seguindo
a lógica do operador or, será impressa a primeira
alternativa truthy na ordem do intérprete do código.'''