#Faça um programa que leia três números e mostre
#Qual é o maior e qual é o menor
num1 = int(input('Digite o valor do primeiro número:'))
num2 = int(input('Digite o valor do segundo número:'))
num3 = int(input('Digite o valor do terceiro número:'))
maior = None
menor = None 
if num1>num2>num3:
    maior = num1
elif num1>num3>num2:
    maior = num1
elif num2>num1>num3:
    maior = num2
elif num2>num3>num1:
    maior = num2
elif num3>num1>num2:
    maior=num3
elif num3>num2>num1:
    maior=num3
    
if num1<num2<num3:
    menor = num1
elif num1<num3<num2:
    menor = num1
elif num2<num1<num3:
    menor = num2
elif num2<num3<num1:
    menor = num2
elif num3<num1<num2:
    menor=num3
elif num3<num2<num1:
    menor=num3
    
print('O maior numero é:{}'.format(maior))
print('O menor numero é:{}'.format(menor))