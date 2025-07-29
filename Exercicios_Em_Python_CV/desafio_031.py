#Desenvolva um programa que pergunte a distancia de uma viagem
#em Km. Calcule o preço da passagem, cobrando R$ 0.5 por km para viagens de até 
#200km e R$ 0.45 para viagens mais longas

distancia_percorrida = float(input('Distacia percorrida:'))
valor_pago = 0
if distancia_percorrida<=200:
    valor_pago = distancia_percorrida * 0.5 
else:
    valor_pago = distancia_percorrida * 0.45

print('O gasto total com a viagem foi:R${:.2f}'.format(valor_pago))
