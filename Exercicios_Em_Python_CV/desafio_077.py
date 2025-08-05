#Crie um programa que tenha uma tupla única com nomes de
#produto e seus respectivos preços, na sequencia. No final,
#mostre uma listagem de preços, organizando os dados em
#forma tabular

listagem = ("Listagem", 1.75,
	    "Borracha", 2,
	    "Caderno", 15.90,
	    "Estojo", 25,
	    "Transferidor", 4.20,
	    "Compasso", 9.99,
	    "Mochila", 120.32,
	    "Canetas", 22.30,
	    "Livro", 34.90
)

print("="*70)
print(f"{'Material Escolar':^70}")
print("="*70)

for i,j in enumerate(listagem):
	
	if i%2 == 0:
		print(f'{j:.<50}', end = " ")
	else:
		print(f'R${j:.2f}')


