#Crie um programa que tenha uma tupla totalmente preenchida
#com uma contagem por extenso, de zero até vinte
#Seu programa deverá ler um número pelo teclado (entre 0 a 20)
#e amostrá-la por extenso

numero = ("zero",
	  "um",
	  "dois",
	  "tres",
	  "quatro",
	  "cinco",
	  "seis",
	  "sete",
	  "oito",
	  "nove",
	  "dez",
	  "onze",
	  "doze",
	  "treze",
	  "quatorze",
	  "quinze",
	  "dezesseis",
	  "dezessete",
	  "dezoito",
	  "dezenove",
	  "vinte")

while True:
	num = int(input("Digite um número inteiro [0-20]:"))
	if 0 <= num <= 20:
		print(f"O número escrito por extenso é: {numero[num]}")
		break
