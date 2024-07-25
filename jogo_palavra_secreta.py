""" faça um jogo para o usuário adivinhar qual a palavra secreta.
-Você vai propor um palavra secreta qualquer e vai dar a possibilidade para o usuário
digitar apenas uma letra, você vai conferir se a letra digitada está na palavra secreta.
- se a letra digitada estiver na palavra secreta, exiba a letra;
-se a letra digitada não estiver na palavra secreta; exiba *.
faça a contagem se tentativas do seu usuário. """

import os
import random

# Nome do arquivo que contém as palavras
nome_arquivo = "arquivo.txt"

# Abre o arquivo e lê todas as palavras
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    palavras = arquivo.readlines()

# Remove possíveis quebras de linha e espaços em branco
palavras = [palavra.strip() for palavra in palavras]

# Escolhe uma palavra aleatória da lista
palavra_secreta = random.choice(palavras)

letras_acertadas = ""
num_tentativas = 0

while True:

    letra_digitada = input("Digite uma letra: ")
    num_tentativas += 1

    if len(letra_digitada) > 1:
        print("Digite pelo menos uma letra!")
        continue

    elif letra_digitada in palavra_secreta:

        letras_acertadas += letra_digitada

    palavra_formatada = ""

    for letra_secreta in palavra_secreta:

        if letra_secreta in letras_acertadas:

            palavra_formatada += letra_secreta
        else:

            palavra_formatada += "*"
    print(" Letras acertas da palavra secreta : ", palavra_formatada)

    if palavra_formatada == palavra_secreta:
        os.system("clear")
        print("VOCÊ GANHOU! PARABÉNS")
        print("A palavra secreta era: ", palavra_secreta)
        print(f"Tentativas {num_tentativas} vezes ")
        letras_acertadas = ""
        num_tentativas = 0
