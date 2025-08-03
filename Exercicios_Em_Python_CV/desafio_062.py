#melhore o desafio 061 perguntando
#para o usuário se ele quer mostrar
#mais alguns termos. O programa encerra quando ele disser
#que quer mostrar 0 termos

quantidade_de_termos = 10
primeiro_termo = int(input('Informe o valor do primeiro termo:'))
razao = int(input('Informe a razão:'))
cont = 0

while quantidade_de_termos != 0:

    while quantidade_de_termos != 0:
        print(primeiro_termo, end = ' ')
        primeiro_termo += razao
        quantidade_de_termos-=1
        cont+=1

    quantidade_de_termos = int(input('Informe a quantidade de novos termos que deseja receber:'))

print('o total de termo da PA foi:{}'.format(cont))
