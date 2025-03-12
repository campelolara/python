import math

def areaTriangulo(base, altura):
    area = (base * altura) / 2
    return area

def areaQuadrado(lado):
    area = pow(lado, 2)
    return area

def areaTrapezio(baseMenor, baseMaior, altura):
    area = (baseMenor + baseMaior) * (altura / 2)
    return area

def areaCirculo(raio):
    area = 3.14 * pow(raio, 2)
    return area

def areaRetangulo(base, altura):
    area = base * altura
    return area

def areaLosangulo(diagonalMaior, diagonalMenor):
    area = (diagonalMaior  * diagonalMenor) / 2
    return area

res = areaLosangulo(6, 4)
print(res)



