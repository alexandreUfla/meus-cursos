"""
Operação ternária (condição de uma linha)
<valor> if <condição> else <outro valor>
"""
condicao1 = 10 == 11 # False
condicao2 = True
variavel1 = 'Valor 1' if condicao1 else 'Outro valor 1'
variavel2 = 'Valor 2' if condicao2 else 'Outro valor 2'
print(variavel1)
print('\n',variavel2)

digito = 9
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print('\n',novo_digito)

print('\nValor' if False else '\nOutro valor' if False else '\nFim')