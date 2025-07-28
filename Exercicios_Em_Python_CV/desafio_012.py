#Faça um algoritmo que leia o preço de um produto
#e mostre seu novo preço, com %5 de desconto
preco_do_produto = float(input('Digite o preço do produto:'))
novo_preco = preco_do_produto * 0.95
print('O produto tem preco incial R${:.2f} e agora com desconto de %5 tera o valor de R${:.2f}'.format(preco_do_produto,novo_preco))