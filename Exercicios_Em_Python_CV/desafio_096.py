#Faça um programa que tenha uma função chamada área(),
#que receba as dimensões de um terreno
#retangular (largura e comprimento) e mostre
#a área do terreno

def area(a, b):

	print(f"A área de um terreno {a} x {b} é de {a*b}m²")

print(f"{'Controle de terrenos'}")
print(f"="*len('Controle de terrenos'))
largura = float(input("Informe a largura do terreno(m):"))
comprimento = float(input("Informe o comprimentdo do terreno(m):"))
area(largura,comprimento)

