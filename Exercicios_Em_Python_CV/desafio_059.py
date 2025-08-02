valor1 = int(input('Digite o primeiro valor:'))
valor2 = int(input('Digite o segundo valor:'))
op = -1
while op!=5:
    print('='*50)
    print('''
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa

        ''')
    print('='*50)
    op = int(input('Escolha a sua opção:'))
    
    if op == 1:
        print('{} + {} = {}'.format(valor1, valor2, valor1+valor2))
    elif op == 2:
        print('{} * {} = {}'.format(valor1, valor2, valor1*valor2))
    elif op == 3:
        if valor1 > valor2:
            print('{} > {}'.format(valor1, valor2))
        else:
            print('{} > {}'.format(valor2, valor1))
    elif op == 4:
        valor1 = int(input('Digite o primeiro numero:'))
        valor2 = int(input('Digite o segundo numero:'))
    
    


