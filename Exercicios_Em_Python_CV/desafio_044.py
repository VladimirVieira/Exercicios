#Elabora um programa que calcule o vor a ser pago por um produto
#Considere o seu preço normal e a condição de pagamento
#-à vista, tem 10% de desconto
#-à vista no cartão, tem 5% de desconto
#em até duas vezes no cartão, preço normal
#3x no cartão, 20% de juros
print('='*60)
print("{'Lojas Preços - Camaradas':^60}")
print('='*60)
preco_da_compra = float(input('Digite o valor da compra:'))
print('''
Formas de pagamento
[1] Pagamento à vista
[2] à vista no cartão
[3] 2x no cartão 
[4] 3x ou mais no cartão
''')
op = int(input("Qual é a sua opção para pagamento:"))
numero_de_parcelas = int(input("Número de parcelas:"))
if op == 1:
    print('Valor total R${:.2f}, e valor atual com desconto R${:.2f}'.format(preco_da_compra, preco_da_compra*0.9))
elif op == 2:
    print('Valor total R${:.2f}, e valor atual com desconto R${:.2f}'.format(preco_da_compra, preco_da_compra*0.95))
elif op == 3:
    print('Valor total R${:.2f}, e em cada parcela você pagará R${:.2f}'.format(preco_da_compra, preco_da_compra/numero_de_parcelas))
elif op == 4:
    print('Valor total R${:.2f}, e valor atual com crescimo R${:.2f} e o preço em cada parcela R${:.2f}'.format(preco_da_compra, preco_da_compra*1.2, (preco_da_compra*1.2)/numero_de_parcelas))



    