#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo proimitivo
#e todas as informações possíveis sobre else
algo = input("Digite algo:")
print("O tipo é:",type(algo))
print("só tem espaços:",algo.isspace())
print("é alfanumerico:",algo.isalnum())
print("é um numero:", algo.isnumeric())
print("é alfabético:",algo.isalpha())
print("a palavra está em maiuscula:",algo.isupper())
print("a plavra está em minuscula:", algo.islower())
print("a palavra está capitalizada:", algo.istitle())