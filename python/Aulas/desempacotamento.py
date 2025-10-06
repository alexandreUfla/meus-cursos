"""
Desempacotamento em chamadas de métodos e funções
"""
string = 'ABCD'
lista = ['Maria','Helena',1,2,3,'Eduarda']
tupla = 'Python','é','legal'
salas = [   #   0       1
            ['Maria','Helena',], # 0
            #   0
            ['Elaine',], # 1
            #   0      1       2  
            ['Luiz','João','Eduarda',], # 2
        ]

#first, x, y, *_, last = lista
#print(first, last, y)

for nome in lista:
    print(nome, end=' ')

print('\n')
print('\n',*lista)
print('\n',*string)
print('\n',*tupla)
print('\n',*salas)
print('\n',*salas, sep='\n')
