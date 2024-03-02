# Operador lógico not:

'''
Usado para inverter expressões:
not True = False
not False = True
'''

senha = input('Senha: ')
if not senha:
    print('Você não digitou nada.')
print('\n')

# Para vermos como ocorre:
print(not True)  # Retornará False
print(not False)  # Retornará True

print(not 1) 
'''Retornará False, pois not é operador que inverte bool.
Como 1 é um valor truthy, então será retornado o bool False.'''
print(not 0) 
'''Retornará True, pois not é operador que inverte bool.
Como 1 é um valor falsy, então será retornado o bool True.'''