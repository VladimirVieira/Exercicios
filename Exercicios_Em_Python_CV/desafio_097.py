#Faça um programa que tenha uma função
#chamada escreva(), que receba um texto
#qualquer como parâmetro e mostre uma
#mensagem com tamanho adaptável

def escreva(a):
    tam = len(a)
    print("~" * (tam + 4))
    print(f"  {a}  ")
    print("~" * (tam + 4))

escreva('olá mundo')
escreva('Vlad Nascimento')
escreva('Globalização')

