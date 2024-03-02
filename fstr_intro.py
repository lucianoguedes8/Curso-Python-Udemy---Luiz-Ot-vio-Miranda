# Introdução a f-strings:
'''As f-strings são strings formatadas. São textos que precisam
que o caractere (f) seja escrito antes no código. Assim, torna-se
possível inserir variáveis dentro de uma string e controlar casas
decimais, por exemplo.'''

nome = 'Luiz Otávio'
altura = 1.80
peso = 95              # Aqui, não há novidades. Apenas variáveis.
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

'''Uma variável pode ser uma string. Mas para uma string
conter uma variável, deve ser descrita como uma f-string
(inserindo o caractere (f) antes de abrir aspas) e também
colocar a variável entre chaves, ou seja: {variável}.'''

'''Para controlar as casas decimais de um float numa f-string,
é necessário colocar a variável entre chaves, inserir dois
pontos e digitar o comando que definirá quantas casas decimais
serão lidas no intérprete: .1f, .2f, .3f, .4f..., .nf
Portanto, segue-se a lógica: {variável:.2f}.'''

print(linha_1)
print(linha_2)
print(linha_3)

# Luiz Otávio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987