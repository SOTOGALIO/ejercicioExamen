import random
import csv
def asignar_creditos_aleatorios(alumnos):
    """
    Asignar creditos aleatorios entre 50 y 200 a cada alumno
    devuelve un diccionario con los creditos asignados
    """
    creditos_alumnos = {}
    #iterar sobre cada alumno en la lista alumno
    for alumno in alumnos:
        #generar un numero entero aleatorio entre 50 y 200 para cada alumno
        credito = random.randint(50,200)
        # asignar el credito al alumno que corresponde en el diccionario
        creditos_alumnos[alumno] = credito

    print("Creditos aleatorios asignados correctamente")
    print(creditos_alumnos)

    return creditos_alumnos

def clasificar_creditos(creditos_alumnos):
    
    menor_a_100= {}
    entre_100_y_150 ={}
    mayor_a_150 = {}

    for alumno, credito in creditos_alumnos.items():
        if credito < 100:
            menor_a_100[alumno] = credito
        elif credito <= 150:
            entre_100_y_150[alumno] = credito
        else:
            mayor_a_150[alumno] = credito

        #Mostrar resultados de la clasificacion
        print("Creditos menores a 100 total",len(menor_a_100))
        for alumno, credito in menor_a_100.items():
            print(alumno,": $", credito)

        print("Creditos entre 100 y 150 total",len(entre_100_y_150))
        for alumno, credito in entre_100_y_150.items():
            print(alumno,": $", credito)
        
        print("Creditos mayores a 150 total",len(mayor_a_150))
        for alumno, credito in mayor_a_150.items():
            print(alumno,": $", credito)

def calcular_estadisticas(creditos_alumnos):
    """
    Maximo, minimo, promedio
    """
    creditos = list(creditos_alumnos.values()) #creditos = lista

    if not creditos:
        print("No se han asignado creditos")
        return None, None, None
    
    max_credito = max(creditos)
    min_credito = min(creditos)
    promedio_credito = sum(creditos) / len(creditos)

    return max_credito, min_credito, promedio_credito

def generar_reporte(creditos_alumnos):

    """
    generar un reporte en formato csv con los creditos de los alumnos
    """

    with open("reporte_creditos_alumnos.csv","w", newline="") as archivo:
        escritor = csv.writer(archivo, delimiter=",")

        #escribir encabezado
        escritor.writerow(["Nombre alumno", "credito"])

        #Escribir cada linea de datos
        for alumno, credito in creditos_alumnos.items():
            escritor.writerow([alumno,credito])

    print("reporte generado correctamente en reportes_creditos_alumnos.csv")
