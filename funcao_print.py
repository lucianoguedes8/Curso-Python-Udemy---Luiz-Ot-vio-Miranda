'''
A função print é utilizada para exibir algo na tela, no terminal.
Dito isso, a anatomia da função print é descrita como:

print(argumentos)
print(1, 0, 1) → print(argumento, argumento, argumento)

Os parenteses servem para armazenar o argumento na função.
Novamente, print significa imprimir algo no terminal.
'''

# Os argumentos podem ser classificados como não-nomeados e nomeados.

# Exemplos de argumentos não-nomeados:
print(1, 0, 0)
print(0, 0, 3)

# Para nomear argumentos, é necessário aplicar alguma subfunção que discrimine-os:
print(1, 0, 0, sep='-') # Este é um exemplo de argumento nomeado.

# Subfunção sep='?': É a função que define o modo de separação de argumentos. Ex:
print(1, 0, 0, sep='Rocky') # Pode ser escrito qualquer coisa, mas entre aspas.
print(5, 0, 0, sep='') # Digitando nada, a função atuará, mas nada exibirá no terminal.

'''
Existem algumas funções no Python que já são aplicadas automaticamente.
Este é o caso da QUEBRA DE LINHA, descrito pela função:

end=''      Dentro das aspas, pode ser escrito \n\r ou só \n

\n\r, que significa Carriage Return + Line Feed no caso do Windows;
ou, somente \n, que significa Line Feed, no caso de outros sistemas operacionais.

(LF) Line Feed e CRLF (Carriage Return + Line Feed) referem-se ao modo pelo qual
a linha de texto do código é finalizada.
Ambos são utilizados para um controle das linhas.

LF: no Windows representa a ida para uma próxima linha.
CRLF: representa união entre LF e o CR, que determina o retorno do cursor ao
início da linha.
'''

# Subfunção QUEBRA DE LINHA, ou seja, end='':

print(44, 44, 0, end='\n\r') 
# Neste caso, nada será exibido, pois \n\r já é aplicado automaticamente.

print(33, 33, 0, end='##')
print(22, 22, 0)
# Já neste caso, não haverá quebra de linha exibida no final do código no terminal.

print(1, 1, 1, end='\n\r##')
print(2, 2, 2)
# Já neste, ocorre a quebra de linha e depois é adicionado ## no início da próxima linha.
'''Neste último caso, se ## for colocado antes de \n\r, haverá quebra de linha,
porém ## será adicionado no final da primeira linha.'''


'''A cerquilha, nesses últimos casos, não cumpre sua função, pois está
subjulgada à função end='''

# Lembre-se: Print com P maiúsculo não existe em Python.