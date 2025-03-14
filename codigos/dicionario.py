#ex001 = Procurar produto
def procuraProduto():
    precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}
    nome_produto = input("Qual produto voçê deseja consultar o preço: ").lower()

    if nome_produto in precos:
        print(f"O {nome_produto} custa: R${precos[nome_produto]}")
    else:
        print("Tente Novamente")

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
            venda_notebook += 1

    print(venda_notebook)

vendaNotebook()





    

    
