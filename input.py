# Função input:

'''Função utilizada para coletar dados. Só é utilizada 
para ser exibida no terminal, onde o usuário do programa
 irá fornecer dados.'''
input('Qual o seu nome? ')
print('\n')
# Aqui, foi apenas definido uma pergunta (string) no terminal.
# O usuário deve responder essa string no terminal com outra string.
# A resposta do usuário serão os dados coletados.
# Esses dados coletados irão permitir que o programa continue rodando.

'''Depois que o programa é executado, a função input('') joga
uma string no terminal. Depois disso, o usuário do programa
deve digitar algo que será retornado à função para dar 
continuidade ao programa.
   Isso possibilita atribuir valores a uma variável através 
dos dados do usuário, por exemplo.'''
'''Função input só é exibida no TERMINAL. No OUTPUT não funciona.'''
'''O programa só irá continuar a rodar depois dessa coleta de dados.'''

# Anatomia do código input(''):
'''input → função
   () → armazena o argumento
   '' → define o argumento armazenado como uma string'''

# Coletando dados do usuários para atribuir valores a uma variável:
nome = input('Qual o seu nome? ')
print(f'O seu nome é {nome}')
print('\n')
'''Note que, pelo que foi construído no programa,
a função print retornará uma f-string com os dados 
coletados.'''

# Somando strings com a coleta de dados do usuário:
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')
print(f'A soma dos números, que ainda estão como str, é: {numero_1 + numero_2}')
# Note que a soma dos dados coletados é uma CONCATENAÇÃO.

# Somando ints com a coleta de dados do usuário:
'''É necessário converter a string do input para um int.
POR ISSO, é necessário usar as funções de TYPECONVERSION,
como int(), float()...'''
'''Se numero_1 e numero_2 já foram definidos no input de dados, então:'''
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)
print(f'A soma dos números é: {int_numero_1 + int_numero_2}')
'''Já neste caso, pelo que foi definido no programa, a soma
dos dados coletados pelo usuário é uma ADIÇÃO DE INT.'''
'''Se caso fosse coletado caracteres que não sejam INT ou FLOAT,
o programa irá quebrar (dar).'''

'''O mais importante desse código é que, a depender do input
de dados do usuário, o programa rodará em um fluxo diferente.
O programa terá resultados diferentes, no final.'''