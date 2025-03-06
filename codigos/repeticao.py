#### EXERCÍCIOS COM ESTRUTURA DE REPETIÇÃO WHILE ####

###FUNÇÕES
#Qual número é maior e qual é o menor
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
    
#Ordenação de Listas
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



### CORPO PRINCIPAL
print("---------OPÇÕES---------")
print("1. Maior e menor número")
print("2. Listas")

escolha = int(input("Digite um numero: "))

if escolha == 1:
    print("----Maior e menor número----")
    maiorMenor()
elif escolha == 2:
    print("-----------Listas-----------")
    lista()
    