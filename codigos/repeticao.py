#Maior e menor valor
contador = 1
while contador <= 3:
    num = int(input("Digite um numero: "))
    lista = [num]
    contador += 1

maior_elemento = max(lista)
menor_elemento = min(lista)
print(f"O maior elemento é: {maior_elemento}")
print(f"O menor elemento é: {menor_elemento}")

##switch case