# Debugger do Python
'''Debbuger é um depurador de código-fonte interativo 
para programas Python. Ele permite a configuração 
de pontos de interrupção (condicionais) e etapas 
únicas no nível da linha de origem, inspeção de 
quadros de pilha, listagem de código-fonte e 
avaliação de código Python arbitrário no contexto 
de qualquer quadro de pilha. Ele também permite 
depuração post-mortem e pode ser chamado sob 
controle do programa.'''
'''O Debugger do Python no VSCode está localizado no ícone
de um inseto junto a um triângulo da barra de tarefas 
(barra vertical) à esquerda do painel de interface do VSCode.'''
'''Para acessar o Debugger do Python, clique no ícone.'''
'''Se você quiser, pode até alterar as configurações do debugger, 
mas isso não é interessante agora.'''

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

'''Se você clicar na linha do código, com o debugger aberto,
você irá criar um BREAKPOINT, como diz a legenda da bolinha
vermelha.'''
'''O BREAKPOINT faz o intérprete parar de ler o programa
na linha selecionada (antes mesmo de executar o código da
linha marcada com a bolinha vermelha).'''
'''A partir disso, existem comandos no canto superior esquerdo
que podem pular a linha do código, que podem ler a linha
subjacente, que podem parar o depurador...''' # São comandos do debugger!

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

if 10 == 10:
    print('Outro if')

print('Fora do do bloco do primeiro if')

# Note que o debugger é um leitor de código, um depurador.
# O debugger respeita a ordem de interpretação do programa.
# A ordem é, sempre: de cima para baixo, da esquerda para a direita.