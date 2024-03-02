# Introdução if/elif/else

# Blocos de Código:
'''São conjuntos de códigos que estão subordinados a outro.'''
'''Há um código coordenador e códigos subordinados.'''
'''O código coordenador é um código que termina com ":"  '''
'''Os códigos subordinados estão abaixos do código coordenador
e são afastados do início da linha por 4 espaços. A tecla TAB
realiza esse afastamento.'''
'''Esse modelo de construção de blocos de código é utilizado
apenas para algumas funções. Algumas dessas funções são:
if, elif e else.'''
'''Todas as funções que estiverem fora dos blocos irão rodar
normalmente depois que o/os bloco/blocos anteriores forem rodados.'''

# O operador ==:
'''Este sinal quer dizer "for igual a". '''
'''No caso, este é um operador comparativo.'''
'''Quando é só um sinal de igual (=), é um operador de atribuição.'''

# Operadores de atribuição são utilizados para definir valores para variáveis.
# Já os operadores de comparação, para comparar valores.


# Funções if / elif / else → se / se não se / se não:
'''São funções que implicam em reações (novas funções) a 
depender de uma dada condição.'''
'''Essas funções criam BLOCOS DE CÓDIGOS.'''
'''Necessitam de operadores comparativos, como "==". '''

# Se isso for isso, criará um bloco de códigos dessa forma → função if
# Se isso não for isso, mas for igual a isso, criará outro bloco → elif
# Se não for nenhum desses, criará este outro bloco → else

'''Primeiro, é necessário criar uma variável, através da coleta
de dados, que forneça duas ou mais opções para o usuário.'''
entrada = input('Você quer "entrar" ou "sair"? ')
'''Lembre-se de dar um espaço no final do texto de input
para o usuário responder com o carregamento de dados, 
mas antes das aspas da string na pergunta.'''
if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair.')
print('\n')

print('Esta string está fora dos blocos associados as funções condicionais anteriores.')
print('\n')

# Interdependência das funções condicionais:
'''As funções condicionais são interdependentes. Ou seja,
elif e else dependem da função if. Caso não esteja prescrito
no código a função if, então as funções elif e else não funcionarão.'''
'''Isto faz sentido, porque não há como ter um evento "se não se" ou 
"se não" se não tiver tido um "se".'''
'''A função elif pode ser usada várias vezes na mesma situação
de interdependência, criando vários blocos.'''
rocky = input('O Rocky "roncava pouco", "roncava muito" ou "não roncava" enquanto dormia? ')
if rocky == 'roncava pouco':
    print('Então ele não incomdava ninguém e era muito fofinho dormindo.')
elif rocky == 'roncava muito':
    print('Então, ainda assim ele não incomodava ninguém e era muito fofinho dormindo.')
elif rocky == 'não roncava':
    print('Então ele incomodava menos ainda e era muito fofinho.')
else:
    print('Você não digitou nem "roncava pouco", nem "roncava muito" e nem "não roncava".')
print('\n')

print('Esta string não faz parte de nenhum dos blocos acima, mas está associada a continuidade do programa.')

# PORÉM, if não depende de elif ou else, pois é a primeira condição.
banana = input('Pode se dizer que "sim", banana é uma fruta saborosa? ')
if banana == 'sim':
    print('Não, não pode. Você está errado.')
    print('De qualquer forma, banana sendo ruim ou não...')
    print('...não são necessárias as funções elif e else para executar a função if.')
'''Se for digitada qualquer coisa além de sim no terminal, nada acontecerá.'''
