sexo = str(input('Digite (F) se seu sexo for Feminino ou (M) para masculino: '))

if sexo == 'F':
    print('Sexo Feminino confirmado')
elif sexo == 'M':
    print('Sexo Masculino confirmado')
elif sexo != 'M' or 'F':
    print('Sexo incorreto')