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

def imprimirPalavra():
    lista_digitada = listaString()

    for i in lista_digitada:
        if i[0] == "A" or i[0] == "a":
            print(i)

def conversaoTemperatura():
    numeros_digitados = listaNum()
    convertidos = []

    for i in numeros_digitados:
        convert_f = i * (9 / 5) + 32
        convertidos.append(convert_f)

    print(f"Em Celsius: {numeros_digitados}")
    print(f"Em Fahrenheit: {convertidos}")

def acimaMedia():
    numeros_digitados = listaNum()

    for i in numeros_digitados:
        if i >= 7:
            print(i)




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
print("9. Alunos acima da Média")


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
    print("----Alunos acima da Média----")
    acimaMedia()

    