#ex002 = Mais vendidos
def maisVendido():
    mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu', 'livros': 'o alquimista', 
                    'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}

    vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 
                        'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 
                        'notebook dell': 17000, 'notebook asus': 2450}

    print(f"O mais vendido na categoria livro: {mais_vendidos['livros']}")
    print(f"O mais vendido na categoria lazer: {mais_vendidos['lazer']}")
    print(f"O valor do 'notebook asus' é: {vendas_tecnologia['notebook asus']}")

#Se possui a chave copo
    if vendas_tecnologia.get('copo') == None:
        print("Copo não está dentro da lista de tecnologia")
    else:
        print(vendas_tecnologia.get('copo'))

def adicionarValor():
    lucro1 = {'janeiro': 100000, 'fevereiro': 120000, 'março': 90000}
    lucro2 = {'abril': 88000, 'maio': 89000, 'junho': 120000}

    lucro1.update(lucro2)
    lucro1['janeiro'] = 80000

    print(lucro1)

    lucro1.clear()
    print(lucro1)

    del(lucro2)
    

#total de notebook vendido
def vendaNotebook():
    vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 
                         'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 
                         'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}
    
    venda_notebook = 0
    for produto in vendas_tecnologia:
        if 'notebook' in produto:
            venda_notebook += vendas_tecnologia[produto]

    print(venda_notebook)

#vendas acima de 5000
def vendas():
    vendas = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 
              'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 
              'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}
    
    for produto, qtde in vendas.items():
        if qtde > 5000:
            print(f"{produto}: {qtde} unidades")


    #for chave in vendas:
        #if vendas[chave] >= 5000:
            #print(f"{chave}: {vendas[chave]}")

def chaveValor():
    vendas = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 
              'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 
              'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}
    
    chaves = vendas.keys()
    valores = vendas.values()
    print(list(chaves)) #chave em forma de lista
    print(valores) #valor em forma de tupla


#Consultar produtos
def consultaProdutos():
    produtos = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 
                        'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 
                        'notebook dell': 17000, 'notebook asus': 2450}

    produto_digitado = input("Digite um produto que deseja consultar: ").lower()

    
    if produto_digitado in produtos:
        preco = produtos[produto_digitado]
        print(f"O produto {produto_digitado} tem  o valor de R${preco}.")
    else:
        opcao = input(f"Produto {produto_digitado} não encontrado! Deseja cadastra-lo? (S/N)").lower()
        if opcao == "s":
            preco = float(input(f"Digite o valor de {produto_digitado}: "))
            produtos[produto_digitado] = preco
            print(produtos)

        else:
            print("Tchau!")


#reajuste de preço
def reajusteDePreco():
    precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 3000}
    novos_precos = {}
    for produto in precos:
        preco_produto = precos[produto]
        if preco_produto <= 1000:
            novo_preco = preco_produto * 1.1
        elif preco_produto <= 2000:
            novo_preco = preco_produto * 1.15
        else:
            novo_preco = preco_produto * 1.2
        print(f"Produto {produto}, Novo Preço: R${novo_preco:.2f}")
        novos_precos[produto] = novo_preco
    total_antigo = sum(precos.values())
    total_novo = sum(novos_precos.values())
    reajuste = total_novo - total_antigo
    print(f"O reajuste total foi de R${reajuste}")


"""
- Uma empresa está analisando os resultados de vendas do 1º semestre de 2022 e 2023
- Qual foi o % de crescimento de cada mês de 2023 em relação a 2022?
- Depois de calcular isso, calcule o valor total de crescimento de 2023 em relação a 2022
"""

def analiseDeSemestre():
    vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000}
    vendas_23 = {"jan": 17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500}

    for mes in vendas_23:
        valor_22 = vendas_22[mes]
        valor_23 = vendas_23[mes]
        percentual = valor_23 / valor_22 - 1
        print(f"Em {mes}, a variação percentual foi de: {percentual:.1%}")

    total_22 = sum(vendas_22.values())
    total_23 = sum(vendas_23.values())
    crescimento = total_23 / total_22 - 1
    print(f"Crescimento Real: {crescimento:.1%}")


#nível de co2
def nivelDeCo2():
    niveis_co2 = {
    'AC': [325,405,429,486,402],
    'AL': [492,495,310,407,388],
    'AP': [507,503,368,338,400],
    'AM': [429,456,352,377,363],
    'BA': [321,508,372,490,412],
    'CE': [424,328,425,516,480],
    'ES': [449,506,461,337,336],
    'GO': [425,460,385,485,460],
    'MA': [361,310,344,425,490],
    'MT': [358,402,425,386,379],
    'MS': [324,357,441,405,427],
    'MG': [345,367,391,427,516],
    'PA': [479,514,392,493,329],
    'PB': [418,499,317,302,476],
    'PR': [420,508,419,396,327],
    'PE': [404,444,495,320,343],
    'PI': [513,513,304,377,475],
    'RJ': [502,481,492,502,506],
    'RN': [446,437,519,356,317],
    'RS': [427,518,459,317,321],
    'RO': [517,466,512,326,458],
    'RR': [466,495,469,495,310],
    'SC': [495,436,382,483,479],
    'SP': [495,407,362,389,317],
    'SE': [508,351,334,389,418],
    'TO': [339,490,304,488,419],
    'DF': [376,516,320,310,518], 
}
    
    for estado in niveis_co2:
        quant_sensores = len(niveis_co2[estado])
        total_co2 = sum(niveis_co2[estado])
        media_co2 = total_co2 / quant_sensores
        if media_co2 > 450:
            print(f"O {estado} está com níveis altíssimos de CO2 ({media_co2}), chamar equipe especializada para verificar a região.")

    

nivelDeCo2()


    

















    

    
