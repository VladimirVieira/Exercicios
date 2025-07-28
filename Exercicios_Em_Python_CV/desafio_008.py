#Escreva um programa que leia um valor em metros e o exiba convertido
#em centimetros e milímetros
metros = float(input('Digite o total de metros a ser convertido:'))
print('Total em metros:{:.2f}m'.format(metros))
print('Total em centímetros:{:.2f}cm'.format(metros*100))
print('Total em milímetros:{:.2f}mm'.format(metros*1000))