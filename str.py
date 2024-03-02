#
"""
Python = Linguagem de programação cujo tipo de tipagem = Dinâmica / Forte.
Tipagem Dinâmica → Implica no fato que o intérprete entende todas as informações
no código, sem precisar dizer que um código representa um número ou um texto. Ou
seja, o tipo pode ser atribuído dinamicamente ao Python.
Tipagem Forte → Não produz a conversão automática de dados.

str -> string -> texto
Strings são textos que estão dentro de aspas. Podem estar dentro de função.
DocStrings são tipos de strings. Estão dentro de aspas triplas, fora de função.
"""

print(1234) # Neste caso, não são strings. São números.
'''No caso, o Python reconhece-os como números e como números inteiros, por
ser uma linguagem de tipagem dinâmica.'''

print('Rocky') # Neste caso, são strings!

# As strings podem estar dentro de aspas simples. Ex:
print('Luiz Otávio')
print(1, 'Luiz "Otávio"')
# Se a palavra Otávio não tiver sido fechada com aspas, irá dar problema.
# Note que há aspas da função print e aspas da string.

# Também podem estar dentro de aspas duplas. Ex:
print("Rocky Balboa")
print(2, "Rocky 'Balboa'") 
'''Neste caso, o número 2 não é uma string e as aspas simples em Balboa serão
exibidas no terminal por estarem fechando uma parte da string. Porém, as 
aspas duplas nesse caso estão DEFININDO a string Rocky Balboa.
   Poderia ser o inverso, com as aspas duplas fechando o texto Balboa e
as aspas simples definindo a string Rocky Balboa.
   PORÉM, o número 2 é um argumento, assim como a string Rocky Balboa, onde
o termo Balboa está sob aspas.'''


# Caractere de escape (\) → Lê-se barra invertida:
print("Luiz \"Otávio\"")
# É utilizada para fazer as aspas aparecerem no terminal, reconhecendo-as como string.
'''É necessário utilizar a nota de escape pois as aspas NÃO FORAM DIFERENCIADAS,
e isso gerará problema ao rodar o programa.'''

# r → Utilizado para fazer o caractere de escape ser exibido no terminal.
print(r"Luiz \"Otávio\"")


'''OU SEJA... os caracteres \ e r só servem para complicar o código. É muito
mais simples dicernir aspas duplas de aspas simples para fazer a porcaria 
das aspas serem exibidas no terminal.'''