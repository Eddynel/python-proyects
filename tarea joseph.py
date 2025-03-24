print('\n\n- Sistema bancario -')

#VARIABLES DE EJECUCION
deposito = 0
retiro = 0
saldo = 0
retiro_f = 0

#VARIABLES DE PERSONA
CICLO = True

while CICLO is True:
    consulta = int(input('\n1-consulta\n2-deposito\n3-retiro\n4-salir\n-> '))
    #*** CONSULTA ***
    if consulta == 1:
        print(f'Su saldo es de {saldo}RD$ ')     
    #*** DEPOSITO ***
    elif consulta == 2: 
        deposito = int(input('Ingresa el monto a depositar: '))
        saldo += deposito
        print(f'Ha depositado {deposito}RD$, su saldo actual es de {saldo}RD$')
    #*** RETIRO ***    
    elif consulta == 3:
        retiro = int(input('Ingresa la cantidad a retirar de su cuenta: '))
        if retiro <= saldo:
            retiro_f = retiro - deposito
            saldo -= retiro      
            print(f'Ha retirado {retiro}RD$, por lo que su saldo actual es de {saldo}RD$')
        else:
            print('Monto erroneo, no puedes retirar mas de lo que hay en la cuenta ')
    elif consulta == 4:
        print('Saliendo... ')
        break
    else:
        print('El numero introducido esta fuera del rango, vuelve a intentar... ' )
CICLO = True