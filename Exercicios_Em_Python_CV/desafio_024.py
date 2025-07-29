#Crie um programa e leia o nome de uma cidade
#e diga se ela começa ou não com o nome 'santo'
nome_da_cidade = str(input('Digite o nome da cidade que você nasceu:')).strip().split()
print('A cidade começa com o nome SANTO:{}'.format(nome_da_cidade[0].upper()=='SANTO'))