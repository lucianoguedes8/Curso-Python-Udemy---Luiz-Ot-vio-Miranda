'''Pads: são preenchimentos fixos que podem ser gerados no código.
Por exemplo, se eu tenho uma variável que é representada pela
string 'ABC', que tem 3 caracteres, e eu gostaria de formatar
esta variável para que ela tenha 10 itens ao invés de 3 (itens = caractere);
então eu posso preencher definindo PADS.
Preencher com PADS significa que adicionar caracteres a uma variável
até que sua quantidade de itens chegue até o limite de preenchimento fixo.
Se eu configurar para 10, então a variável da string 'ABC' será preenchida 
com 7 caracteres até chegar ao limite de 10.
Esses caracteres podem ser espaços vazios, letras, enfim...
Portanto, PADS definem preenchimentos fixos.'''


# Formatação básica de strings com f-strings:

"""Similar ao método .format e à interpolação de strings, a formatação
com f-strings será a mais utilizada no curso.
Esta formatação é dada basicamente pelo uso de PLACEHOLDER (espaço reservado)
dentro da f-string e pelo uso de dois pontos (:) dentro da f-string para
definir qual TYPE foi formatado."""

# Formatando através de f-strings com PADS:
""""Para formatar PADS nas f-strings é necessário informar ao intérprete
a posição de onde será definido o limite fixo de caracteres, se será
à esquerda da variável inserida no PLACEHOLDER, se será à direita dela
ou se a variável vai ficar no centro.

A posição é informada através de um caractere de posição, um caractere
que define a quantidade de itens à serem predefinidos pelo PAD e pelo
caractere que vai preencher o PAD.
> → Define o PAD à esquerda da variável formatada na f-string (variável à direita do PAD)
< → Define o PAD à direita da variável formatada na f-string (variável à esquerda do PAD)
^ → Define o PAD à esquerda e à direita na f-string (variável no centro)

Antes dos símbolos >, < ou ^ inseridos para definir a posição do PAD, é 
necessário inserir o caractere preenchedor do PAD. Pode ser uma letra, um
símbolo com $ ou até uma pontuação.
ESSES SÍMBOLOS SÓ FUNCIONARÃO SE NÃO TIVER NENHUM ESPAÇO E FOR APENAS O 
ITEM ISOLADO. Por exemplo:
f'{variavel: $^10} → Não Funcionará!!!
f'{variavel:$^funcionará} → Funcionará!
"""
variavel = 'ABC'
print(f'{variavel}') 
print(f'{variavel:x>10}')
print(f'{variavel: <10}.')
print(f'{variavel:$^10}.')
"""

# Formatando através de f-strings com caracteres de TYPES:
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal

= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')