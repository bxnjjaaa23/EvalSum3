import csv
import os
import time
from random import *
acceso=1

def limpiar():
    os.system('cls')
def menu():
    while acceso==1:
        print(''' Bienvenido al menu de CatPremium
                1) Registrar pedido
                2) Listar todos los pedidos
                3) Imprimir hoja de ruta
                4) Salir del programa 
                ¿Que desea hacer? ''')
        opciones()
        break

def opciones():
    try:
        opc=int(input('Porfavor elija una opcion del 1 al 4: '))
        if opc==1:
            print('ingresando...')
            time.sleep(0.3)
            limpiar()
            n_pedido()
            sacos()
            
        elif opc==2:
            print
        elif opc==3:
            print
        elif opc==4:
            print
    except ValueError:
        print('Porfavor elija una opcion valida')

def volver():
    try:
        vuelves=int(input('¿Desea volver al menu?  si=1   2= no: '))
        if vuelves==1:
            print('Volviendo...')
            time.sleep(0.2)
            menu()
        elif vuelves==2:
            print('Saliendo...')
            acceso=2
            quit
    except ValueError:
        print('Porfavor elija una opcion valida')
        volver()

def datos():
    nombre=input('Ingrese su nombre: ')
    direccion=input('Ingrese su direccion: ')
    sector=input('Ingreses su sector: ')

def n_pedido():
    nro=randint(1,1000)
    pnro2= nro+1

def sacos():
    k_saco=int(input(''' Tenemos sacos de:
                    1) 5 kilos
                    2) 10 kilos
                    3) 20 kilos
                    4) volver al menu
                    ¿Que saco desea agregar?: '''))
    try:
        if k_saco==1:
            datos()
            cantidad5=int(input('¿Cuentos sacos desea agregar?: '))
            maspedido()
        if k_saco==2:
            datos()
            cantidad10=int(input('¿Cuentos sacos desea agregar?: '))
            maspedido()
        if k_saco==3:
            datos()
            cantidad20=int(input('¿Cuentos sacos desea agregar?: '))
            maspedido()
        if k_saco==4:
            print('Volviendo...')
            time.sleep(0.2)
            limpiar()
            menu()
    except ValueError:
        print('Elija una opcion valida')
        sacos()

def maspedido():
    try:
        otropedido=int(input('¿Desea agregar algun otro saco?  si=1   2= no: '))
        if otropedido==1:
            print('Volviendo...')
            time.sleep(0.2)
            limpiar()
            sacos()
        elif otropedido==2:
            print('Saliendo...')
            time.sleep(0.3)
            limpiar()
            menu()
    except ValueError:
        print('Porfavor elija una opcion valida')
        maspedido()

def csv_():
    with open('pedidos.csv', 'w', newline='') as archivo1_csv:
        contenido=archivo1_csv.write()




#profe de aqui en adelante me blokie se me fue como terminar de hacer el csv 
menu()
