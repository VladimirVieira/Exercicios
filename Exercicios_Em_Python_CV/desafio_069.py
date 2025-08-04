#Crie um programa que leia a idade e o sexo
#de várias pessoas. A cada pessoa cadastrada, o programa
#deverá perguntar se o usuário quer ou 
#não continuar. No final mostre:
#a)quantas pessoas tem mais de 18 anos
#b)quantos homens foram cadastrados
#c)quantas mulheres tem menos de 20 anos

maior_idade = 0
quant_de_homens = 0
quant_mulheres_20 = 0
while True:
    idade = int(input('Digite a idade de uma pessoa:'))
    sexo = str(input('Informe o sexo da pessoa[M/F]:')).strip()[0]

    if idade >= 18:
        maior_idade += 1

    if sexo in 'Mm':
        quant_de_homens += 1

    if sexo in 'Ff':
        quant_mulheres_20 += 1

    op = str(input('Deseja continuar[S/N]:')).strip()
    if op in 'Nn':
        break

print('Quantidade de pessoas com idade maior que 18:{}'.format(maior_idade))
print('Quantidade de homens:{}'.format(quant_de_homens))
print('Quantidade de mulheres:{}'.format(quant_mulheres_20))

    
        
