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
#ex001 = Números pares e ímpares de um intervalo
def intervalo(valorInicial, valorFinal):
    lista_par = []
    lista_impar = []
    for i in range(valorInicial, valorFinal+1):
        if i % 2 == 0:
            lista_par.append(i)
        else:
            lista_impar.append(i)
    print(lista_par)
    print(lista_impar)

#ex002 = Tabuada de Multiplicação
def tabuadaMultiplicacao(num):
    for i in range(11):
        multiplicacao = num * i
        print(f"{num} x {i} = {multiplicacao}")

#ex003 = Números ímpares entre 100 e 200
def numerosImpares():
    numImpar = []
    for i in range(100, 200):
        if i % 2 != 0:
            numImpar.append(i)
    print(numImpar)

#ex004 = Contador
def contador(num):
    cont = []
    for i in range(num+1):
        cont.append(i)
    print(cont)
    
#ex005 = Soma dos números
def soma():
    numeros = []
    for i in range(5):
        numeros.append(int(input("Digite um número: ")))
    print(f"Os números digitados foram: {numeros}")
    print(f"A soma dos números é: {sum(numeros)}")

#ex006 = fatorial
def fatorial(num):
    #fatoria inicia com 1
    fat = 1
    #para cada numero de 1 até num
    for i in range(1, num+1):  
        fat *= i
    print(fat)

#ex007 = Numeros pares e ímpares de 1 até num
def parImpar(num):
    lista_par = []
    lista_impar = []
    for i in range(1, num+1):
        if i % 2 == 0:
            lista_par.append(i)
        else:
            lista_impar.append(i)
    print(f"Os números pares são: {lista_par}")
    print(f"Os números ímpares são: {lista_impar}")

#ex008 = Divisores de um Número
def divisores(num):
    lista_divisores = []
    for i in range(1, num+1):
        if num % i == 0:
            lista_divisores.append(i)
    print(f"O divisores de {num} são: {lista_divisores}")
                

        
### CORPO PRINCIPAL
print("---------OPÇÕES---------")
print("1. Par e Impar dentro de um intervalor")
print("2. Tabuada de multiplicação")
print("3. Números ímpares entre 100 e 200")
print("4. Contador")
print("5. Soma dos números")
print("6. Fatorial")
print("7. Par e Impar de 1 até um número")
print("8. Divisores de um número")

escolha = int(input("Digite um numero: "))

if escolha == 1:
    print("----Par e Impar num intervalo----")
    numI = int(input("Digite o valor inicial: "))
    numF = int(input("Digite o valor final: "))
    intervalo(numI, numF)

elif escolha == 2:
    print("----Tabuada de multiplicação----")
    num = int(input("Digite um valor: "))
    tabuadaMultiplicacao(num)

elif escolha == 3:
    print("----Números ímpares entre 100 e 200----")
    numerosImpares()

elif escolha == 4:
    print("----Contador----")
    num = int(input("Digite um valor: "))
    contador(num)

elif escolha == 5:
    print("----Soma dos números----")
    soma()

elif escolha == 6:
    print("----Fatorial----")
    num = int(input("Digite um número:"))
    fatorial(num)

elif escolha == 7:
    print("----Par e Impar de 1 até um número----")
    num = int(input("Digite um número:"))
    parImpar(num)

elif escolha == 8:
    print("----Divisores de um número----")
    num = int(input("Digite um número:"))
    divisores(num)




