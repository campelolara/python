"""
#ex001
numeros = [10, 20, 30, 40, 50]
numerosDobro = []
for item in numeros:
    numerosDobro.append(item * 2)

print("==================Saída====================")
print(f"Lista: {numeros}")
print(f"Lista com valores dobrados: {numerosDobro}")
print("===========================================")


#ex002
listaSupermercado = ["Arroz", "Farinha", "Açúcar", "Maionese", "Ketchup", "Laranja", "Maçã", "Uva", "Carne", "Pão"]
print("==============Lista de Compras==============")
for produto in listaSupermercado:
    print(f"Produto: {produto}")

"""
### FUNÇÕES 
#ex001 = intervalo de uma lista com números pares
def intervalo(valorInicial, valorFinal):
    lista_intervalo = []
    for i in range(valorInicial, valorFinal):
        if i % 2 == 0:
            lista_intervalo.append(i)
    print(lista_intervalo)


### CORPO PRINCIPAL
print("---------OPÇÕES---------")
print("1. Valores pares")

escolha = int(input("Digite um numero: "))

if escolha == 1:
    print("----Valores pares----")
    valorI = int(input("Digite o valor inicial: "))
    valorF = int(input("Digite o valor final: "))
    intervalo(valorI, valorF)

