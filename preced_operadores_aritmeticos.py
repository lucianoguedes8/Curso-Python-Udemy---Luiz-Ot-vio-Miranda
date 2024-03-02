# Precedência dos Operadores: diz respeito a ordem em que os operadores são executados.

# 1º. (n + n) → A ordem dos parênteses segue sempre de dentro para fora.
# 2º. **
# 3º. * / // %
# 4º. + -

# Além disso, o intérprete do Python lê os códigos (que contém operações):
# De cima para baixo, da esquerda para a direita.

conta_1 = 1 + 1 ** 5 + 5
conta_2 = (1 + 1) ** (5 + 5)
conta_3 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)
print(conta_2)
print(conta_3)