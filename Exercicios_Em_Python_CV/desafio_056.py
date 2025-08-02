#Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas
#No final do programa mostre:
#A média de idade do grupo  
#Qual é o nome do homem mais velho 
#Quantas mulheres tem menos de 20 anos 
media_de_idade = 0
homem_mais_velho = 0
cont_num_mulheres = 0
for i in range(4):
    nome = str(input('Digite o nome de uma pessoa:'))
    idade = int(input('Digite a idade da pessoa:'))
    sexo = str(input('Digite o sexo de uma pessoa [M/F]:'))
    
    media_de_idade += idade
    
    if i == 0 and sexo == 'M':
        homem_mais_velho = idade
    elif idade > homem_mais_velho and sexo == 'M':
        homem_mais_velho = idade 
        
    if sexo == 'F' and idade < 20:
        cont_num_mulheres += 1
        
print('A média de idade do grupo é: {}'.format(media_de_idade/4))
print('A idade do homem mais velho: {}'.format(homem_mais_velho))
print('Quantas mulheres tem menos de 20 anos: {}'.format(cont_num_mulheres))