from gerenciar_produto import *
from gerenciar_cliente import *
from gerenciar_funcionario import *
from gerenciar_venda import *

while(True) :
    print("Boa noite, bem-vindo(a) a loja Hyperclothes, em que posso ajudar?")
    print("| 1 - Cadastrar uma roupa")
    print("| 2 - Atualizar uma roupa")
    print("| 3 - Deletar uma roupa")
    print("| 4 - Exibir o estoque")
    print("| 5 - Cadastrar um cliente")
    print("| 6 - Excluir um cliente")
    print("| 7- Exibir a lista de clientes")
    print("| 8 - Cadastrar um funcionário")
    print("| 9 - Demitir um funcionário")
    print("| 10 - Exibir a lista de funcionários")
    print("| 11 - Realizar vendas")
    print("| 12 - Sobre")
    print("| 0 para sair")
    op = int(input("Digite a opção: "))

    if op == 1 :
        cadastro_roupa()
    elif op == 2 :
        atualizacao_roupa()
    elif op == 3 :
        deleta_roupa()
    elif op == 4 :
        exibir_estoque()
    elif op == 5 :
        cadastrar_cliente()
    elif op == 6 :
        excluir_cliente()
    elif op == 7 :
        exibir_clientes()
    elif op == 8 :
        cadastrar_funcionario()
    elif op == 9 :
        demitir_funcionario()
    elif op == 10 :
        exibir_funcionarios()
    elif op == 11 :
        realizar_venda()
    elif op == 12 :
        print("Desenvolvido por LESSA APOLINARIO DA SILVA NETO")
        print("lasn1@aluno.ifal.edu.br")
        print("Turma de Sistemas de Informação - Segundo período")
    elif op  == 0 :
        print("Obrigado, volte sempre!\n")
        break
    else:
        print("Por gentileza, digite uma opção válida!\n")