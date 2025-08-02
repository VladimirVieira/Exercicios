#Crie um programa que leia 
#uma frase qualquer e diga 
#se ela é um palíndromo 
#desconsiderando os espaços 
#Ex: a sacada da casa
#após a sopa 
#a torre da derrota 
#o lobo ama o bolo 
#anotaram a data da maratona

frase = str(input('Digite uma frase para ser analisada:')).strip().split()
frase = ''.join(frase)
if frase == frase[::-1]:
    print('é palindromo')
else:
    print('não é palindromo')