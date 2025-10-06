"""
Imprecisão de ponto flutuante
"""
import decimal

# O tipo float não é muito preciso devido a forma que é salvo na memória, logo pode ocorrer erros de aproximação
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print('Sem biblioteca decimal')
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))

# A biblioteca decimal importada no início do código corrige esse problema
numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print('\nCom biblioteca decimal')
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 3))

# É interessante usar essa biblioteca para projetos que seja necessária visulizar e utilizar o máximo de casa decimais possíveis