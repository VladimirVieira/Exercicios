entrada1 = str(input()).split()
entrada2 = str(input()).split()

valor1 = float(entrada1[1]) * float(entrada1[2])
valor2 = float(entrada2[1]) * float(entrada2[2])

valor = valor1 + valor2

print(f"VALOR A PAGAR: R$ {valor:.2f}")
