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


def eliminar_movimiento(ingresos, gastos):
    print("\n---Eliminar Movimiento---")
    
    if not ingresos and not gastos:
        print("[Aviso] No hay movimientos registrados para eliminar.")
        return
        
    print("1. Eliminar un ingreso")
    print("2. Eliminar un gasto")
    
    opcion = input("\nSelecciona una opción (1-2): ")
    
    if opcion == "1":
        if not ingresos:
            print("[Aviso] No hay ingresos registrados.")
            return
        
        # Mostrar los ingresos con su índice para que el usuario sepa cuál borrar
        for i, ing in enumerate(ingresos, start=1):
            print(f"{i}. {ing}")
            
        indice = int(input("\nSelecciona el número del ingreso para eliminar: ")) - 1
        if 0 <= indice < len(ingresos):
            eliminado = ingresos.pop(indice)
            print(f"[Éxito] Ingreso eliminado correctamente.")
        else:
            print("[Error] Número fuera de rango.")
            
    elif opcion == "2":
        if not gastos:
            print("[Aviso] No hay gastos registrados.")
            return
            
        for i, gas in enumerate(gastos, start=1):
            print(f"{i}. {gas}")
            
        indice = int(input("\nSelecciona el número del gasto para eliminar: ")) - 1
        if 0 <= indice < len(gastos):
            eliminado = gastos.pop(indice)
            print(f"[Éxito] Gasto eliminado correctamente.")
        else:
            print("[Error] Número fuera de rango.")             


def generar_resumen(ingresos, gastos, meta):
    print("\n--- RESUMEN Y SEMÁFORO FINANCIERO ---")

    total_ingresos = sum(item['cantidad'] for item in ingresos)
    total_gastos = sum(item['cantidad'] for item in gastos)
    saldo = total_ingresos - total_gastos

    print(f"Total Ingresos: ${total_ingresos:.2f}")
    print(f"Total Gastos: ${total_gastos:.2f}")
    print(f"Saldo Actual: ${saldo:.2f}")
    if saldo >= meta:
        print("¡Felicidades! Has alcanzado tu meta de ahorro.")
    else:
        print("Aún no has alcanzado tu meta de ahorro.")
    
    if saldo > 0:
        print("Semáforo: VERDE (Tienes un saldo positivo)")
    elif saldo == 0:
        print("Semáforo: AMARILLO (Estás en punto de equilibrio)")
    else:
        print("Semáforo: ROJO (Cuidado, tus gastos superan tus ingresos)")


def gestionar_meta():
    print("Gestionar meta de ahorro")
    try:
        nueva_meta = float(input("Ingresa la cantidad de tu meta de ahorro ($): "))
        if nueva_meta <= 0:
            print("[Error] La meta no puede ser una cantidad negativa.")
            return None
        
        print(f"[Éxito] Meta de ahorro establecida en: ${nueva_meta:.2f}")
        return nueva_meta
    except ValueError:
        print("[Debes ingresar un número válido.")
        return None

def ver_meta(meta):
    if meta <= 0:
        print("[Aviso] No has establecido una meta de ahorro todavía.")
        print("Usa la opción 7 para establecer una.")
    else:
        print(f"\n--- TU META DE AHORRO ACTUAL ---")
        print(f"Meta establecida: ${meta:.2f}")

def main():
    # Listas para almacenar los datos del proyecto
    ingresos = []
    gastos = []
    meta_ahorro = 0
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
                eliminar_movimiento(ingresos, gastos)
            elif opcion == 6:
                generar_resumen(ingresos, gastos, meta_ahorro)
            elif opcion == 7:
                resultado_meta = gestionar_meta()
                if resultado_meta is not None:
                    meta_ahorro = resultado_meta    
            elif opcion == 8:
                ver_meta(meta_ahorro)
            elif opcion == 9:
                print("\nPrograma finalizado. ¡Hasta luego!")
                break
            else:
                print("\n[Error] La opción debe estar entre 1 y 9.")
                
        except ValueError:
            print("\n[Error] Cantidad incorrecta o carácter inválido. Ingresa un número.")

if __name__ == "__main__":
    main()