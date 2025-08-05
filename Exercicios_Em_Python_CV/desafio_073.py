#Crie uma tupla preenchida com os 20
#primeiros colocados da tabela do
#Campeonato Brasileiro de Futebol
#na ordem de colocação. Depois mostre:
#a) Os 5 primeiros
#b) Os últimos 4 colocados
#c) Times em ordem alfabética
#d) Em que posição está o time da Chapecoense

times = ("Atlético - MG",
	 "Flamengo",
	 "Palmeiras",
	 "Fortaleza",
	 "Corinthians",
	 "Bragantino",
	 "Fluminense",
	 "América-MG",
	 "Atlético-GO",
	 "Santos",
	 "Ceará SC",
	 "Internacional"
	 "São Paulo",
	 "Athletico-PR",
	 "Cuiabá",
	 "Juventude",
	 "Grêmio",
	 "Bahia",
	 "Sport Recife",
	 "Chapecoense")
	 
print(f"Os cinco primeiro colocados são:{times[:5]}")
print("="*60)
print(f"Os quatro últimos colocados são:{times[-4:]}")
print("="*60)
print(f"Times em ordem alfabética:{sorted(times)}")
print("="*60)
print(f"Posição do time da chapecoense:{times.index('Chapecoense')+1}")
	 
