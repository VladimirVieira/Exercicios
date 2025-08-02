#Faça um programa que leia um número
#qualquer e mostre o seu fatorial

fatorial = int(input('Digite um númeroooo para calcular o fatorial:'))
produtorio = 1
while fatorial > 0:
    
    if fatorial > 1:
        produtorio *= fatorial
        print(fatorial, end = ' * ')
    elif fatorial == 1:
        print(fatorial, end = ' = ')
    
    fatorial -= 1

print(produtorio)        
