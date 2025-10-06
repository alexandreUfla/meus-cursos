"""
Listas de listas/tuplas e seus índices
vetores dentro de vetores --> matriz
"""
salas = [   #   0       1
            ['Maria','Helena',], # 0
            #   0
            ['Elaine',], # 1
            #   0      1       2    3:0  1   2   3   4
            ['Luiz','João','Eduarda',(0, 10, 20, 30, 40)], # 2
        ]
# Helena
print(salas[0][1])
# Eduarda
print(salas[2][2])
# Elaine
print(salas[1][0])
# 20
print(salas[2][3][2])

salas = [   #   0       1
            ['Maria','Helena',], # 0
            #   0
            ['Elaine',], # 1
            #   0      1       2  
            ['Luiz','João','Eduarda',], # 2
        ]

for i, sala in enumerate(salas):
    print('\nSala: ', i)
    for aluno in sala:
        print('Aluno: ', aluno)