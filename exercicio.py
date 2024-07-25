
num = input("informe um numero inteiro: ")

if num.isdigit():
    entrada = int(num)

    if entrada % 2 == 0:
        print(f" O número {entrada} e Par!!")
    else:
        print(f"O número {entrada} e Impar!!")
else:

    print("Você não digitou um número inteiro.")
    
