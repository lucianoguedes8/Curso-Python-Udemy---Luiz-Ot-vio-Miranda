'''Índices são valores que atribuem ordem a um código ou objeto. Os
índices podem ser atribuídos a strings inteiras ou para cada letra
de uma string.'''

'''Iterável → Código que pode ser navegado item por item, por
exemplo, as strings. A string 'Rocky' é iterável, pois é possível
navegar em cada item deste código, ou seja, é possível navegar
nas letras R, o, c, k, y.
A navegação é realizada através dos índices do código, sendo
os índices números ordenados para cada item. Ex: R → 0, o → 1,
c → 2, k → 3, y → 4. Lembrando que os índices são valores que
implicam em ordem.
    Os índices podem ser aplicados à itens de código, como está
escrito acima. No entanto, os índices também podem ser
classificados como positivos (parágrafo acima) e negativos.
Os índices negativos, no caso da string acima, são descritos como:
R → -5, o → -4, c → -3, k → -2, y → -1.
    Pois é... Os índices negativos começam do último item e não
iniciam a ordenação no índice zero, mas sim no índice -1.'''

# Acessando índices de itens de strings:
'''Para acessar um índice de um determinado item de uma string, utiliza-se
colchetes no código. Exemplo:'''
print('Rocky'[0])
rocky = 'Rocky'
print(rocky[3])
'''Aqui, acessamos o primeiro e o quarto item da string 'Rocky'. Podemos
acessar tanto através de uma variável, como na própria string descrita.
A função print só foi utilizada para imprimir o programa no terminal.'''

# Operadores lógicos in/not in:
'''São operadores para determinar se um objeto está dentro de outro ou não.
O operador in, por exemplo, pode afirmar que um item de string está dentro
de uma string.
   Podemos usar a função print para fazer essa checagem:'''
print('o' in rocky)
'''Aqui, usamos um boolean para checar se a vogal 'o' está dentro
da variável rocky (que representa a string 'Rocky').'''
print('ock' in 'Rocky')
print('Will' in rocky)
print('\n')
'''Caso não esteja dentro, o resultado do programa irá imprimir o
bool False.'''

'''Já o operador not in, representa o contrário da função in. Este
pode ser usado para afirmar que um item de string NÃO está dentro
de uma string.'''
print('Zero' not in rocky)
print('Geologia' not in rocky)
print('ock' not in rocky)
print('\n')
'''Novamente, o retorno da função print, nesse caso, será um boolean.'''

'''Através desses operadores, podemos criar um simples joguinho no
programa.'''
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')