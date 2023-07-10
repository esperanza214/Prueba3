import numpy
import msvcrt
import os
import time

arreglo = numpy.zeros((2.5))

while True:
    print("""\tMENÚ
        1.-Grabar
        2.-Buscar
        3.-Imprimir certificados
        4.-Salir""")
    opc=int(input("Seleccione una opción (1-4): "))
    if opc==1 or opc==2 or opc==3 or opc==4:
        break
    else:
        print("ERROR! Sólo puede ingresar números del 1 al 4")
        break
while True:
    if opc==1:
        print("GRABAR")
        num_nif=input("Ingrese su NIF: ")
        if len(num_nif)==12:
            print("NIF válido")
            #agregar funcion para grabar datos
        else:
            print("ERROR! NIF inválido")
            break
        nombre=input("Ingrese su Nombre: ")
        if len(nombre)>=8:
            print("Nombre válido")
            #agregar funcion para grabar datos
        else:
            print("ERROR! Nombre inválido")
            break
        edad=int(input("Ingrese su edad: "))
        if edad>=0:
            print("Edad válida")
            #agregar funcion para grabar datos
        else:
            print("ERROR! Edad inválida")
            break
        print("Registro")
        for x in range(2):
            print(f"Fila {x+1}", end=" ")
            for y in range(5):
                print(arreglo[x][y], end=" ")
            print()
        print("\t1 2 3 4 5")
        print("\tCOLUMNAS")
        print("\tPresione una tecla para continuar")
        msvcrt.getch()
    elif opc==2:
        print("BUSCAR")
    elif opc==3:
        print("IMPRIMIR CERTIFICADOS")
    else:
        print("") #terminar
        break