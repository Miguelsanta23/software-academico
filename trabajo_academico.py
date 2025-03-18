asignaturas = {}

def registrar_asignatura():
    nombre = input("Ingrese el nombre de la asignatura: ")
    while True:
        try:
            creditos = int(input("Ingrese la cantidad de créditos: "))
            costo_credito = float(input("Ingrese el costo por crédito: "))
            if creditos > 0 and costo_credito > 0:
                break
            else:
                print("Los valores deben ser positivos.")
        except ValueError:
            print("Ingrese valores numéricos válidos.")
    asignaturas[nombre] = {"creditos": creditos, "costo_credito": costo_credito, "estudiantes": []}

def registrar_estudiante():
    nombre_asig = input("Ingrese el nombre de la asignatura: ")
    if nombre_asig in asignaturas:
        nombre = input("Nombre del estudiante: ")
        genero = input("Género del estudiante: ")
        while True:
            try:
                edad = int(input("Edad del estudiante: "))
                estrato = int(input("Estrato del estudiante (1, 2 o 3): "))
                if edad > 0 and estrato in [1, 2, 3]:
                    break
                else:
                    print("Ingrese valores válidos.")
            except ValueError:
                print("Ingrese valores numéricos válidos.")
        descuento = {1: 0.5, 2: 0.3, 3: 0.1}.get(estrato, 0)
        costo_final = asignaturas[nombre_asig]["creditos"] * asignaturas[nombre_asig]["costo_credito"] * (1 - descuento)
        asignaturas[nombre_asig]["estudiantes"].append({"nombre": nombre, "genero": genero, "edad": edad, "estrato": estrato, "costo": costo_final})
    else:
        print("Asignatura no encontrada.")

def mostrar_informacion():
    total_recaudado = 0
    asignatura_max_ingreso = ""
    max_ingreso = 0
    suma_costos_creditos = 0
    total_creditos = 0
    descuentos_por_estrato = {1: 0, 2: 0, 3: 0}
    
    for nombre, datos in asignaturas.items():
        print(f"Asignatura: {nombre} - Estudiantes matriculados: {len(datos['estudiantes'])}")
        ingreso = sum(estudiante["costo"] for estudiante in datos["estudiantes"])
        total_recaudado += ingreso
        suma_costos_creditos += datos["costo_credito"]
        total_creditos += 1
        if ingreso > max_ingreso:
            max_ingreso = ingreso
            asignatura_max_ingreso = nombre
        for estudiante in datos["estudiantes"]:
            descuento_total = datos["creditos"] * datos["costo_credito"] * {1: 0.5, 2: 0.3, 3: 0.1}.get(estudiante["estrato"], 0)
            descuentos_por_estrato[estudiante["estrato"]] += descuento_total
    
    print(f"Asignatura con más ingresos: {asignatura_max_ingreso} - Ingreso: {max_ingreso}")
    print(f"Promedio de costos por crédito: {suma_costos_creditos / total_creditos if total_creditos > 0 else 0}")
    print(f"Total recaudado: {total_recaudado}")
    
    estrato_consulta = int(input("Ingrese un estrato para ver los descuentos otorgados: "))
    print(f"Descuentos totales por estrato {estrato_consulta}: {descuentos_por_estrato.get(estrato_consulta, 0)}")

while True:
    print("\n1. Registrar asignatura\n2. Registrar estudiante\n3. Mostrar información\n4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        registrar_asignatura()
    elif opcion == "2":
        registrar_estudiante()
    elif opcion == "3":
        mostrar_informacion()
    elif opcion == "4":
        break
    else:
        print("Opción no válida.")