#Faça um programa que leia nome e média de 
#um aluno, guardando também a situação
#em um dicionário. No final, mostre o conteúdo da estrutura 
#na tela

cadastro_aluno = dict()

cadastro_aluno['Nome'] = str(input("Digite o nome do aluno:"))
cadastro_aluno['Média'] = float(input("Digite a média:"))

if cadastro_aluno['Média'] > 6:
	cadastro_aluno['Situacao'] = "Aprovado"
elif cadastro_aluno['Média'] > 4:
	cadastro_aluno['Situacao'] = "Recuperação"
else:
	cadastro_aluno['Situacao'] = "Reprovado"
	
for i, j in cadastro_aluno.items():
	print(f"{i}: {j}")
