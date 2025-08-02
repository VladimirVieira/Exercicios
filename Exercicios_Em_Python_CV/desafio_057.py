#Faça um programa que leia o sexo de uma 
#pessoa, mas só aceite os valores 'M' ou 'F'
#Caso esteja errado, peça digitação novamente
#até ter um valor correto 

op = 'sexo'

while op not in 'MF':
    op = str(input('informe o seu sexo:'))
    
print('Fim')
