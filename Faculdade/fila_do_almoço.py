import random
seguranca = {}
usados = {}
contR = 0
contI = 0
contV = 0
usuario = int(input('número de senha a ser gerada: '))
for i in range (usuario):
    let = 'c'
    b = random.randint(1,10000)
    b = str(b)
    c = b + let
    seguranca[c] = ('senha' + str(i +1))
print(seguranca)
fila = int(input('digite quantas pessoas na fila:'))
for x in range(fila):

    senha = str(input('Digite a senha: '))

    if senha in seguranca:
        if senha in usados:
            print('Senha repitida')
            contR = contR + 1
        else:
            usados[senha] = ('senha')
            print('Senha valida')
            contV = contV +1
    else:
        print('Senha invalida')
        contI = contI +1
print('Senhas invalidas: ',contI)
print('Senhas Repitidas: ',contR)
print('Senhas validas: ',contV)
