#Escreva um programa que converta uma temperatura digitada temperatura
#em °C e converta para °F
temperatura_C = float(input('Digite a temperatura atual:'))
conversor_F = (9*temperatura_C+160)/5
print("temperatura em °C:{}",temperatura_C)
print("Temperatura em °F:{}",conversor_F)