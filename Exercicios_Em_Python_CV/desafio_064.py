#Crie um programa que leia vários númros inteiros pelo teclado
#O programa só vai parar quando o usuário digitar o valor 999, que
#é a condição de parada. No final, mostre quantos números inteiros foram
#Digitados e qual foi a soma entre eles (desconsidere a flag)

n = -1
total = 0
cont = 0
while n != 999:
    n = int(input('Digite um valor inteiro para obter o somatorio:'))
    if n != 999:
        total += n
        cont += 1

print('O somatorio resultante é:{}'.format(total))
print('A quantidade de números adicionados:{}'.format(cont))

