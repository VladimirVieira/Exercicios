#Escreva um programa que pergunte o salárop de um funcionário
#e calcule o valor do seu aumento
#Para valores superiores a R$ 1250, calcule um aumento de 10%
#Para valores inferiores um aumento de 15%

salario_atual = float(input('Digite o valor do salario em R$:'))

if salario_atual>1250:
    salario_atual*=1.1 
else:
    salario_atual*=1.15 
    
print('O seu novo salario é:R${:.2f}'.format(salario_atual))