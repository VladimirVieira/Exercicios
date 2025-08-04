#Crie um programa que simule o funcionamento de um
#caixa eletrônico. No inicio, pergunte ao usuário
#qual será o valor a ser sacado (número inteiro)
#e o programa vai informar quant cédulas de cada
#valor serão entregues


cem = 0
cinquenta = 0
vinte = 0
dez = 0 
cinco = 0
dois = 0
um = 0

valor_sacado = float(input('Digite o valor a ser sacado:R$'))

while valor_sacado > 0:
    if valor_sacado > 99:
        cem += 1
        valor_sacado -= 100
    elif valor_sacado > 49:
        cinquenta += 1
        valor_sacado -= 50
    elif valor_sacado > 19:
        vinte += 1
        valor_sacado -= 20
    elif valor_sacado > 9:
        dez += 1
        valor_sacado -= 10
    elif valor_sacado > 4:
        cinco += 1
        valor_sacado -= 5
    elif valor_sacado > 1:
        dois += 1
        valor_sacado -= 2
    elif valor_sacado > 0:
        um += 1
        valor_sacado -= 1


if cem > 0:
    print(f'Você obteve {cem} cédulas de R$100')
if cinquenta > 0:
    print(f'Você obteve {cinquenta} cédulas de R$50')
if vinte > 0:
    print(f'Você obteve {vinte} cédulas de R$20')
if dez > 0:
    print(f'Você obteve {dez} cédulas de R$10')
if cinco > 0:
    print(f'Você obteve {cinco} cédulas de R$5')
if dois > 0:
    print(f'Você obteve {dois} cédulas de R$2')
if um > 0:
    print(f'Você obteve {um} cédulas de R$1')
