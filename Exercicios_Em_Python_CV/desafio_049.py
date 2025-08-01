#Refaça o exercicio 009, mostrando a tabuada
#de um número que o usuário escolher,
#só que agora utilizando um laço for 

tabuada = int(input('Digite um número para obter a sua tabuada [0-10]:'))

print('='*60)
print("{:^60}".format('Tabuada'))
print('='*60)
for i in range(0,11,1):
    print('{:>2} x {:>2} = {:>3}'.format(i,tabuada,tabuada*i))
    

    