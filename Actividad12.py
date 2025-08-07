def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x[1]['paquetes_entregados'] < pivote[1]['paquetes_entregados']]
    iguales = [x for x in lista if x[1]['paquetes_entregados'] == pivote[1]['paquetes_entregados']]
    mayores = [x for x in lista[1:] if x[1]['paquetes_entregados'] > pivote[1]['paquetes_entregados']]
    return quick_sort(mayores) + iguales + quick_sort(menores)
repartidores = {}
cont = int(input("Ingrese cuantos repartidores trabajaron hoy: "))
for i in range(cont):
    print(f"Repartidor #{i+1}")
    while True:
        nombre = input("Ingrese el nombre del repartidor: ").upper()
        if nombre in repartidores:
            print("Error, este repartidor ya existe")
        else:
            break
    while True:
        paquetes_entregados = int(input("Ingrese la cantidad de paquetes entregados: "))
        if paquetes_entregados < 0:
            print("Error, los paquetes entregados deben de ser números positivos")
        else:
            break
    while True:
        zona = input("Ingrese la zona asignada: ")
        if not zona:
            print("Error,campo requerido")
        else:
            break
    repartidores[nombre] = {
        "paquetes_entregados": paquetes_entregados,
        "zona": zona,
        "cantidad": cont
    }
def busqueda_secuencial(lista, objetivo):
    for i in range(len(lista)):
        if lista[i][0] == objetivo:
            return i
    return None
while True:
    print("======MENÚ======")
    print("1. Listado de repartidores.")
    print("2. Buscar repartidor.")
    print("3. Salir.")
    opcion = input("Seleccione una opcion: ")
    match opcion:
        case "1":
            hola = list(repartidores.items())
            resultado = quick_sort(hola)
            for nombre, valor in resultado:
                print(f"Clave: {nombre}, Datos: {valor}")
            promedio = 0
            for clave, datos in repartidores.items():
                promedio += datos["paquetes_entregados"]
                total = promedio/datos["cantidad"]
            print(f"Promedio de paquetes entregados: {total}")
        case "2":
            print("Ingrese el nombre del repartidor que desea buscar: ")
            busqueda = input().upper()
            repa = list(repartidores.items())
            lupa = busqueda_secuencial(repa, busqueda)
            if lupa is not None:
                nom, datos = repa[lupa]
                print(f"Clave: {nom}, Datos: Paquetes encontrados:{datos['paquetes_entregados']}, Zona:{datos['zona']}")
            else:
                print("No se ha encontrado al repartidor")
        case "3":
            print("Saliendo del programa...")
            exit()