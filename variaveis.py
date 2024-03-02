# Variáveis são usadas para salvar algo na memória do computador.
'''PEP8: inicie variáveis com letras minúsculas, pode 
usar números e underline _.
Exemplos de variáveis:
cachorro_grande                        PEP8 é um tutorial de Python.
batom_rosa
materia_chata
Ou até mesmo o nome variavel...

Isso quer dizer que um variável é qualquer texto que pode ser atribuído um valor
(como int, float ou boolean) ou até mesmo outro texto ('string')!
Lembre-se: variaveis salvam algo na memória do computador.
'''

# O sinal de = é o operador de atribuição. Ele é usado para
# atribuir um valor a um nome (variável).
# Uso: nome_variavel = expressão

# nome_completo = 'Luiz Otávio Miranda'
# soma_dois_mais_dois = 2 + 2
# int_um = int('1')

# Aplicando variáveis nas funções:
int_um = int('1')
print(int_um, type(int_um))
print('\n')
# Note que acima ocorreu uma operação de atribuição e uma função.

# Aplicando variáveis na função print, com strings e boolean.
nome = 'Luiz'
idade = 17
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade:', idade)
print('É maior?', maior_de_idade)
'''Note que neste último código, além do bool definido na
variável maior_de_idade, são impressas no terminal strings 
que não produzem o menor efeito no programa, a não ser sua
própria exibição. Essas strings vêm das variáveis e
também vêm na própria função print.'''