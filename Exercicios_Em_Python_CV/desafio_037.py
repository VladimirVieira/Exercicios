#Escreva um programa que leia um número inteiro qualquer e peça
#para o usuário escolher qual vai ser a base de conversão
print('='*60)
print("{'Tabela de conversao:^60'}")
print('='*60)
print('''
[1] binário
[2] octal
[3] hexadecimal
''')
print('='*60)
op = int(input('Digite a opção escolhida:'))
valor = int(input('Digite um valor inteiro a ser convertido:'))
if op == 1:
    print('{}'.format(bin(valor)))
elif op == 2:
    print('{}'.format(oct(valor)))
elif op == 3:
    print('{}'.format(hex(valor)))

    
