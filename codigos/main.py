import math

"""
#ex002 e ex003 = soma, subtração, multiplicação e divisão
num1 = float(input("Informe um número: "))
num2 = float(input("Informe outro número: "))

soma = num1 + num2 
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
media = (num1 + num2) / 2

print(f"A soma dos dois números é {soma}")
print(f"A subtração dos dois números é {subtracao}")
print(f"A multiplicação dos dois números é {multiplicacao}")
print(f"A divisão dos dois números é {divisao}")
print(f"A média dos dois números é {media}")

########################################################

#ex001 e ex004 =  nome, idade e cidade
nome = input("Qual o seu nome: ")
idade = int(input("Qual a sua idade: "))
cidade = input("Em qual cidade você mora: ")

print(f" Olá, seja bem-vindo(a) {nome}. Você tem {idade} anos e mora em {cidade}")

########################################################

#ex006 = calcular a área de um retângulo (base × altura)
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

area = base * altura

print(f"A área do rentângulo é {area}")

########################################################

#ex007 = Celsius para Fahrenheit - F = (C × 9/5) + 32
celsius = float(input("Digite a temperatura em grau Celsius: "))

convert_fahrenheit = (celsius * 9/5) + 32

print(f"O grau em Celsius convertido para Fahrenheit é {convert_fahrenheit}")

########################################################

#ex008 = Cálculo do Perímetro de um Quadrado - 4 × lado
lado = float(input("Quanto é o lado do quadrado: "))

perimetro = 4 * lado

print(f"O perímetro do quadrado é: {perimetro}")

########################################################

#ex009 = Conversão Real para Dolar

real = float(input("Digite o valor em real: "))

dolar = real / 5

print(f"O valor em dólar é: {dolar}")

########################################################

#ex010 = Área do triângulo - (base * altura) / 2
base = float(input("Qual é a base do triângulo? "))
altura = float(input("Qual é a altura do triângulo? "))

area = (base * altura) / 2

print(f"O triângulo de base {base} e de altura {altura}, possui a área = {area}")

########################################################

#ex011 = IMC -  peso / (altura × altura)
peso = float(input("Digite seu peso(kg): "))
altura = float(input("Digite sua altura(kg): "))

imc = peso / (altura * altura)

print(f"O seu IMC é: {imc}")  #colocar limite de casa decimal

########################################################

#ex012 = calcular desconto - preço_final = preço_original - (preço_original × desconto/100). 

preco_original = float(input("Digite o preço original do produto: "))
desconto = float(input("Digite o desconto(%): "))

preco_final = preco_original - (preco_original * (desconto / 100))

print(f"O preço final é de: {preco_final}")  

########################################################

#ex013 = Aumento Salarial - novo_salário = salário + (salário × aumento/100)
salario = float(input("Digite o salário: "))
aumento = float(input("Digite o seu aumento(%): "))

novo_salario = salario + (salario * (aumento / 100))

print(f"O seu novo salário é: {novo_salario}")  

########################################################

#ex014 = Cálculo do Custo de Viagem - custo = (distância / consumo) × preço 
distancia = float(input("Digite a distância em km: "))
consumo = float(input("Digite o consumo de galosina em km/l: "))
preco = float(input("Digite o preço do combústivel: "))

custo = (distancia / consumo) * preco

print(f"O custo da viagem é: {custo}") 

########################################################

#ex016 = Centimetros para metros
centimetro = float(input("Digite o centímetro: "))

metro = centimetro / 100

print(f"Em metro é: {metro}") 

########################################################

#ex017 = Volume de um Cubo - aresta³
aresta = float(input("Digite a aresta do cubo: "))

volume = math.pow(aresta, 3)

print(f"O volume do cubo é: {volume}") 

########################################################

#ex018 = Segundos para minutos
segundos = float(input("Digite os segundos: "))

minutos = segundos / 60

print(f"Em minutos é: {minutos}") 

########################################################

#ex019 - Percentual = (valor_parcial / valor_total) × 100
valor_parcial = float(input("Digite o valor parcial: "))
valor_total = float(input("Digite o valor total: "))

percentual = (valor_parcial / valor_total) * 100

print(f"Em percentual é: {percentual}") 

########################################################

#ex020 = Área do Circulo - área = 3.14 × (raio × raio)
raio = float(input("Digite o raio do circulo: "))

area = 3.14 * (raio * raio)

print(f"A area do circulo é: {area}")

########################################################

#ex025 - média = (n1 × p1 + n2 × p2 + n3 × p3) / (p1 + p2 + p3)
num1 = float(input("Digite o primeiro número: "))
peso1 = float(input("Digite o PESO do primeiro número: "))
num2 = float(input("Digite o segundo número: "))
peso2 = float(input("Digite o PESO do segundo número: "))
num3 = float(input("Digite o terceiro número: "))
peso3 = float(input("Digite o PESO do terceiro número: "))

media = ((num1 * peso1) + (num2 * peso2) + (num3 * peso3)) / (peso1 + peso2 + peso3)

print(f"A média ponderada destes valores é: {media}")

########################################################

"""





