# Exercício - Condicionais
print('Exercício - Condicionais')
print('\n')


primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite um segundo valor: ')
print('\n')

resposta_1 = f'{primeiro_valor} é maior que {segundo_valor}'
resposta_2 =f'{primeiro_valor} é menor que {segundo_valor}'

if primeiro_valor > segundo_valor:
    print(resposta_1)
elif primeiro_valor < segundo_valor:
    print(resposta_2)
else:
    print(f'Não foi feita uma comparação onde o primeiro ou o segundo valor são diferentes')

# Note que não é necessário criar uma variável para imprimir uma f-str no terminal.


