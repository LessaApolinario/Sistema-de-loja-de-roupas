from manipula_arquivo.manipula_arquivos import *
from manipula_arquivo.roupa import *

def cadastro_roupa() :
    cod = input("Digite o código: ")
    tipo = input("Digite o tipo: ")
    marca = input("Digite a marca: ")
    preco = input("Digite o preço: ")
    quantidade = input("Digite a quantidade: ")
    novaRoupa = new_roupa(cod, tipo, marca, preco, quantidade)
    cadastrar_roupa(novaRoupa)

def atualizacao_roupa() :
    cod = input("Digite o código da roupa desejada: ")
    tipo = input("Digite o novo tipo: ")
    marca = input("Digite a nova marca: ")
    preco = input("Digite o novo preço: ")
    quantidade = input("Digite a nova quantidade: ")
    roupaAtualizada = new_roupa(cod, tipo, marca, preco, quantidade)
    atualizar_roupa(roupaAtualizada)

def deleta_roupa() :
    cod = input("Digite o código a ser deletado: ")
    deletarRoupa(cod)

def exibir_estoque() :
    lista_roupas = retornarRoupas()
    print(lista_roupas)