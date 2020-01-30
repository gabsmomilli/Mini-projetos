dia = input("informe o dia do seu nascimento: ")
mes = input("informe o mes do seu nascimento: ")

if dia >= 20 and mes == 1 or dia <= 18 and mes == 2:
    print("voce eh do signo de aquario")
elif dia >= 19 and mes == 2 or dia <= 20 and mes == 3:
    print("voce eh do signo de peixes")
elif dia >=21 and mes == 3 or dia <= 19 and mes == 4:
    print("voce eh do signo de aries")
elif dia >= 20 and mes == 4 or dia <= 20 and mes == 5:
    print("voce eh do signo de touro")
elif dia >= 21 and mes == 5 or dia <= 20 and mes == 6:
    print("voce eh do signo de gemeos")
elif dia >= 21 and mes == 6 or dia <= 22 and mes == 7:
    print("voce eh do signo de cancer")
elif dia >= 23 and mes == 7 or dia <= 22 and mes == 8:
    print("voce eh do signo de leao")
elif dia >= 23 and mes == 8 or dia <= 22 and mes == 9:
    print("voce eh do signo de virgem")
elif dia >= 23 and mes == 9 or dia <= 22 and mes == 10:
    print("voce eh do signo de libra")
elif dia >= 23 and mes == 10 or dia <= 21 and mes == 11:
    print("voce eh do signo de escorpiao")
elif dia >= 22 and mes == 11 or dia <= 21 and mes == 12:
    print("voce eh do signo de sagitario")
elif dia >= 22 and mes == 12 or dia <= 19 and mes == 1:
    print("voce eh do signo de capricornio")
else:
    print("dia ou mes invalidos, tente novamente")