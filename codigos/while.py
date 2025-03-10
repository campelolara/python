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



###CORPO PRINCIPAL
print("---------OPÇÕES---------")
print("1. Contador e Soma")
print("2. Quantidade de números positivos")
print("3. Soma de números")
print("4. Validação de Senha")
print("5. Contagem Regressiva")

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


