#### EXERCÍCIOS DE CONDICIONAIS ####

### FUNÇÕES
#verificar se é positivo ou negativo
def positivoNegativo(num):
    if num > 0:
        print("Positivo")
    else:
        print("Negativo")

#verificar se é par ou ímpar
def parImpar(num):
    if num % 2 == 0:
        print("O número informado é par")
    else:
        print("“O número informado é ímpar")

#Se é múltiplo de 3
def multiploDeTres(num):
    if num % 3 == 0:
        print("O número informado é múltiplo de 3")
    else:
        print("O número informado NÃO é múltiplo de 3")

#Se é maior, menor ou igual
def maiorMenorIgual(num1, num2):
    if num1 == num2:
        print(f"Os números {num1} e {num2} são iguais")
    elif num1 > num2:
        print(f"O número {num1} é maior")
    else:
        print(f"O número {num2} é maior")

#Se é maior
def maiorNumero(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(f"O número {num1} é o maior")
    elif num2 > num3:
        print(f"O número {num2} é o maior")
    else:
        print(f"O número {num3} é o maior")

#Se é maior ou menor de idade
def deMaiorDeMenor(idade):
    if idade >= 18:
        print(f"Você possui {idade} anos, já é de maior")
    else:
        print(f"Você possui {idade} anos, ainda é de menor")

#Vogal ou Consoante
def vogalConsoante(letra):
    vogais = ['a', 'e', 'i', 'o', 'u']
    
    consoante = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 
                 'k', 'l', 'm', 'n', 'p', 'q', 'r', 
                 's', 't', 'v', 'w', 'x', 'y', 'z']
    
    if letra in vogais:
        print(f"{letra} é uma vogal")
    elif letra in consoante:
        print(f"{letra} é uma consoante")
    else:
        print("Não é vogal ou consoante")

#Nome do dia da semana
def diaSemana(num):
    if num == 1:
        print('domingo')
    elif num == 2:
        print('segunda')
    elif num == 3:
        print('terça')
    elif num == 4:
        print('quarta')
    elif num == 5:
        print('quinta')
    elif num == 6:
        print('sexta')
    elif num == 7:
        print("sábado")
    else:
        print("Digite um número válido.")

#Dias do mês
def diaMes(num):
    if num == 1:
        print('janeiro tem 31 dias')
    elif num == 2:
        print('fevereiro tem 28 dias')
    elif num == 3:
        print('março tem 31 dias')
    elif num == 4:
        print('abril tem 30 dias')
    elif num == 5:
        print('maio tem 31 dias')
    elif num == 6:
        print('junho tem 30 dias')
    elif num == 7:
        print("julho tem 31 dias")
    elif num == 8:
        print("agosto tem 31 dias")
    elif num == 9:
        print("setembro tem 30 dias")
    elif num == 10:
        print("outubro tem 31 dias")
    elif num == 11:
        print("novembro tem 30 dias")
    elif num == 12:
        print("dezembro tem 31 dias")
    else:
        print("Digite um número válido.")

#Se o ano é bissexto
def anoBissexto(ano):
    if ano % 4 == 0:
        print(f"O ano {ano} é bissexto")
    else:
        print(f"O ano {ano} NÃO é bissexto")

#Pontuação de um jogo
def pontuacaoJogo(pontuacao):
    if pontuacao < 50:
        print("Ruim")
    elif pontuacao >= 50 and pontuacao <= 70:
        print("Regular")
    elif pontuacao >= 71 and pontuacao <= 90:
        print("Bom")
    elif pontuacao > 90:
        print("Excelente")
    else:
        print("Não entendi!")

#Verificar Quadrante com coordenadas
def coordenada(x, y):
    
    if x > 0 and y > 0:
        print(f"As coordenadas {x} e {y} estão no Quadrante 1")
    elif x < 0 and y > 0:
        print(f"As coordenadas {x} e {y} estão no Quadrante 2")
    elif x < 0 and y < 0:
        print(f"As coordenadas {x} e {y} estão no Quadrante 3")
    elif x > 0 and y < 0:
        print(f"As coordenadas {x} e {y} estão no Quadrante 4")
    elif x == 0 and y == 0:
        print(f"As coordenadas {x} e {y} estão na Origem")
    elif x != 0 and y == 0:
        print(f"As coordenadas {x} e {y} estão no Eixo x")
    elif x == 0 and y != 0:
        print(f"As coordenadas {x} e {y} estão no Eixo y")
    else:
        print("Digite um valor válido")


### CORPO PRINCIPAL
print("---------OPÇÕES---------")
print("1. Número positivo ou negativo")
print("2. Par ou Ímpar")
print("3. Se é múltiplo de 3")
print("4. Se é maior, menor ou igual")
print("5. Maior número")
print("6. Maior ou menor de idade")
print("7. Vogal ou Consoante")
print("8. Nome do dia da semana")
print("9. Dias do mês")
print("10. Se o ano é bissexto")
print("11. Pontuação de um  jogo")
print("12. Verificar Quandrante com Coordenadas")

escolha = int(input("Digite um numero: "))

if escolha == 1:
    print("----Positivo ou Negativo----")
    num = int(input("Digite um número: "))
    positivoNegativo(num)
elif escolha == 2:
    print("--------Par ou Ímpar--------")
    num = int(input("Digite um número: "))
    parImpar(num)
elif escolha == 3:
    print("--------Múltiplo de 3--------")
    num = int(input("Digite um número: "))
    multiploDeTres(num)
elif escolha == 4:
    print("----Maior, menor ou igual----")
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    maiorMenorIgual(num1, num2)
elif escolha == 5:
    print("---------Maior número---------")
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    num3 = int(input("Digite outro número: "))
    maiorNumero(num1, num2, num3)
elif escolha == 6:
    print("----Maior ou menor de idade----")
    idade = int(input("Digite sua idade: "))
    deMaiorDeMenor(idade)
elif escolha == 7:
    print("------Vogal ou Consoante-------")
    letra = input("Digite uma letra: ").lower()
    vogalConsoante(letra)
elif escolha == 8:
    print("------Nome do dia da semana-------")
    num = int(input("Digite o dia da semana (1 a 7): "))
    diaSemana(num)
elif escolha == 9:
    print("---------Dias do mês-----------")
    num = int(input("Digite o mês (1 a 12): "))
    diaMes(num)
elif escolha == 10:
    print("----------Ano Bissexto-----------")
    ano = int(input("Digite o ano: "))
    anoBissexto(ano)
elif escolha == 11:
    print("------Pontuação de um jogo-------")
    pontuacao = int(input("Digite sua pontuação: "))
    pontuacaoJogo(pontuacao)
elif escolha == 12:
    print("------Verificar Coordenada-------")
    x = float(input("Digite o valor do eixo x: "))
    y = float(input("Digite o valor do eixo y: "))
    coordenada(x, y)
else:
    print("Não compreendi sua resposta!")

