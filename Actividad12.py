def busqueda_por_valor(lista, objetivo):
    for elemento in lista:
        if elemento == objetivo:
            return elemento
    return None
datos = [5, 8, 12, 7, 3, 9, 100]
valor_a_buscar = int(input("Ingresa el número a buscar: "))
resultado = busqueda_por_valor(datos, valor_a_buscar)
if resultado is not None:
    print(f"El valor {resultado} está en la lista.")
else:
    print(f"el valor {valor_a_buscar} no está en la lista.")
