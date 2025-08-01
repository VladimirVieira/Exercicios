#Desenvolva um programa que leia seis
#número inteiros e mostre a soma
#apenas daqueles que forem pares
#Se o valor digitado for impar
#desconsidere-o 

somatorio_dos_pares = 0

for i in range(0,6):
    valor = int(input('Digite um número inteiro:'))
    if valor%2==0:
        somatorio_dos_pares+=valor 
        
print('O somatório de números pares é:{}'.format(somatorio_dos_pares))