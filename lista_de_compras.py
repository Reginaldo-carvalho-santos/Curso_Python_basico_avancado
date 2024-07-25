""" Faça uma lista de comprar com listas .
    O usuário deve ter a possibilidade de inserir, apagar, e listar valores da sua lista.
    Não permitir que o programa quebre com erros de índices inexistentes na lista. 
"""

import os

lista_compras = []

while True:

    # print("\nescolha um opção abaixo:\n ")

    op = input("\n[d]-deletar [i]-inserir [l]-listar \nInforme uma opção: ")
    print()

    if op == "d":
        # os.system("clear")
        try:
            # lista = range(len(lista_compras))
            deletar = int(input("Informe o índice na lista a ser deletado: "))
            # for item in lista:

            # if item == deletar:

            # lista_compras.pop(item)
            del lista_compras[deletar]
        except:
            print("Não foi possivel apagar esse indice..")

    elif op == "i":

        inserir = input("Adicione a lista: ")
        lista_compras.append(inserir)

    elif op == "l":
        os.system("clear")
        if len(lista_compras) == 0:
            print("Lista está vazia")

        for indice, nome in enumerate(lista_compras):
            print(f"{indice} --> {nome}")
