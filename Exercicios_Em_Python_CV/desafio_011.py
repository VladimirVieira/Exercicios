#Faça um programa que leia a largura e altura de uma parede em metros
#calcule a sua área e quantidade de tinta necessária para pintá-la
#sabendo que cada litro de tinta pinta uma área de 2m²
largura = float(input("Digite a largura da parede em m:"))
altura = float(input("Digite a altura da parede em m:"))
area = largura * altura 
litros_de_tinta =area/2
print("Com a largura de {} m e a altura de {} m, temos uma área de {}m²".format(largura, altura, area))
print("logo precisamos de {}l de tinta".format(litros_de_tinta))