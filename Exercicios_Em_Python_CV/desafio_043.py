#Desenvolva uma lógica que leia o peso e altura de uma pessoa
#Calcule o imc e mostre o seu status
#de acordo com a tabela abaixo:
#abaixo de 18.5: abaixo do peso 
#entre 18.5 e 25: peso ideal
#entre 25 e 30: sobrepeso
#entre 30 e 40: obesidade
#acima de 40: obesidade morbida

altura = float(input('Digite a sua altura:'))
peso = float(input('Digite o seu peso:'))

imc = peso/(altura**2)
if imc<18.5:
    print('Abaixo do peso')
elif imc<25:
    print('Peso ideal')
elif imc<30:
    print('Sobrepeso')
elif imc<40:
    print('Obesidade')
else:
    print('obesidade morbida')