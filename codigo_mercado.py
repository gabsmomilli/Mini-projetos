codigo = input('insira o codigo do produto: ')

if codigo == 1:
     print('alimento nao-perecivel')
elif  codigo >= 2 and codigo <= 4:
    print ('alimento perecivel')
elif codigo >= 5 and codigo <= 6:
    print('vestuario')
elif codigo == 7:
     print('higiene pessoal')
elif codigo >= 8 and codigo <= 15:
    print('limpeza e utensilios domesticos')
else:
    print('invalido')

