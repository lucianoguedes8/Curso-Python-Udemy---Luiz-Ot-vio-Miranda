# Função format:

'''Em Python, tudo é um objeto.
Definição de objeto: Um objeto em Python é uma única coleção de 
dados (atributos) e comportamento (métodos).
Isso corresponde a qualquer tipo de dado em Python.
Uma string é uma coleção de dados (caracteres) e comportamentos 
(format(), upper(), lower(), etc.). O mesmo se aplica a 
inteiros, flutuante, booleanos, listas e dicionários.'''

'''Quando uma função está dentro de um objeto, esta função é chamada
de método.
   Lembrando que tudo em Python é um objeto.
   Objetos têm ações, objetos podem fazer algumas ações 
   (subfunções), essas ações são chamadas de métodos.'''

# Exemplo de método:
a = 'AAA'
b = 'b'
c = 'c'
funcao_formatar = 'a={}'.format(a, b, c)
print(funcao_formatar)
print('\n')
'''A função .format é um método que formata o(s) valor(es) 
especificado(s) e os insere dentro do espaço reservado {} da string.
Logo {} = espaço reservado da string.
Neste caso, o método .format está subordinado a string 'a={}',
que é descrita pela variável funcao_formatar.'''

'''No caso, as variáveis a, b e c são os valores especificados que
serão formatados e inseridos na string 'a={}'.
PORÉM, apenas o valor de (a) foi inserido na string. Por que?'''

'''Primeiro, devemos analisar a anatomia do código:
funcao_formatar = variável
'a={}' = string ------> {} = espaço reservado da string
.format = método subordinado à string 'a={}'
(a, b, c), que estão dentro do método .format, são argumentos
    → Estes argumentos representariam as variáveis já descritas.

Dessa forma, foi formatado apenas o valor da variável -a- 
(apesar de não ter ocorrido nenhuma formatação) e depois este 
valor foi inserido dentro do espaço entre chaves {} da string
'a={}'. Mas por que?
→ Isso acontece porque no código ocorreu apenas 1 espaço
reservado da string 'a={}'. Por isso, o código formatou
e inseriu apenas o primeiro argumento do método .format,
o que aponta uma lógica de ordem para espaços reservados
{} que não têm valor. Ou seja, os argumentos são inseridos
conforme a ordem da esquerda para direita APENAS quando
não há nada dentro do espaço reservado {}.'''

# Vejamos o que acontece se utilizarmos mais espaços reservados:
funcao_formatar_2 = 'a={}, b={}, c={}'.format(a,b,c)
print(funcao_formatar_2)
print('\n')
'''Note que foi seguida a lógica de ordem dos argumentos
(da esquerda para a direita) na inserção das variáveis
nos espaços reservados {}.'''

# A Lógica de Ordem dos Argumentos:
'''Para cada função ou método, existem números que representam
a ordem dos argumentos dentro desta função ou métodos. Estes
números correspondem a como os argumentos são ordenados dentro
de uma função ou método. Começam sempre com 0, sendo zero
o número que sinaliza o primeiro argumento e a ordem sendo
sempre da esquerda para a direita.'''
# Exemplo: .format(a,b,c) → .format(0,1,2)
'''Estes números são chamados de ÍNDICES. Nós não os vemos,
pois estes estão sempre ocultos e só servem como marcadores
da ordem dos argumentos.'''
'''Portanto, se preenchermos os espaços reservados {} da string
associada a função .format com os índices dos argumentos,
o intérprete lerá os argumentos específicos nesses espaços {}.'''
funcao_formatar_3 = 'a={1}, b={0}, c={2}'.format(a,b,c)
print(funcao_formatar_3)
print('\n')

# Novamente: índices são números ocultos que definem ordem de argumentos.

# Parâmetros e parametrização:
'''Podemos nomear argumentos conforme nosso desejo. Um argumento nomeado
manualmente pelo usuário é chamado de PARÂMETRO NOMEADO. Logo, o 
processo de nomear argumentos é chamado de PARAMETRIZAÇÃO.'''
# Parâmetros nomeados atuam como índices, só que não apontam ordem!
                      # Não necessariamente, mas se quisermos, sim.

# Exemplo:
funcao_formatar_4 = 'b={nome2} c={nome3} a={nome1}'.format(nome1=a, nome2=b, nome3=c)
print(funcao_formatar_4)
print('\n')
'''Toda vez que nomearmos um argumento (com um parâmetro nomeado)
devemos nomear todos os argumentos dentro do método ou função;
pois se não fizermos isso, ocorrerá erro.'''

# Para facilitar:
'''Podemos primeiro criar uma variável para descrever uma string
e depois criar o método .format subordinado a esta variável.'''
string_1 = 'a={} b={} c={}'
string_2 = 'a={nome1} b={nome2} c={nome3}'
funcao_formatar_5 = string_2.format(nome3=c, nome1=a, nome2=b)
funcao_formatar_6 = string_1.format(a, b, c)
funcao_formatar_7 = string_2.format(nome1=c, nome2=a, nome3=b)
print(funcao_formatar_5)
print(funcao_formatar_6)
print(funcao_formatar_7)
'''Variável string_1 → Respeita a ordem dos índices.'''
'''Variável string_2 → Respeita os parâmetros descritos nas variáveis
funcao_formatar_6 e funcao_formatar_7.'''



