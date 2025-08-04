#Crie um programa que leia o nome e o 
#preco de vários produtos. O programa
#deverá perguntar se o usuário vai continuar. No final, mostre:
#a) qual é o total gasto na compra
#b) quantos produtos custam mais de R$ 1000
#c) qual é o nome do produto barato

total_gasto = 0
cont = 0

nome_produto_barato = None
preco_produto_barato = None

while True:
    nome_do_produto = str(input('Digite o nome do produto:')).strip()
    preco_do_produto = float(input('Digite o valor do produto R$'))

    total_gasto += preco_do_produto

    if preco_do_produto >= 1000:
        cont += 1 

    if preco_produto_barato == None:
        nome_produto_barato = nome_do_produto
        preco_produto_barato = preco_do_produto
    elif preco_do_produto < preco_produto_barato:
        nome_produto_barato = nome_do_produto
        preco_produto_barato = preco_do_produto
    op = str(input('Deseja continuar[S/N]:'))
    if op in 'Nn':
        break 
print('='*60)
print('Qual é o total gasto na compra:{}'.format(total_gasto))
print('Quantos produtos custasm mais de R$1000:{}'.format(cont))
print('Qual é o nome do produto mais barato:{}'.format(nome_produto_barato))



     
