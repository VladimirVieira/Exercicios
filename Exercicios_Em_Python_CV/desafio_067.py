#Faça um programa que mostre a tabuada de vários números, um de
#cada vez, para cada valor digitado pelo usuário. O programa será
#interrompido quando o número solicitado for negativo

while True:
    tabuada = int(input('Digite um número intero cujo você necessita obter a tabuada:'))
    if tabuada < 0:
        break
    print("="*60)
    for i in range(1,11):
        print(f'{i:>2} x {tabuada:>2} = {tabuada * i:>2}')
    print("="*60)
