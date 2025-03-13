
###FUNÇÕES
#ex001 = Alunos Acima da Média
def acimaMedia():
    alunos = ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo']
    notas = [6.5, 8.0, 7.2, 5.5, 9.1]

    for i, nota in enumerate(notas):
        if nota >= 7:
            print(f"O aluno {alunos[i]} passou com a nota: {nota}")
        else:
            print(f"O aluno {alunos[i]} não passou com a nota: {nota}")

#ex002 = mais de dez
def maisDeDez():
    produtos = ['Sabão', 'Detergente', 'Shampoo', 'Condicionador', 'Escova']
    precos = [3.5, 2.0, 15.0, 18.5, 8.0]

    for i, preco in enumerate(precos):
        if preco >= 10:
            print(f"O produto {produtos[i]} tem o preço: {preco}")
    
#ex003 = Salário alto
def salarioAlto():
    funcionarios = ['João', 'Mariana', 'Carlos', 'Beatriz', 'Lucas']
    salarios = [2800, 3500, 2700, 4200, 3100]

    for i, salario in enumerate(salarios):
        if salario >= 3000:
            print(f"O funcionário {funcionarios[i]} tem o salário de: {salario}")

#ex004 = Aluno e idade
def alunoIdade():
    alunos = ['Gabriel', 'Mariana', 'Sofia']
    idades = [15, 17, 14]

    for i, idade in enumerate(idades):
        print(f"O aluno {alunos[i]} tem: {idade} anos.")

#ex005 = elementos com mais de 5 letras
def maisDeCinco():
    palavras = ["Python", "Java", "C", "Ruby", "JavaScript"]
    cinco_letras = []

    for i in palavras:
        if len(i) > 5:
            cinco_letras.append(i)

    print(palavras)
    print(cinco_letras)

#ex006 = Ordenar por nota
def ordenar():
    #ordenar por nota
    #            [0]           [1]           [2]          [3]   
    #           [0,1]         [0,1]         [0,1]        [0,1]
    dados = [("João", 7), ("Maria", 9), ("Pedro", 6), ("Ana", 8)]

    #o elemento 1 de cada tupla será a chave(key) de ordenação
    dados.sort(key=lambda x: x[1])
    print(dados)


###CORPO PRINCIPAL
def main():
    #MENU
    print("---------OPÇÕES---------")
    print("1. Alunos Acima da média")
    print("2. Mais de 10")
    print("3. Salário Alto")
    print("4. Aluno e idade")
    print("5. elementos com mais de 5 letras")
    print("6. Ordenar por nota")
    print("0. Para sair")

    escolha = int(input("Digite um numero: "))

    if escolha == 1:
        print("----Alunos Acima da Média----")
        acimaMedia() 

    elif escolha == 2:
        print("----Mais de 10----")
        maisDeDez()
        
    elif escolha == 3:
        print("----Salário alto----")
        salarioAlto()
        
    elif escolha == 4:
        print("----Aluno e idade----")
        alunoIdade()
    
    elif escolha == 5:
        print("----Elementos com mais de 5 letras----")
        maisDeCinco()

    elif escolha == 6:
        print("----Ordenar por nota----")
        ordenar()

    elif escolha == 0:
        print("---Saindo---")
        
    else:
        print("Digite uma opção válida.")
            
            
main()

