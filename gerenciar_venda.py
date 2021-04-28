from manipula_arquivo.manipula_arquivos import *
from manipula_arquivo.venda import *
from manipula_arquivo.roupa import *

def realizar_venda() :
    lista_roupas = retornarRoupas()
    print(lista_roupas)
    cod = input("Informe o código do produto desejado: ")
    for i in lista_roupas :
        if i["cod"] == cod :
            quantidade = int(input("Informe a quantidade do produto: "))
            if i["quantidade"] >= quantidade :
                saldo = i["preco"] * quantidade
                vendaRealizada = new_venda(cod, i["tipo"], saldo)
                realizarVenda(vendaRealizada)
                i["quantidade"] -= quantidade
                atualizar_roupa(i)
                return 
            else :
                print("Quantidade indisponível!\n")
                return

    print("Código digitado não encontrado!\n")
    input("Digite enter para continuar...")

def exibir_venda() :
    lista_vendas = retornarVendas()
    print(lista_vendas)
