# Projeto: Calculadora
# Autor: Alexandre Reis Francisco Júnior
# Primeiro projeto em python. Calculadora simples.

import math

print('---------------------------------------------------------------------------')
print('                                CALCULADORA                                ')
print('---------------------------------------------------------------------------')
print('Bem vindo à calculadora simples! Aqui você pode realizar operações simples')
print('como adição, subtração, multiplicação, divisão, potência e raiz quadrada.')
print('Vamos Começar?')

continuar_loop = True
while continuar_loop:

    print('---------------------------------------------------------------------------')
    print('                                   Funções                                 ')
    print('---------------------------------------------------------------------------')
    print(f"\t0 - Sair da calculadora")
    print(f"\t1 - Calculadora")
    print('---------------------------------------------------------------------------')
    func = int(input('Escolha a opção desejada: '))

    match func:
        case 0:
            continuar_loop = False
            break
            exit
        case 1:
            print('---------------------------------------------------------------------------')
            print('                              Manual do Usuário                            ')
            print('---------------------------------------------------------------------------')
            print('Para executar a operação citada da primeira coluna, digite o símbolo')
            print('indicado na segunda coluna quando a operação desejada for solicitada.')
            print('\n')
            print(f"\tSoma \t\t\t\t+")
            print(f"\tSubtração \t\t\t-")
            print(f"\tMultiplicação \t\t\t*, x ou X")
            print(f"\tDivisão \t\t\t/")
            print(f"\tPotência \t\t\t^ ou **")
            print(f"\tRaiz Quadrada \t\t\traiz ou sqrt")
            print('\n')
            print('---------------------------------------------------------------------------')
            x1 = float(input('Insira o primeiro operando: ')) 
            op = str(input('Operação desejada: '))

            match op:
                case 'raiz':
                    y = math.sqrt(x1)
                    print('Resposta: ', y)
                    exit
                case 'sqrt':
                    y = math.sqrt(x1)
                    print('Resposta: ', y)
                    exit
                case _:
                    x2 = float(input('Insira o segundo operando: '))
                    print('---------------------------------------------------------------------------')
                    if op == '+':
                        y = x1+x2
                    elif op == '-':
                        y = x1-x2
                    elif op == '*' or op == 'x' or op == 'X':
                        y = x1*x2
                    elif op == '/':
                        y = x1/x2
                    elif op == '^' or op == '**':
                        y = pow(x1,x2)

                    print('RESULTADO: ', y)
                    exit

            x1 = None
            x2 = None
            y = None
            exit
    exit


