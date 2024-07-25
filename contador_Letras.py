nome = str(input("informe seu nome: \n"))


if len(nome)>1 and len(nome)<= 4:
    print("seu nome e muito curto")

    if len(nome)  == 5 or len(nome) == 6:
            print("seu nome e normal")
    elif len(nome) > 6:
            print("seu nome e muito grande")

else:
    print("Digite pelo menos 2 letras")