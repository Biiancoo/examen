from funciones_examen import *



while True:
    os.system("cls")
    print("DATOS TRABAJADORES")
    print("1. Asignar sueldos aleatoriamente")
    print("2. Clasificar sueldos")
    print("3. Ver estadisticas")
    print("4. Reporte de sueldos")
    print("5. Salir")
    opciones = (1,2,3,4,5)
    opc = validar_opciones(opciones)
    if opc == 1:
        asignar_sueldos()
    elif opc ==2:
        clasificar_sueldos()
    elif opc ==3:
        ver_estaisticas()
    elif opc ==4:
        reporte_sueldos()
    else:
        print("Fnalizando programa...")
        time.sleep(1)
        print("Desarrollado por Bianco Martinez\nRUT 22.231.551-4")
        break

