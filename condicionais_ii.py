# Fluxo do programa - Condicionais

'''Podemos ter várias condições dentro de um mesmo bloco de códigos.
No entanto, o intérprete prioriza a execução de funções subordinadas
(em um mesmo bloco de códigos) da primeira condição satisfeita no
bloco.'''
'''A ordem do fluxo do programa em um mesmo bloco de código é:
if → Que, no caso, é sempre primeira condição
elif → De cima para baixo, no mesmo bloco
else → Quando nenhuma condição é satisfeita.'''

'''Booleans também podem determinar variáveis e posteriormente
essas variáveis podem ser usadas nas funções if/elif/else.'''

condicao1 = False
condicao2 = True
condicao3 = False
condicao4 = False

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

'''Neste caso, como if não foi satisfeito e o elif da variável
condicao2 foi satisfeita, será exibido no terminal o código
associado a satisfação do primeiro elif de cima para baixo.'''
'''Note que podem ter vários elif dentro de um mesmo bloco.'''
'''Caso os booleans das variáveis sejam mudados, o fluxo do
programa mudará, porém a ORDEM DE INTERPRETAÇÃO desse fluxo
será SEMPRE A MESMA.'''
'''Com o fluxo modificado, resultados diferentes serão exibidos
no terminal.'''

# Outro bloco:
if 10 == 10:
    print('Outro if')
'''Este bloco, no caso, independe de variáveis e independe
do bloco de if/elif/else acima.'''

# Caso uma função esteja fora do blocos, ela será interpretada normalmente.
print('Fora do if')