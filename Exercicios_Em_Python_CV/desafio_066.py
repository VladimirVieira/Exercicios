#Crie um programa que leia vários números inteiros pelo teclado
#O programa só vai parar quando o usuário digitar o valor 999, que é a 
#condição de parada. No final, mostre quantos números foram digitados
#e qual foi a soma entre eles (desconsidere o flag)

n = -1
somatorio = 0
cont = 0
while n!= 999:
    n = int(input('Digite um valor inteiro(999 é a condição de parada):'))
    if n != 999 :    
        somatorio += n
        cont += 1

print('O somatorio é igual a:{}'.format(somatorio))
print('\033[1;33;44m O total de numeros somados foi:{}\033[m'.format(cont))
    
    
    
