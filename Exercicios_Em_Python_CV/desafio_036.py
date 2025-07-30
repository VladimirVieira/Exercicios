#Escreva um programa para aprovar o empréstimo bancário para a 
#Compra de uma casa. Pergunte o valor da casa, o salário do comprador
#E em quantos anos ele vai pagar
#A prestação mensal não pode exceder 30% do sala
#caso ocorra o emprestimo será negado
salario = float(input('Digite o valor de seu salário:R$'))
valor_da_casa = float(input('Digite o valor da casa:'))
anos_de_pagamento = float(input('Digite a quantidade de anos a ser paga a casa:'))

quantidade_de_meses = anos_de_pagamento*12
parcela_da_casa = valor_da_casa/quantidade_de_meses

print(verifica)
if parcela_da_casa > salario*0.3:
    print('A parcela da casa é R${:.2f} e o seu salário é R${:.2f}, logo o emprestimo foi negado.'.format(parcela_da_casa, salario))
else:
    print('Emprestimo aprovado! valor da parcela R${:.2f} e do salário R${:.2f}'.format(parcela_da_casa, salario))
