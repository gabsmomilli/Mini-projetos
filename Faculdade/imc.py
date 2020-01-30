peso = input("informe o seu peso: ")
altura = input("imforme a sua altura: ")

imc = (peso / (altura * altura))
print("seu imc eh de " + imc)
if imc < 18.5:
    print("vc esta abaixo do peso ideal")
elif imc >= 18.5 and imc < 25:
    print ("vc esta no peso normal")
elif imc >= 25 and imc < 30:
    print("vc esta acima do seu peso ideal")
elif imc >= 30:
    print("vc esta obeso")
else:
    print("informe outro valor")
