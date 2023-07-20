list = ["balão","bola", "celular"]

palavra = input("informe a palvra: ")

if palavra in list:

    print(f"a palavra {palavra} está correta ")

elif palavra not in list:

    print(f"{palavra}, não encontrada")

print(bool(palavra in list))
