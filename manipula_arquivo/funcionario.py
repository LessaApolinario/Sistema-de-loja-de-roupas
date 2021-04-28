from manipula_arquivo.manipula_arquivos import *

caminho_funcionarios = "json/dados_func.json"

lista_funcionarios = list(recuperar_dados_dict(caminho_funcionarios))

def new_funcionario(nome, cpf, rg, data_de_nascimento, area, cod) :
    return {
        "nome" : nome,
        "cpf" : cpf,
        "rg" : rg,
        "data_de_nascimento" : data_de_nascimento,
        "area" : area,
        "cod" : cod
    }

def salvar_funcionarios() :
    sobrescrever_dados(caminho_funcionarios, lista_funcionarios)

def cadastrarFuncionario(funcionario) :
    lista_funcionarios.append(funcionario)
    print("Funcionário cadastrado com sucesso!")
    salvar_funcionarios()

def demitirFuncionario(cod) :
    i = 0
    for l in lista_funcionarios :
        if l["cod"] == cod :
            del lista_funcionarios[i]
        i += 1
    print("Funcionário demitido com sucesso!")
    salvar_funcionarios()
    
def retornarFuncionarios() :
    print("Lista de funcionários: ")
    return lista_funcionarios