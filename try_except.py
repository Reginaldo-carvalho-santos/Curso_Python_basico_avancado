numero = input("Vou dobrar o número que você digitar: ")

try:
    numero_float = float(numero)
    print('FLOAT: ', numero_float)
    print(f'O dobro de {numero_float} é {numero_float * 2}')
except :
    print("Não é um número.")
