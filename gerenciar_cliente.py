from manipula_arquivo.cliente import *

def cadastrar_cliente() :
    nome = input("Informe seu nome: ")
    cpf = input("Informe o seu CPF: ")
    rg = input("Informe o seu RG: ")
    data_de_nascimento = input("Informe a sua data de nascimento: ")
    cartao = input("Informe o seu cartão de crédito: ")
    bandeira = input("Informe a bandeira do seu cartão de crédito: ")
    clienteCadastrado = new_cliente(nome, cpf, rg, data_de_nascimento, cartao, bandeira)
    cadastrarCliente(clienteCadastrado)

def excluir_cliente() :
    cpf = input("Informe o CPF do cliente a ser deletado: ")
    deletarCliente(cpf)

def exibir_clientes() :
    lista_clientes = retornarClientes()
    print(lista_clientes)