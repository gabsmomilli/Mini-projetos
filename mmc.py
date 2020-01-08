n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))

if n1 > n2:
    a = n1
else:
    a = n2

for i in range(a):
    x = n1 * i
    if (x % n2) == 0:
        mmc = x

print(mmc)