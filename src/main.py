def mostrar_menu():
    print("\n" + "=" * 50)
    print("--- MENÚ PRINCIPAL: FINANZAS LIMPIAS ---")
    print("=" * 50)
    print("1. Registrar ingreso")
    print("2. Registrar gasto fijo o variable")
    print("3. Consultar movimientos")
    print("4. Modificar movimiento")
    print("5. Eliminar movimiento")
    print("6. Generar resumen y semáforo financiero")
    print("7. Registrar o calcular meta de ahorro")
    print("8. Ver monto de la meta de ahorro")
    print("9. Salir")
    print("=" * 50)




def generar_id(ingresos, gastos):
    ids = []

    for ingreso in ingresos:
        ids.append(ingreso["id"])

    for gasto in gastos:
        ids.append(gasto["id"])

    if len(ids) == 0:
        return 1

    return max(ids) + 1


def buscar_movimiento(id_movimiento, ingresos, gastos):
    for ingreso in ingresos:
        if ingreso["id"] == id_movimiento:
            return ingreso

    for gasto in gastos:
        if gasto["id"] == id_movimiento:
            return gasto

    return None


# Funciones vacías por ahora (las iremos rellenando juntos)
def registrar_ingreso(ingresos, gastos):
    print("\n--- REGISTRAR INGRESO ---")

    concepto = input("Ingresa el concepto del ingreso: ")

    try:
        cantidad = float(input("Ingresa la cantidad: $"))

        if cantidad <= 0:
            print("\n[Error] La cantidad debe ser mayor que cero.")
            return

    except ValueError:
        print("\n[Error] Debes ingresar una cantidad numérica.")
        return

    nuevo_id = generar_id(ingresos, gastos)

    ingreso = {
        "id": nuevo_id,
        "tipo": "ingreso",
        "concepto": concepto,
        "cantidad": cantidad
    }

    ingresos.append(ingreso)

    print("\nIngreso registrado correctamente.")
    print("ID asignado:", nuevo_id)

def registrar_gasto(ingresos, gastos):
    print("\n--- REGISTRAR GASTO ---")

    concepto = input("Ingresa el concepto del gasto: ")
    categoria = input("Ingresa la categoría del gasto: ")

    clasificacion = input(
        "Clasificación del gasto (fijo/variable): "
    ).lower()

    if clasificacion != "fijo" and clasificacion != "variable":
        print("\n[Error] Debes escribir 'fijo' o 'variable'.")
        return

    try:
        cantidad = float(input("Ingresa la cantidad: $"))

        if cantidad <= 0:
            print("\n[Error] La cantidad debe ser mayor que cero.")
            return

    except ValueError:
        print("\n[Error] Debes ingresar una cantidad numérica.")
        return

    nuevo_id = generar_id(ingresos, gastos)

    gasto = {
        "id": nuevo_id,
        "tipo": "gasto",
        "concepto": concepto,
        "categoria": categoria,
        "clasificacion": clasificacion,
        "cantidad": cantidad
    }

    gastos.append(gasto)

    print("\nGasto registrado correctamente.")
    print("ID asignado:", nuevo_id)

def consultar_movimientos(ingresos, gastos):
    print("\n--- MOVIMIENTOS REGISTRADOS ---")

    if len(ingresos) == 0 and len(gastos) == 0:
        print("\nNo existen movimientos registrados.")
        return

    print("\nINGRESOS")

    if len(ingresos) == 0:
        print("No hay ingresos registrados.")
    else:
        for ingreso in ingresos:
            print(
                f'ID: {ingreso["id"]} | '
                f'Concepto: {ingreso["concepto"]} | '
                f'Cantidad: ${ingreso["cantidad"]:,.2f}'
            )

    print("\nGASTOS")

    if len(gastos) == 0:
        print("No hay gastos registrados.")
    else:
        for gasto in gastos:
            print(
                f'ID: {gasto["id"]} | '
                f'Concepto: {gasto["concepto"]} | '
                f'Categoría: {gasto["categoria"]} | '
                f'Clasificación: {gasto["clasificacion"]} | '
                f'Cantidad: ${gasto["cantidad"]:,.2f}'
            )

def modificar_movimiento(ingresos, gastos):
    print("\n--- MODIFICAR MOVIMIENTO ---")

    if len(ingresos) == 0 and len(gastos) == 0:
        print("\nNo existen movimientos registrados.")
        return

    try:
        id_movimiento = int(
            input("Ingresa el ID del movimiento que deseas modificar: ")
        )

    except ValueError:
        print("\n[Error] Debes ingresar un ID numérico.")
        return

    movimiento = buscar_movimiento(
        id_movimiento,
        ingresos,
        gastos
    )

    if movimiento is None:
        print("\n[Error] No existe un movimiento con ese ID.")
        return

    print("\nMovimiento encontrado:")
    print("Tipo:", movimiento["tipo"])
    print("Concepto actual:", movimiento["concepto"])
    print(f'Cantidad actual: ${movimiento["cantidad"]:,.2f}')

    nuevo_concepto = input("Ingresa el nuevo concepto: ")

    try:
        nueva_cantidad = float(
            input("Ingresa la nueva cantidad: $")
        )

        if nueva_cantidad <= 0:
            print("\n[Error] La cantidad debe ser mayor que cero.")
            return

    except ValueError:
        print("\n[Error] Debes ingresar una cantidad numérica.")
        return

    if movimiento["tipo"] == "gasto":

        nueva_categoria = input(
            "Ingresa la nueva categoría: "
        )

        nueva_clasificacion = input(
            "Nueva clasificación (fijo/variable): "
        ).lower()

        if nueva_clasificacion != "fijo" and nueva_clasificacion != "variable":
            print("\n[Error] Debes escribir 'fijo' o 'variable'.")
            return

        movimiento["categoria"] = nueva_categoria
        movimiento["clasificacion"] = nueva_clasificacion

    movimiento["concepto"] = nuevo_concepto
    movimiento["cantidad"] = nueva_cantidad

    print("\nMovimiento modificado correctamente.")

def eliminar_movimiento():
    print("\n[Función 5] Aquí buscaremos y eliminaremos un movimiento.")

def generar_resumen():
    print("\n[Función 6] Aquí calcularemos totales, saldo, semáforo y categoría con mayor gasto.")

def gestionar_meta():
    print("\n[Función 7] Aquí capturaremos y guardaremos la meta y el ahorro mensual.")

def ver_meta():
    print("\n[Función 8] Aquí consultaremos y mostraremos el monto de la meta.")

def main():
    # Listas para almacenar los datos del proyecto
    ingresos = []
    gastos = []
    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("\nSelecciona una opción (1-9): "))
            
            if opcion == 1:
                registrar_ingreso(ingresos, gastos)
            elif opcion == 2:
                registrar_gasto(ingresos, gastos)
            elif opcion == 3:
                consultar_movimientos(ingresos, gastos)
            elif opcion == 4:
                modificar_movimiento(ingresos, gastos)
            elif opcion == 5:
                eliminar_movimiento()
            elif opcion == 6:
                generar_resumen()
            elif opcion == 7:
                gestionar_meta()
            elif opcion == 8:
                ver_meta()
            elif opcion == 9:
                print("\nPrograma finalizado. ¡Hasta luego!")
                break
            else:
                print("\n[Error] La opción debe estar entre 1 y 9.")
                
        except ValueError:
            print("\n[Error] Cantidad incorrecta o carácter inválido. Ingresa un número.")

if __name__ == "__main__":
    main()