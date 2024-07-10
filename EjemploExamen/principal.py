import funciones as fn

alumnos = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández",
      "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
      ]

creditos_alumnos={}

while True:
    print("----menu----")
    print("0.Inicializar credito")
    print("1.Asignar creditos aleatorios")
    print("2.clasificacion de creditos")
    print("3.calcular estadisticas")
    print("4.generar reporte CSV")
    print("5.salir")

    opcion = int(input("Ingrese su opcion: "))

    if opcion == 0:
        creditos_alumnos = {alumno: 0 for alumno in alumnos} # Inicializar creditos alumnos en 0
        print("Creditos inicializados Correctamente")

    elif opcion == 1:
        if not creditos_alumnos:
            print("primero debe inicializar los creditos")
        else:
            creditos_alumnos = fn.asignar_creditos_aleatorios(alumnos)

    elif opcion == 2:
        if creditos_alumnos :
            fn.clasificar_creditos(creditos_alumnos)
        else:
            print("primero debe inicializar los creditos")
        
    elif opcion == 3:
        if creditos_alumnos:
            max_credito,min_credito,promedio_credito = fn.calcular_estadisticas(creditos_alumnos)
            if max_credito is not None:
                print("Credito maximo: $", max_credito)
                print("Credito minimo: $", min_credito)
                print("Promedio de credito: $", promedio_credito)
            else:
                print("Primero debe asignar creditos")

    elif opcion == 4:
        if creditos_alumnos:
            fn.generar_reporte(creditos_alumnos)
        else:
            print("primero debe inicializar los creditos")

    elif opcion == 5:
        print("Saliendo del sistema")
        break
    else:
        print("opcion no valida, ingrese una opcion entre 0 y 5")
