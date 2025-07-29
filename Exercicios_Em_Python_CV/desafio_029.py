#Escreva um programa que leia a velocidade de um carro
#se ele ultrapassar 80km/h, mostre uma mensagem
#dizendo que ele foi multado
#A multa vai custar R$7.00 par cada km acima do do limite
velocidade_do_carro = float(input('Digite a velocidade do carro:'))
if velocidade_do_carro<=80:
    print('Parabéns, você dirige com segurança!')
else:
    multa = velocidade_do_carro - 80 
    multa *= 7 
    print("Multa a ser paga por dirigir acimada do limite permitido:R${:.2f}".format(multa))