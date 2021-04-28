from manipula_arquivo.manipula_arquivos import *

caminho_vendas = 'json/dados_venda.json'
lista_vendas = list(recuperar_dados_dict(caminho_vendas))

def new_venda(cod, tipo, saldo) :
    return {
        "cod" : cod,
        "tipo" : tipo,
        "saldo" : saldo
    }

def salvar_vendas() :
    sobrescrever_dados(caminho_vendas, lista_vendas)

def realizarVenda(venda) :
    lista_vendas.append(venda)
    print("Venda realizada com sucesso!")
    salvar_vendas()

def retornarVendas() :
    return lista_vendas