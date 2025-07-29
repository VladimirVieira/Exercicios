#Crie um programa que leia o nome de uma pessoa
#E diga se ela tem 'Silva' no nome
nome_completo = input('Digite o seu nome completo:').strip().upper()
print('Existe Silva no nome:{}'.format('SILVA' in nome_completo))
