#Faça um programa que calcule a soma
#entre todos os números impares
#que são múltiplos de três
#e que se encontram no intervalo
#de 1 a 500
somatorio = 0
for i in range(1,501,1):
    if i%2!=0 and i%3==0:
        somatorio += i
print('o somatório dos números impares é:{}' .format(somatorio))