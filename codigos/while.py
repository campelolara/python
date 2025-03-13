###FUNÇÕES
#ex001 = Contador e Soma
def contadorSoma():
    num = int(input("Digite um número:"))
    lista = []
    contador = 1
    while contador <= num:
        lista.append(contador)   
        contador += 1
        
    print(f"A contagem dos números é: {lista}")
    print(f"A soma dos número é: {sum(lista)}")

#ex002 = Leitura de números positivos
def leituraNumeros():
    num = int(input("Digite um número (valor negativo encerra o código):"))
    lista_numeros = []

    while num >= 0:
        lista_numeros.append(num)
        num = int(input("Digite um número (valor negativo encerra o código):"))

    print(f"Os números digitados foram: {lista_numeros}")
    print(f"A quantidade de números positivos digitados foi: {len(lista_numeros)}")

#ex003 = Soma de números (0 para)
def somaNumeros():
    numeros = []
    num = int(input("Digite um número (0 encerra): "))
    while num != 0:
        numeros.append(num)
        num = int(input("Digite um número (0 encerra): "))
    
    print(f"Os números digitados foram: {numeros}")
    print(f"A soma dos números é: {sum(numeros)}")
        

#ex004 = Validação de senha
def validacaoSenha():
    senha = input("Digite uma senha:")
    while senha != "1234":
        print("Senha inválida")
        senha = input("Digite uma senha:")
    if senha == "1234":
        print("Senha correta")

#ex005 = Contagem regressiva
def contagemRegressiva():
    num = int(input("Digite um número:"))
    lista = []
    while num >= 0:
        lista.append(num)
        num -= 1
    
    print(f"A contagem regressiva dos números é: {lista}")

#ex006 = múltiplos de 3
def multiploTres():
    num = int(input("Digite um número:"))
    lista = []
    contador = 3

    while contador <= num:
        if contador % 3 == 0:
            lista.append(contador)
        contador += 1
    
    print(f"Os valores múltiplos de 3 dentro do intervalo são: {lista}")
   
#ex007 = Cálculo fatorial[
def fatorial():
    num = int(input("Digite um número:"))
    fat = 1
    contador = 1

    while contador <= num:
        fat *= contador
        contador += 1

    print(f"O fatorial de {num} é {fat}")

#ex008 = maior que 10
def maiorQueDez():
    numeros = []
    maior_que_dez = []

    num = int(input("Digite um número (número negativo encerra): "))

    while num >= 0:
        numeros.append(num)
        num = int(input("Digite um número (número negativo encerra): "))
        if num > 10:
            maior_que_dez.append(num)
        
    print(f"Os valores informados são: {numeros}")
    print(f"Os valores maiores que dez são: {maior_que_dez}")
        

#ex009 = soma e média
def somaMedia():
    numeros = []
    num = int(input("Digite um número (-1 encerra): "))

    while num != -1:
        numeros.append(num)
        num = int(input("Digite um número (-1 encerra): "))

    media = sum(numeros) / len(numeros)

    print(f"A soma dos números digitados é {sum(numeros)}")
    print(f"A média dos números digitados é {media}")
        
#ex010 = Par e impar de um intervalo
def parImpar():
    numI = int(input("Digite o valor inicial: "))
    numF = int(input("Digite o valor final: "))
    numeros_pares = []
    numeros_impares = []

    while numI <= numF:
        if numI % 2 == 0:
            numeros_pares.append(numI)
            numI += 1
        else:
            numeros_impares.append(numI)
            numI += 1
        

    print(f"Os valores pares são: {numeros_pares}")
    print(f"Os valores impares são: {numeros_impares}")

 #ex011 = Qual número é maior e qual é o menor
def maiorMenor():
    lista = []
    contador = 1

    while contador <= 3:
        num = int(input("Digite um numero: "))
        lista.append(num)
        contador += 1

    maior_elemento = max(lista)
    menor_elemento = min(lista)
    print(f"O maior elemento é: {maior_elemento}")
    print(f"O menor elemento é: {menor_elemento}")

#ex012 = Ordenação de Listas
def lista():
    lista = []
    contador = 1

    while contador <= 5:
        lista.append(int(input("Digite valores: ")))
        contador += 1

    print(lista)

    lista.sort()
    print("Lista Ordenada", lista)

    lista.sort(reverse=True)
    print("Lista Ordenada Inversamente", lista)

    print("Maior elemento da lista", max(lista))
    


###CORPO PRINCIPAL
def main():
    #MENU
    print("---------OPÇÕES---------")
    print("1. Contador e Soma")
    print("2. Quantidade de números positivos")
    print("3. Soma de números")
    print("4. Validação de Senha")
    print("5. Contagem Regressiva")
    print("6. Múltíplo de Três")
    print("7. Cálculo fatorial")
    print("8. Maior que dez")
    print("9. Soma e média")
    print("10. Pares e Impares em um intervalo")
    print("11. Maior e menor")
    print("12. Ordenação em lista")
    print("0. Sair")

    escolha = int(input("Digite um numero: "))
    
    if escolha == 1:
        print("----Contador e Soma----")
        contadorSoma()

    elif escolha == 2:
        print("----Quantidade de números positivos----")
        leituraNumeros()

    elif escolha == 3:
        print("----Soma de números----")
        somaNumeros()

    elif escolha == 4:
        print("----Validação de Senha----")
        validacaoSenha()

    elif escolha == 5:
        print("----Contagem Regressiva----")
        contagemRegressiva()

    elif escolha == 6:
        print("----Múltíplo de Três----")
        multiploTres()

    elif escolha == 7:
        print("----Cálculo fatorial----")
        fatorial()

    elif escolha == 8:
        print("----Maior que dez----")
        maiorQueDez()

    elif escolha == 9:
        print("----Soma e Média----")
        somaMedia()

    elif escolha == 10:
        print("----Pares e Impares em um intervalo----")
        parImpar()

    elif escolha == 11:
        print("----Maior e menor----")
        maiorMenor()

    elif escolha == 12:
        print("----Ordenação em lista----")
        lista()

    elif escolha == 0:
        print("---Saindo---")
        
    else:
        print("Digite uma opção válida.")



main()

