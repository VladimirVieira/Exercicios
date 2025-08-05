#Desenvolva um programa que 
#leia quatro alores pelo teclado e 
#guarde-os em uma tupla. No final, mostre:
#a)Quantas veezes apareceu o valor 9
#b)Em que posição foi digitado o primeiro valor 3
#c)Quais foram os números pares

n1 = int(input("Digite o primeiro valor:"))
n2 = int(input("Digite o segundo valor:"))
n3 = int(input("Digite o terceiro valor:"))
n4 = int(input("Digite o quarto valor:"))

valores = (n1, n2, n3, n4)
print(f"Número de vezes que o 9 apareceu:{valores.count(9)}")
print(f"Em que posição foi digitado o primeiro 3:{valores.index(3)}")
print(f"Número pares:")
for i in valores:
	if i % 2 == 0:
		print(i, end = " ")
		
print("")
