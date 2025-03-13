import math
###FUNÇÕES
def areaCirculo():
    raio = float(input("Digite o raio do círculo: "))

    area = 3.14 * pow(raio, 2)
    print(f"A área é: {area}")


def areaLosangulo():
    diagonalMaior = float(input("Digite a diagonal maior do losângulo: "))
    diagonalMenor = float(input("Digite a diagonal menor do losângulo: "))

    area = (diagonalMaior  * diagonalMenor) / 2
    print(f"A área é: {area}")


def areaQuadrado():
    lado = float(input("Digite o lado do quadrado: "))

    area = pow(lado, 2)
    print(f"A área é: {area}")


def areaRetangulo():
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))

    area = base * altura
    print(f"A área é: {area}")


def areaTrapezio():
    baseMaior = float(input("Digite a base maior do trapézio: "))
    baseMenor = float(input("Digite a base menor do trapézio: "))
    altura = float(input("Digite a altura do trapézio: "))

    area = (baseMenor + baseMaior) * (altura / 2)
    print(f"A área é: {area}")


def areaTriangulo():
    base = float(input("Digite a base do triangulo: "))
    altura = float(input("Digite a altura do triangulo: "))
    area = (base * altura) / 2
    print(f"A área é: {area}")

###CORPO PRINCIPAL
print("---Escolha a figura geométrica que deseja calcular a área---")
print("1. Circulo")
print("2. Losângulo")
print("3. Quadrado")
print("4. Retângulo")
print("5. Trapézio")
print("6. Triângulo")



escolha = int(input("Digite um numero: "))

if escolha == 1:
    print("----Circulo----")
    areaCirculo()
    

elif escolha == 2:
    print("----Losângulo----")
    areaLosangulo()


elif escolha == 3:
    print("----Quadrado----")
    areaQuadrado()
    

elif escolha == 4:
    print("----Retângulo----")
    areaRetangulo()


elif escolha == 5:
    print("----Trapézio----")
    areaTrapezio()
    

elif escolha == 6:
    print("----Triângulo----")
    areaTriangulo()
    

