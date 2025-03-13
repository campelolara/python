###FUNÇÕES
##Funções de ajuda
#lista de string
def listaString():
    lista = []
    item = input("Digite um item para adicionar a lista (espaço finaliza): ")
    
    while item != " ":
        lista.append(item)
        item = input("Digite um item para adicionar a lista (espaço finaliza): ")

    return lista

#lista numérica
def listaNum():
    numeros = []
    num = float(input("Digite um número (0 finaliza): "))
    
    while num != 0:
        numeros.append(num)
        num = float(input("Digite um número (0 finaliza): "))

    return numeros

#ex001 = Fazer uma lista 
def lista():
    lista_digitada = listaString()

    print("Sua lista é: ")
    for i in lista_digitada:
        print(i)

#ex002 = Soma
def soma():
    numeros_digitados = listaNum()
    print(f"A soma dos números é: {sum(numeros_digitados)}")

#ex003 = múltiplos de 5
def multiplo():
    numeros_digitados = listaNum()
    listaMultiplos = []

    for i in numeros_digitados:
        if i % 5 == 0:
            listaMultiplos.append(i)

    print(f"Os múltiplos de 5 são: {listaMultiplos}")

#ex004 = multiplicar por 2
def dobrar():
    numeros_digitados = listaNum()
    dobrados = []
    
    for i in numeros_digitados:
        dobrados.append(i * 2)

    print(f"Os números dobrados ficam: {dobrados}")

#ex005 = transformar em maiúscula
def transformaString():
    lista_digitada = listaString()
    emMinusculo = []
    emMaiusculo = []
    
    for i in lista_digitada:
        emMinusculo.append(i.lower())
        emMaiusculo.append(i.upper())

    print(f"Tudo minúsculo é: {emMinusculo}")
    print(f"Tudo maiúsculo é: {emMaiusculo}")

#ex006 = retirar espaçoes extras nas palavras
def removerEspaco():
    lista_digitada = listaString()
    lista_sem_espaco = []

    for i in lista_digitada:
        lista_sem_espaco.append(i.strip())

    print(f"Com espaço: {lista_digitada}")
    print(f"Sem espaço: {lista_sem_espaco}")

#ex007 = Imprimir palavra com inicial específica
def imprimirPalavra():
    lista_digitada = listaString()

    for i in lista_digitada:
        if i[0] == "A" or i[0] == "a":
            print(i)

#ex008 = Converção de temperatura
def conversaoTemperatura():
    numeros_digitados = listaNum()
    convertidos = []

    for i in numeros_digitados:
        convert_f = i * (9 / 5) + 32
        convertidos.append(convert_f)

    print(f"Em Celsius: {numeros_digitados}")
    print(f"Em Fahrenheit: {convertidos}")

#ex009 = Remover itens pares
def removePar():
    numeros = listaNum()
    print(numeros)

    for i in numeros:
        if i % 2 == 0:
            numeros.remove(i)

    print(numeros)

#ex010 = Quadrado dos números
def quadrado():
    numeros = listaNum()
    quadrado = []

    for i in numeros:
        i **= 2
        quadrado.append(i)

    print(numeros)
    print(quadrado)

#ex011 = Inserir e Remover
def inserirRemover():
    numeros = listaNum()

    print(f"Os números informados são: {numeros}")
    remover = int(input("Qual valor deseja remover? "))

    numeros.remove(remover)
    print(f"Os novos valores são: {numeros}")



###CORPO PRINCIPAL
print("---------OPÇÕES---------")
print("1. Fazer uma lista")
print("2. Soma")
print("3. Múltiplos de 5")
print("4. Dobrar valores")
print("5. Formatação de texto")
print("6. Retirar espaço")
print("7. Imprimir palavra")
print("8. Celsius para Fahrenheit")
print("9. Remover itens pares")
print("10. Quadrado dos números")
print("11. Inserir e Remover")
print("0. Sair")
escolha = int(input("Digite um numero: "))

if escolha == 1:
    print("----Fazer uma lista----")
    lista()
    
elif escolha == 2:
    print("----Soma----")
    soma()

elif escolha == 3:
    print("----Múltiplos de 5----")
    multiplo()

elif escolha == 4:
    print("----Dobrar valores----")
    dobrar()

elif escolha == 5:
    print("----Formatação de texto----")
    transformaString()

elif escolha == 6:
    print("----Retirar espaço----")
    removerEspaco()

elif escolha == 7:
    print("----Imprimir palavra----")
    imprimirPalavra()

elif escolha == 8:
    print("----Celsius para Fahrenheit----")
    conversaoTemperatura()
elif escolha == 9:
    print("----Remover itens pares----")
    removePar()

elif escolha == 10:
    print("----Quadrado dos números----")
    quadrado()

elif escolha == 11:
    print("----Inserir e Remover----")
    inserirRemover()

elif escolha == 0:
    print("Saindo....")

else:
    print("Digite um valor válido")


