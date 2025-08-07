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

print("======MENÚ======")
print("1. Listado de repartidores.")
print("2. Buscar repartidor.")
opcion = input("Seleccione una opcion: ")
while True:
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
            break