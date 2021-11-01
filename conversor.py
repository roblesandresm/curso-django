def solicitarDivisas():
    menu ="""
    Bienvenido al conversor de monedas 
    1 - Pesos Mexicanos
    2 - Pesos Colombianos 
    3 - Dolares    
    : """

    #desdeDivisa = input('Elige la Divisa (1 - 3): \n1 Pesos Mexicanos \n2 Pesos Colombianos \n3 Dolares \n: ')
    desdeDivisa = input(menu)
    desdeDivisaCorrecta = False
    aDivisaCorrecta     = False

    if validaDivisa(desdeDivisa):
        print(desdeDivisa)
        nombreDesdeDivisa = obtieneNombreDivisa(desdeDivisa)
        print(nombreDesdeDivisa)
        cantidadDesdeDivisa = input(f'¿Cuántos {nombreDesdeDivisa} tienes?: ')

        if validaImporteDivisa(cantidadDesdeDivisa):
            desdeDivisaCorrecta = True
        else:
            print(f'El importe en {nombreDesdeDivisa} es incorrecto')
    else:
        print('Divisa incorrecta')


    if desdeDivisaCorrecta:
        aDivisa = input('Desde la Divisa: \n1 pesos Mexicanos \n2 Pesos Colombianos \n3 Dolares \n: ')
        if validaDivisa(aDivisa):
            nombreADivisa = obtieneNombreDivisa(aDivisa)
            aDivisaCorrecta = True
        else:
            print('Divisa incorrecta')

    if nombreDesdeDivisa == nombreADivisa:
        print('Las Divisas no pueden ser iguales.')
    else:
        if aDivisaCorrecta:
            calcularTipoCambio(nombreDesdeDivisa,cantidadDesdeDivisa,nombreADivisa)

def obtieneNombreDivisa(desdeDivisa):
    nombreDivisa = ''
    if desdeDivisa == "1":
        nombreDivisa = 'Pesos Mexicanos'
    elif desdeDivisa == "2":
        nombreDivisa = 'Pesos Colombianos'
    elif desdeDivisa == "3":
        nombreDivisa = 'Dólares Estadounidense'

    return nombreDivisa

def validaDivisa(divisa):
    divisaCorrecta = False

    if divisa.isnumeric():
        divisa = int(divisa)
        if divisa >= 1 and divisa <= 3:
            divisaCorrecta = True

    return divisaCorrecta

def validaImporteDivisa(importe):
    importeCorrecto = False

    if importe.isnumeric():
        divisa = float(importe)
        if divisa >= 0:
            importeCorrecto = True

    return importeCorrecto

def calcularTipoCambio(nombreDesdeDivisa,cantidadDesdeDivisa,nombreADivisa):
    cantidadDesdeDivisa = int(cantidadDesdeDivisa)
    totalImporte = 0
    tipoCambioPesoColombiano    = 3771.50
    tipoCambioPesoMexicano      = 20.21
    tipoCambioMexAColom         = 187.13

    if nombreDesdeDivisa == 'Dólares Estadounidense' and nombreADivisa == 'Pesos Colombianos':
        totalImporte = round(cantidadDesdeDivisa * tipoCambioPesoColombiano)
    elif nombreDesdeDivisa == 'Dólares Estadounidense' and nombreADivisa == 'Pesos Mexicanos':
        totalImporte = round(cantidadDesdeDivisa * tipoCambioPesoMexicano,2)
    elif nombreDesdeDivisa == 'Pesos Mexicanos' and nombreADivisa == 'Dólares Estadounidense':
        totalImporte = round(cantidadDesdeDivisa / tipoCambioPesoMexicano, 2)
    elif nombreDesdeDivisa == 'Pesos Colombianos' and nombreADivisa == 'Dólares Estadounidense':
        totalImporte = round(cantidadDesdeDivisa / tipoCambioPesoColombiano, 2)
    elif nombreDesdeDivisa == 'Pesos Colombianos' and nombreADivisa == 'Pesos Mexicanos':
        totalImporte = round(cantidadDesdeDivisa / tipoCambioMexAColom, 2)
    elif nombreDesdeDivisa == 'Pesos Mexicanos' and nombreADivisa == 'Pesos Colombianos':
        totalImporte = round(cantidadDesdeDivisa * tipoCambioMexAColom, 2)

    print(f'{cantidadDesdeDivisa} {nombreDesdeDivisa} equivale a  {totalImporte} {nombreADivisa}')

solicitarDivisas()
