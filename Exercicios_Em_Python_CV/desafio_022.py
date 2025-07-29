#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas e minúsculas
#Quantas letras ao todo(sem considerar os espaços)
#Quantas letras tem o primeiro nome
nome = str(input('Digite o nome completo:'))
print('O nome formado apenas por letras maiusculas:{}'.format(nome.upper()))
print('O nome formado apenas por letras minusculas:{}'.format(nome.lower()))
print('O total de letras no nome é:{}'.format(len(nome)-nome.count(" ")))
print('Quantas letras tem o primeiro nome:{} ou {}'.format(len(nome.split()[0]), nome.find(" ")))
