#Faça um algoritmo que leia o salario de um funcionário
#e mostre o seu novo salário, com 15% de aumento
salario = float(input('Digite o seu novo salário atual R$:'))
novo_salario = salario*1.1 
print("O seu antigo salário era:R${:.2f}".format(salario))
print("O seu novo salário é:R${:.2f}".format(novo_salario))