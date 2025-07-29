#Faça um programa que leia uma frase pelo teclado
#e mostre:
#Quantas vezes aparece a letra "a"
#Em que posição ela aparece pela primeira vezes
#Em que posição ela aparece pela última vez 

frase = str(input('Digite uma frase:')).strip()
quantidade_de_vezes = frase.count('a')
primeira_ocorrencia = frase.find('a')
ultima_ocorrencia = frase.rfind('a')
print('Total de vezes em que a aparece:{}'.format(quantidade_de_vezes))
print('Primeira ocorrência:{}'.format(primeira_ocorrencia))
print('Ultima ocorrência:{}'.format(ultima_ocorrencia))