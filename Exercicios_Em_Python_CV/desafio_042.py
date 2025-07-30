#Refaça o exercicio 035, acrescentando o recurso de mostrar que tipo de triângulo será
#formado:
#Equilátero: todos os lados iguais
#Isosceles: dois lados iguais
#Escaleno: Todos os lados diferentes
l1 = float(input('Digite o tamanho do primeiro lado:'))
l2 = float(input('Digite o tamanho do segudo lado:'))
l3 = float(input('Digite o tamanho do terceiro lado:'))

if l1<l2+l3 and l2<l1+l3 and l3<l2+l1:
    if l1 == l2 == l3:
        print('Triangulo equilátero')
    elif (l1 == l2 and l1!=l2) or (l1 == l3 and l1 != l2) and (l2 == l3 and l1!=2):
        print('Triangulo isosceles')
    else:
        print('Triângulo equilátero')