"""
Exercício do Curso: Python 3+ completo
PLataforma de cursos: Udemy
Autor: Alexandre R. F. Júnior

Faça uma lista de compras com listas. O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista. Não permita que o programa quebre com erros de índices inexistentes na lista.
"""
loop = True
lista = []

while loop:
    print('=============================================================================')
    print('                                     Opções                                  ')
    print('=============================================================================')
    print(f"[0]Listar\t[1]Inserir\t[2]Apagar\t[3]Editar Item\t[4]Sair")
    print('=============================================================================')
    op = int(input('Digite o número referente a opção desejada: '))

    match op:
        case 0:
            print('=============================================================================')
            print('                                     Lista                                   ')
            print('=============================================================================')
            print(f"Total de itens: {len(lista)}\n")
            print(f"\t--------------------------------")
            print(f"\tÍndice \tNome")
            print(f"\t--------------------------------")
            for item in enumerate(lista):
                indice, nome = item
                print(f"\t{indice+1} \t{nome}")
            print(f"\t--------------------------------")
            exit
        case 1:
            while True:
                item = str(input('Digite o item (0 para parar): '))
                if item == '0':
                    print('Lista salva com sucesso!')
                    break
                lista.append(item)
            print('Lista salva com sucesso!\n')
            print('=============================================================================')
            print('                                     Lista                                   ')
            print('=============================================================================')
            print(f"Total de itens: {len(lista)}\n")
            print(f"\t--------------------------------")
            print(f"\tÍndice \tNome")
            print(f"\t--------------------------------")
            for item in enumerate(lista):
                indice, nome = item
                print(f"\t{indice+1} \t{nome}")
            print(f"\t--------------------------------")
            exit
        case 2:
            x = int(input('Insira o índice do item a ser excluído da lista: '))
            try:
                lista.remove(lista[x-1])
                print('Item apagado com sucesso!\n')
                print('=============================================================================')
                print('                                     Lista                                   ')
                print('=============================================================================')
                print(f"Total de itens: {len(lista)}\n")
                print(f"\t--------------------------------")
                print(f"\tÍndice \tNome")
                print(f"\t--------------------------------")
                for item in enumerate(lista):
                    indice, nome = item
                    print(f"\t{indice+1} \t{nome}")
                print(f"\t--------------------------------")
                exit
            except TypeError:
                print('Por favor, digite um número inteiro')
                exit
            except ValueError:
                print('Por favor, digite um número inteiro')
                exit
            except IndexError:
                print('O item selecionado não existe na lista')
                exit
            except Exception:
                print('Erro desconhecido')
                exit
        case 3:
            x = int(input('Insira o índice do item a ser editado: '))
            try:
                lista[x-1] = str(input('Novo nome: '))
                print('Item editado com sucesso!\n')
                print('=============================================================================')
                print('                                     Lista                                   ')
                print('=============================================================================')
                print(f"Total de itens: {len(lista)}\n")
                print(f"\t--------------------------------")
                print(f"\tÍndice \tNome")
                print(f"\t--------------------------------")
                for item in enumerate(lista):
                    indice, nome = item
                    print(f"\t{indice+1} \t{nome}")
                print(f"\t--------------------------------")
                exit
            except TypeError:
                print('Por favor, digite um número inteiro')
                exit
            except ValueError:
                print('Por favor, digite um número inteiro')
                exit
            except IndexError:
                print('O item selecionado não existe na lista')
                exit
            except Exception:
                print('Erro desconhecido')
                exit
            exit
        case 4:
            break
    
    print('=============================================================================')
    print('                                     Opções                                  ')
    print('=============================================================================')
    print(f"\t\t[0]Menu incial \t\t\t[1]Sair")
    print('=============================================================================')
    op2 = int(input('O que deseja?: '))

    if op2 == 0: loop = True
    elif op2 == 1:
        break