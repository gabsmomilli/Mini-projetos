dia = input('insira o dia do seu nascimento: ')
mes = input('insira o mes do seu nascimento: ')
ano = input('insira o ano do seu nascimento: ')
dia_hoje = input('insira o dia de hoje: ')
mes_hoje = input('insira o mes de hoje: ')
ano_hoje = input('insira o ano de hoje: ')
anos = ano_hoje - ano

if mes_hoje < mes:
    anos = anos - 1
elif mes_hoje == mes and dia_hoje < dia:
    anos = anos - 1

meses = mes_hoje - mes
dias = dia_hoje - dia

print (str('A idade em anos eh: ' + str(anos) + '\nA idade em meses eh: ' + str(anos * 12 + meses) +
           '\nA idade em dias eh: ' + str(anos * 365 + meses * 30 + dias)))
