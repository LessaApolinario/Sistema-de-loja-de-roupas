from manipula_arquivo.manipula_arquivos import *
from manipula_arquivo.funcionario import *

def cadastrar_funcionario() :
    nome = input("Informe o seu nome: ")
    cpf = input("Informe o seu CPF: ")
    rg = input("Informe o seu RG: ")
    data_de_nascimento = input("Informe a sua data de nascimento: ")
    area = input("Informe a sua área de atuação ou função: ")
    cod = input("Informe o seu código: ")
    funcionarioCadastrado = new_funcionario(nome, cpf, rg, data_de_nascimento, area, cod)
    cadastrarFuncionario(funcionarioCadastrado)

def demitir_funcionario() :
    cod = input("Informe o código do funcionário a ser demitido: ")
    demitirFuncionario(cod)

def exibir_funcionarios() :
    lista_funcionarios = retornarFuncionarios()
    print(lista_funcionarios)