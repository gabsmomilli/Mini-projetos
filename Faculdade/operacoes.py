simbolo = ""
a = int(input("insira um valor de a: "))
simbolo = input("insira o simbolo: ")
b = int(input("insira um valor de b: "))

if simbolo == "+":
    print(a + b)
elif simbolo == "-":
    print (a - b)
elif simbolo == "*":
    print(a * b)
elif simbolo == "/":
    print(a / b)
else:
	print("Simbolo incorreto")
