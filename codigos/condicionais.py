"""
#ex001 = positivo ou negativo
num = int(input("Digite um número: "))

if num > 0:
    print("Positivo")
else:
    print("Negativo")

########################################################
#ex002 = par ou ímpar
num = int(input("Digite um número: "))

if num % 2 == 0:
    print("O número informado é par")
else:
    print("“O número informado é ímpar")

########################################################
#ex003 = múltiplo de 3
num = int(input("Digite um número: "))

if num % 3 == 0:
    print("O número informado é múltiplo de 3")
else:
    print("O número informado NÃO é múltiplo de 3")

########################################################
#ex004 = maior, menor ou igual
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 == num2:
    print(f"Os números {num1} e {num2} são iguais")
elif num1 > num2:
    print(f"O número {num1} é maior")
else:
    print(f"O número {num2} é menor")

########################################################
#ex005 = maior número
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite outro número: "))

if num1 > num2 and num1 > num3:
    print(f"O número {num1} é o maior")
elif num2 > num3:
    print(f"O número {num2} é o maior")
else:
    print(f"O número {num3} é o maior")

########################################################
#ex006 = de maior e de menor
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"Você possui {idade} anos, já é de maior")
else:
    print(f"Você possui {idade} anos, ainda é de menor")

########################################################
#ex007 = aprovado, de recuperação e reprovado
nota = float(input("Digite sua nota: "))

if nota >= 6:
    print("Você está aprovado!")
elif nota < 6 and nota > 4:
    print("Você está em recuperação!")
else:
    print("Você está reprovado!")

########################################################
#ex008 = Vogal ou Consoante

letra = input("Digite uma letra: ").lower()

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

########################################################
#ex009 = nome do dia da semana
num = int(input("Digite o dia da semana (1 a 7): "))

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

########################################################
#ex010
num = int(input("Digite o dia da semana (1 a 12): "))

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
 
########################################################
#ex011 = se é ano bissexto
ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} NÃO é bissexto")

########################################################
#ex012 = Aumento de 10% no salário ou NADA
salario = float(input("Digite o seu salário: "))

if salario >= 1000:
    print("O seu salário será mantido!")
else:
    salario = salario * 1.10
    print(f"Seu novo salário é {salario:.2f}")

########################################################
#ex013 = Se o número ta dentro do intervalo
num = int(input("Digite um número: "))

if num >= 1 and num <= 100:
    print(f"{num} está dentro do intervalo de 1 a 100")
else:
    print(f"{num} NÃO está dentro do intervalo de 1 a 100")

########################################################
#ex014 = Está frio, quente ou moderado?
temperatura = float(input("Digite a temperatura: "))

if temperatura < 15:
    print("Está frio")
elif temperatura >= 15 and temperatura <= 25:
    print("Está moderado")
else:
    print("Está quente")

########################################################
#ex015 = Se é alto
altura = float(input("Digite sua altura:"))

if altura >= 1.80:
    print("Você é alto")
else:
    print("Você é baixo zé")

########################################################
#ex016 = Saudação
pronome = input("Digite o seu pronome (ele/ela/elu): ").lower()

if pronome == "ele":
    print("Seja bem vindo!")
elif pronome == "ela":
    print("seja bem vinda!")
else:
    print("Seja bem vindx!")
 
########################################################
#ex017 = Menu

print("-------------MENU-------------")
print("1. Cadastrar")
print("2. Consultar")
print("3. Atualizar")
print("4. Excluir")

escolha = int(input("Digite um número correspondente ao que deseja: "))

if escolha == 1:
    print("Área de Cadastro")
elif escolha == 2:
    print("Área de Consulta")
elif escolha == 3:
    print("Área de Atualização")
elif escolha == 4:
    print("Área de exclusão")
else:
    print("Digite um número correspondente!")

"""
########################################################
#ex019 = Pontuação de um jogo

pontuacao = int(input("Digite sua pontuação: "))

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


"""
#Verificar a Coordenada
x = float(input("Digite o valor do eixo x: "))
y = float(input("Digite o valor do eixo y: "))

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
"""


