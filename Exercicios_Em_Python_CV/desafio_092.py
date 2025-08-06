#Crie um programa que leia ome, ano de nascimento e carteira de trabalho
#e cadastre-os (com idade) em um dicionario se por acaso
#a ctps for diferente de zero, o dicionario receberá
#também o ano de contratação e o salário. Calcule e acrescente
#além da idade, com quantos anos a pessoa vai se aposentar

from datetime import date

cadastro_trabalhador = dict()

cadastro_trabalhador['nome'] =  str(input("Informe o nome do trabalhador:"))
cadastro_trabalhador['idade'] = int(input("Informe o ano de nascimento:"))
cadastro_trabalhador['ctps'] = int(input('Informe a carteira de trabalho(0 não tem)'))

if cadastro_trabalhador['ctps'] != 0:
	cadastro_trabalhador['contratacao'] = int(input('Digite o ano de contratação:'))
	cadastro_trabalhador['salario'] = float(input('Digite o valor do salário em R$:'))
	cadastro_trabalhador['aposentadoria'] = cadastro_trabalhador['contratacao'] - cadastro_trabalhador['idade'] + 30
	
	cadastro_trabalhador['idade'] = date.today().year - cadastro_trabalhador['idade']
	
print("="*60)

for i, j in cadastro_trabalhador.items():
	print(f"{i} tem o valor {j}")
