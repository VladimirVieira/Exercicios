#Faça um programa que leia o peso de cinco pessoas
#No final, mostre qual foi o maior e o menor peso lidos
menor = 0
maior = 0
for i in range(5):
    peso = float(input('Digite o valor do peso de uma pessoa:'))
    
    if i == 0:
        menor = peso 
        maior = peso 
    else:
        if peso > maior:
            maior = peso 
        
        if peso < menor:
            menor = peso 
            
print('O maior peso lido é:{}'.format(maior))
print('O menor peso lido é:{}'.format(menor))
    























