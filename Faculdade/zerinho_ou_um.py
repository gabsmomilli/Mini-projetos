Alice = input ("Escolha zerinho ou um para Alice:\n")
Beto = input ("Escolha zerinho ou um para Beto:\n")
Clara = input ("Escolha zerinho ou um para Clara:\n")

if Alice == Beto and Alice != Clara:
    print ("C")
elif Alice == Beto and Alice == Clara:
    print ("*")
elif Alice != Beto and Beto == Clara:
    print("A")
elif Alice != Beto and Alice == Clara:
    print("B")
if Alice != 0 and Alice != 1:
    print("valor invalido")
if Beto != 0 and Beto != 1:
    print("valor invalido")
if Clara != 0 and Clara != 1:
    print ("valor invalido")