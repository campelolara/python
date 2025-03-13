import math

###FUNÇÕES
#ex001 = Nota do aluno
def notaAluno():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    print(f"Sua nota final é: {media}")

    if media >= 7:
        print("APROVADO")
    elif media >= 6 and media < 7:
        print("RECUPERAÇÃO")
    else:
        print("REPROVADO")

#ex002 = Bhaskara 
def bhaskara():
    a = float(input("Qual é o Coeficiente a: "))   
    b = float(input("Qual é o Coeficiente b: ")) 
    c = float(input("Qual é o Coeficiente c: ")) 

    #pow(num, 0.5) ou math.sqrt(num) = raiz quadrada
    delta = (pow(b, 2) - 4 * a * c)
    raizQuadradaDelta = pow(delta, 0.5)
    x1 = (-(b) + (raizQuadradaDelta)) / (2 * a)
    x2 = (-(b) - (raizQuadradaDelta)) / (2 * a)

    if delta >= 0:
        print(f"O valor de x1 é: {x1:.4f}")
        print(f"O valor de x2 é: {x2:.4f}")
    else:
        print("A equação não possui raízes reais")

#ex003 = Operadora - minutos consumidos
def operadora():
    minutos = int(input("Digite a quantidade de minutos: "))

    if minutos <= 100:
        plano = 50
    else:
        plano = 50 + ((minutos-100) * 2)

    print(f"Valor a pagar: ${plano}")

#ex004 = Troco
def troco():
    precoUni = float(input("Preço unitário: "))
    quantComprada = int(input("Quantidade comprada: "))
    dinheiroRecebido = float(input("Dinheiro recebido: "))

    precoTotal = precoUni * quantComprada
    troco = dinheiroRecebido - precoTotal

    if precoTotal < dinheiroRecebido:
        print(f"TROCO: {troco}")
    elif precoTotal == dinheiroRecebido:
        print("Sem troco")
    else:
        restante = precoTotal - dinheiroRecebido
        print(f"Dinheiro insuficiente. faltam: {restante} reais")
        
#ex005 = Temperatura
def temperatura():
    escala = input("Qual a escala de temperatura (C/F)? ").lower()

    if escala == "c":
        celsius = float(input("Digite a temperatura em Celsius: "))
        convert_f = celsius * (9 / 5) + 32
        print(f"Temperatura equivalente em Fahrenheit: {convert_f:.2f}")

    elif escala == "f":
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        convert_c = (5 / 9) * (fahrenheit - 32)
        print(f"Temperatura equivalente em Celsius: {convert_c:.2f}")
    
#ex006 = Lanchonete
def lanchonete():
    codigo = int(input("Código do produto comprado: "))
    quant = int(input("Quantidade comprada: "))

    if codigo == 1:
        valor = 5.00
    elif codigo == 2:
        valor = 3.50
    elif codigo == 3:
        valor = 4.80
    elif codigo == 4:
        valor = 8.90
    elif codigo == 5:
        valor = 7.32

    valor_total = valor * quant
    print(f"Valor a pagar: {valor_total}")


#ex007 = Multiplos
def multiplos():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    if num1 % num2 == 0 or num2 % num1 == 0:
        print("São múltiplos")
    else: 
        print("NÃO são múltiplos")

#ex008 = Aumento
def aumento():
    salario = float(input("Digite o salário da pessoa: "))

    if salario <= 1000:
        percentual = 20
    elif salario > 1000 and salario <= 3000:
        percentual = 15
    elif salario > 3000 and salario <= 8000:
        percentual = 10
    else:
        percentual = 5

    aumento = (percentual / 100) * salario
    novo_salario = aumento + salario

    print(f"Novo salário: R$ {novo_salario}")
    print(f"Aumento: R$ {aumento}")
    print(f"Porcentagem:  {percentual} %")

#ex009 = Tempo de Jogo
def tempoJogo():
    inicio = int(input("Hora inicial: "))
    fim = int(input("Hora final: "))

    if inicio < fim:
        hora_total = fim - inicio
    else:
       hora_total = (24 - inicio) + fim
    
    print(f"O JOGO DUROU {hora_total} HORA(S)")


### CORPO PRINCIPAL
print("---------OPÇÕES---------")
print("1. Nota do aluno")
print("2. Bhaskara")
print("3. Operadora")
print("4. Troco")
print("5. Temperatura")
print("6. Lanchonete")
print("7. São Múltiplos?")
print("8. Aumento Salarial")
print("9. Tempo de Jogo")

escolha = int(input("Digite um numero: "))

if escolha == 1:
    print("----Nota do Aluno----")
    notaAluno()

elif escolha == 2:
    print("----Bhaskara---")
    bhaskara()

elif escolha == 3:
    print("----Operadora----")
    operadora()

elif escolha == 4:
    print("----Troco----")
    troco()

elif escolha == 5:
    print("----Temperatura----")
    temperatura()

elif escolha == 6:
    print("----Lanchonete----")
    lanchonete()

elif escolha == 7:
    print("----São Múltiplos?----")
    multiplos()

elif escolha == 8:
    print("----Aumento Salarial----")
    aumento()

elif escolha == 9:
    print("----Tempo de Jogo----")
    tempoJogo()

elif escolha == 0:
    print("Saindo....")

else:
    print("Digite um valor válido")

