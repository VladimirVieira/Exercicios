#Crie um programa que tenha uma tupla com várias palavras
#(não usar acentos). Depois disso, você deve mostrar, para 
#cada palavra, quais são as suas vogais

tupla_aurelio = ("Andar",
		 "Correr",
		 "Patinar",
		 "Andarilho",
		 "Corredor",
		 "Saltitante",
		 "Medieval",
		 "Biografia",
		 "Armadilha")
		 
for i in tupla_aurelio:
	print(f"Na palavra \033[1;33;44m{i.lower()}\033[m temos as seguintes vogais:")																									
	for j in i.lower():
		if j in 'aeiou':
			print(j, end = " ")
			
	print("")
		 
