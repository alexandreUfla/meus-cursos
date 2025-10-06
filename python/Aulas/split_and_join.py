"""
split e join com list e str
split - divide uma string
join - une uma string
"""
# Split
frase = '   Olha só que    , coisa interessante          '
lista_palavras = frase.split()
print(lista_palavras)

lista_frases = frase.split(',')
print(lista_frases)

print('\n')
for i, frase in enumerate(lista_frases):
    print(lista_frases[i])

# strip() remove os espaços de antes e depois da frase ou palavra
print('\n')
for i, frase in enumerate(lista_frases):
    print(lista_frases[i].strip())

# rstrip() remove os espaços da direita
print('\n')
for i, frase in enumerate(lista_frases):
    print(lista_frases[i].rstrip())

# lstrip() remove os espaços da esquerda
print('\n')
for i, frase in enumerate(lista_frases):
    print(lista_frases[i].lstrip())

print('\n')
for i, frase in enumerate(lista_frases):
    lista_frases[i] = lista_frases[i].strip()
print(lista_frases)

frase = '   Olha só que    , coisa interessante          '
lista_frases_cruas = frase.split(',')
lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print('\n')
print(lista_frases_cruas)
print(lista_frases)

# Join
frases_unidas = ' '.join(lista_frases) # 'caracter usado entre os itens "x"'.join(x)
print('\n')
print(frases_unidas)