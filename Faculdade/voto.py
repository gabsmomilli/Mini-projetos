idade = input ("informe sua idade: ")

if idade <= 15:
    print ("voce ainda nao vota")
if idade >= 16 and idade <= 17:
    print ("voce ja pode votar, mas nao eh obrigatorio")
if idade >= 18 and idade <= 65:
    print ("voce deve votar obrigatoriamente")
if idade >= 65:
    print ("seu voto eh facultativo")