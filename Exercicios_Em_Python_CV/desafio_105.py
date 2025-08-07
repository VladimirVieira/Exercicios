#Faça um programa que tenha uma função
#notas() que pode receber várias notas
#de alunos e vai retornar um dicionario com
#as seguintes informações:
#- Quantidade de notas:
#- A maior nota
#- A menor nota
#- A média da turma
#- A situação (opcional)
#Adicione também as docstrings

def notas(*num, sit = False):
	dicionario = dict()
	
	dicionario['Quantidade de notas'] = len(num)
	maior = None
	menor = None
	media = 0
	cont = 0
	for i in num:
		cont += 1
		media += i
		if maior == None and menor == None:
			maior = i
			menor = i
		if maior < i:
			maior = i
			
		if menor > i:
			menor = i
			
	dicionario['Maior Nota'] = maior
	dicionario['Menor Nota'] = menor
	dicionario['Media'] = media/cont
	if sit:
		if dicionario['Media'] > 6:
			dicionario['Sit'] = 'Aprovado'
		elif dicionario['Media'] > 4:
			dicionario['Sit'] = 'Recuperação'
		else:
			dicionario['Sit'] = 'Reprovado'
	return dicionario		
	
print(notas(5,6,7,8, sit = True))
