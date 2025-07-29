#Faça um programa que leia o nome completo de uma pessoa
#mostrando em seguida o primeiro e o último nome separadamente
#Exemplo:Ana Maria de Souza
#Primeiro = Ana
#Último = Souza
nome_completo = str(input('Digite o seu nome completo:')).strip().split()
primeiro = nome_completo[0]
ultimo = nome_completo[len(nome_completo)-1]
print('O seu primeiro nome é:{}'.format(primeiro))
print('O seu último nome é:{}'.format(ultimo))
