#Escreva um programa que pergunte a quantidade de km
#percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
#Calcule o preço a pagar sabendo que o carro custa R$ 60,00 por dias
#e R$ 0.15 por km rodado
km_percorrido = float(input('Digite a quantidade de km percorrido:'))
dias_alugado = int(input('Quantidade de dias alugados:'))
pagamento = dias_alugado * 60 + km_percorrido * 0.15
print('Você deve pagar : R${}'.format(pagamento))