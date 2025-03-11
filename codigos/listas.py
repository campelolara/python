"""
#remover itens pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros)

for elementos in numeros:
    if elementos % 2 == 0:
        numeros.remove(elementos)

print(numeros)

#substituir o valor
numeros[0] = 20
print(numeros)

#se tem dentro da lista

if 11 in numeros:
    print("possui o valor")
else:
    print("não possui o valor")

######################################
#Retorna elementos com mais de 5 letras
palavras = ["Python", "Java", "C", "Ruby", "JavaScript"]
cinco_letras = []

for i in palavras:
    if len(i) > 5:
        cinco_letras.append(i)

print(palavras)
print(cinco_letras)

######################################
#cada item da lista multiplicado
numeros = [2, 4, 6, 8, 10]
multiplicados = []

for i in numeros:
    i *= 2
    multiplicados.append(i)

print(numeros)
print(multiplicados)

######################################
#ordenar valores digitados
numeros = []
num = int(input("Digite um número: "))

while num != 0:
    numeros.append(num)
    num = int(input("Digite um número: "))

numeros.sort()
print(f"OS números ordenados ficam: {numeros}")

######################################
#nova lista com os quadrados de cada item
numeros = [2, 4, 6, 8, 10]
quadrado = []

for i in numeros:
    i **= 2
    quadrado.append(i)

print(numeros)
print(quadrado)

######################################
#transformar uma string em uma lista
frase = "Python é uma linguagem poderosa e divertida"

lista = []
lista.append(frase.split())
print(frase)
print(lista)


######################################
#remover um elemento específico
contador = 1
numeros = []
num = int(input("Digite um número:"))

while contador <= 11:
    numeros.append(num)
    num = int(input("Digite um número:"))
    contador += 1

print(f"Os números informados são: {numeros}")
remover = int(input("Qual valor deseja remover? "))

numeros.remove(remover)
print(f"Os novos valores são: {numeros}")

######################################
#ordenar por nota
#            [0]           [1]           [2]          [3]   
#           [0,1]         [0,1]         [0,1]        [0,1]
dados = [("João", 7), ("Maria", 9), ("Pedro", 6), ("Ana", 8)]

#o elemento 1 de cada tupla será a chave(key) de ordenação
dados.sort(key=lambda x: x[1])
print(dados)

######################################
#cópia
import copy 

original = [[1, 2], [3, 4]]
copia = copy.deepcopy(original)
print(copia)

"""
######################################
#dicionario
texto = "A prática leva à perfeição. A repetição traz aprendizado"

for i in texto:
    if i in texto:
        print(texto.count(i))

















