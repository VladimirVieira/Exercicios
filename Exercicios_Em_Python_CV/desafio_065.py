#Crie um programa que leia vários números inteiros pelo teclado
#No final da execução, mostre a média entre todos os valores e qual
#foi o maior e o menor valores lidos. O programa deve perguntar ao usuário
#se ele quer ou não continuar a digitar valores

somatorio = 0
cont = 0
op = '-'
maior_valor = None
menor_valor = None
while op not in 'Nn':
    num = int(input('Digite um número inteiro:'))
    somatorio += num
    op = str(input('Deseja continuar[S/N]:')).strip()
    cont += 1

    if maior_valor == None:
        maior_valor = num
    elif maior_valor < num:
        maior_valor = num

    if menor_valor == None:
        menor_valor = num
    elif menor_valor > num:
        menor_valor = num

print('A média dos valores lidos:{}'.format(somatorio/cont))
print('O maior valor lido foi:{}'.format(maior_valor))
print('O menor valor lido foi:{}'.format(menor_valor))



