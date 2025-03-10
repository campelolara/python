num = int(input("Digite um número:"))
lista = []

while num >= 0:
    lista.append(num)
    num -= 1

print(f"A contagem regressiva dos números é: {lista}")