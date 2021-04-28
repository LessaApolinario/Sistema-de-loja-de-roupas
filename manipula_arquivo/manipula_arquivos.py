import json
def sobrescrever_dados(caminho, dados_list) :
    arquivo = open(caminho, 'w')
    json.dump(dados_list, arquivo)
    arquivo.close()

def recuperar_dados_dict(caminho) :
    arquivo = open(caminho, 'r')
    dados_dict = json.load(arquivo)
    return dados_dict