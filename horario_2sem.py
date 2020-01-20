dia = input ('Escolha um dia da semana:\n 1)SEGUNDA\n 2)TERCA\n 3)QUARTA\n 4)QUINTA\n 5)SEXTA\n 6)SABADO\n 7)DOMINGO\n')

if dia == 1:
    print('End. Software\nEnd. Software\nPlan. Estrategico\nFund. Calculo\nFund. Calculo')
elif dia == 2:
    print('Gestao de Pessoas\nGestao de Pessoas\nPlan. Estrategic\nLing. Programacao\nLing. Programacao')
elif dia == 3:
    print('Laboratorio\nLaboratorio\nLaboratorio\nLing. Programacao\nLing. Programacao')
elif dia == 4:
    print('Laboratorio\nIngles\n Ingles\nArquitetura\nArquitetura')
elif dia == 5:
    print('End. Software\nEnd. Software\nAULA LIVRE\nArquitetura\nArquitetura')
elif dia <= 6 and dia >= 7 :
    print('Aproveite, nao tem aula, mas pode ter tarefa :(')
else:
    print('Invalido')