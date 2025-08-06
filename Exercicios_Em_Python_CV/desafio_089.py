#Crie um programa que leia nome e duas notas de vários alunos
#e guarde tudo em uma lista composta. No final, mostre um boletim
#contendo a média de cada um e permita que o usuário
#possa mostrar as notas de cada aluno individualmente

lista_dos_alunos = []

while True:
	nome = str(input("Digite o nome do aluno:"))
	nota1 = float(input("Digite a primeira nota:"))
	nota2 = float(input("Digite a segunda nota:"))
	
	lista_aux = [nome, nota1, nota2, (nota1+nota2)/2]
	lista_dos_alunos.append(lista_aux[:])
	
	op = str(input("Cadastrar aluno[S/N]:")).strip()[0]
	if op in "Nn":
		break
	lista_aux.clear()
print("="*60)
print(f"{'Boletim':^60}")
print("="*60)
for i, j in enumerate(lista_dos_alunos):
	print(f"{i:>2} {j[0]:.<10} {j[3]:.>40.2f}")
	
print("="*60)
while True:
	op = str(input("Verificar nota de algum aluno:"))
	if op in "Nn":
		break
	aluno = int(input("Use o identificador do aluno para verificar notas:"))
	print(f"{lista_dos_alunos[aluno][1]} {lista_dos_alunos[aluno][2]}")	
	
