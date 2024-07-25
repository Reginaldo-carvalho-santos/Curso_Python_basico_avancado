
frase = 'o python é uma linguagem de programação  \nmultiparadigma.'\
        '\npython foi criado por Guido Van Rossum'


i=0
while i < len(frase):

   letra_atual = frase[i]
  # print(letra_atual)

   qtd_repiticao_letra = frase.count(letra_atual)
   print(letra_atual,qtd_repiticao_letra)
   
   i+= 1
    