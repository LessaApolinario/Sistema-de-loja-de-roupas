from manipula_arquivo.manipula_arquivos import *

caminho_cliente = "json/dados_clientes.json"

#Lista que será carregada com os dados do arquivo.
lista_clientes = list(recuperar_dados_dict(caminho_cliente))

def new_cliente(nome, cpf, rg, data_de_nascimento, cartao, bandeira) :
    return {
        "nome" : nome,
        "cpf" : cpf,
        "rg" : rg,
        "data_de_nascimento" : data_de_nascimento,
        "cartao" : cartao,
        "bandeira" : bandeira
    }

def salvar_clientes() :
    sobrescrever_dados(caminho_cliente, lista_clientes)

def cadastrarCliente(cliente) :
    lista_clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")
    salvar_clientes()

def deletarCliente(cpf) :
    i = 0
    for l in lista_clientes :
        if l["cpf"] == cpf :
            del lista_clientes[i]
        i += 1
    print("Cliente deletado com sucesso!")
    salvar_clientes()

def retornarClientes() :
    print("Lista de clientes: ")
    return lista_clientes