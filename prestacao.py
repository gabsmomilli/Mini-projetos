valor_prestacao = input ('insira o valor da prestacao: ')
valor_com_juros = (valor_prestacao + (valor_prestacao * 0.10))
valor_com_desconto = valor_com_juros - (valor_com_juros * 0.10)
print ('Total a pagar: ' + str(valor_com_desconto) + '\nPrejuizo: ' + str(valor_prestacao - valor_com_desconto))
