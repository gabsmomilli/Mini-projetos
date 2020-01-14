
while True:
    valor = float(input ('Insira o preço do produto: '))
    condicao = input ('Insira a condicao de pagamento: ')
    if condicao == "dinheiro" or condicao == "cheque":
        print('A vista em dinheiro ou cheque, recebe 10% de desconto.\nValor a pagar é de: ' + str(valor - (valor * 0.10)))
        break
    elif condicao == "cartao" or condicao == "credito":
        print('A vista no cartao de credito, recebe 5% de desconto.\nValor a pagar é de: ' + str(valor - (valor * 0.05)))
        break
    elif condicao == "parcelar em 2x":
        print('Duas vezes, preco normal da etiqueta.\nValor a pagar é de: ' + str(valor))
        break
    elif condicao == "parcelar 3x":
        print('Tres vezes, preco normal da etiqueta mais juros de 10%.\nValor a pagar é de: ' + str(valor + (valor * 0.10)))
        break
    else:
        print('Invalido')
