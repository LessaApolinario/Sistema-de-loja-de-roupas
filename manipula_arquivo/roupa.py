from manipula_arquivo.manipula_arquivos import *

caminho_roupa = "json/dados_roupa.json"
lista_roupas = list(recuperar_dados_dict(caminho_roupa))

def new_roupa(cod, tipo, marca, preco, quantidade) :
    return {
        "cod" : cod,
        "tipo" : tipo,
        "marca" : marca,
        "preco" : float(preco),
        "quantidade" : int(quantidade)
    }

def salvar_roupas() :
    sobrescrever_dados(caminho_roupa, lista_roupas)

def cadastrar_roupa(roupa) :
    lista_roupas.append(roupa)
    print("Roupa cadastrada com sucesso!")
    salvar_roupas()

def atualizar_roupa(roupa) :
    i = 0
    for l in lista_roupas :
        if l["cod"] == roupa["cod"] :
            lista_roupas[i] = roupa
        i += 1
    print("Roupa atualizada com sucesso!")
    salvar_roupas()
    
def deletarRoupa(cod) :
    i = 0
    for l in lista_roupas :
        if l["cod"] == cod :
            del lista_roupas[i]
        i += 1
    print("Roupa deletada com sucesso!")
    salvar_roupas()

def retornarRoupas() :
    print("Lista de roupas: ")
    return lista_roupas