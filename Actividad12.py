def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]
    return quick_sort(mayores) + iguales + quick_sort(menores)
repartidores = {}
cont = int(input("Ingrese cuantos repartidores trabajaron hoy: "))
for i in range(cont):
    print(f"Repartidor #{i+1}")
    while True:
        clave = input("Ingrese la clave: ")
        if clave in repartidores:
            print("Error, este repartidor ya existe")
        else:
            break
    nombre = input("Ingrese el nombre del repartidor: ")
    while True:
        paquetes_entregados = int(input("Ingrese la cantidad de paquetes entregados: "))
        if paquetes_entregados < 0:
            print("Error, los paquetes entregados deben de ser números positivos")

