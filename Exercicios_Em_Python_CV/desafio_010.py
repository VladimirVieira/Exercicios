#Crie um programa que leia o quanto de dinheiro uma pessoa tem na carteira
#e mostre quantos dolares
valor_na_carteira = float(input('Digite quanto você tem na carteira:'))
dolares = valor_na_carteira/5.5
print('Com R${:.2f} você pode compra U${:.2f}'.format(valor_na_carteira,dolares))