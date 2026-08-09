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

# Funciones vacías por ahora (las iremos rellenando juntos)
def registrar_ingreso():
    print("\n--- REGISTRAR NUEVO INGRESO ---")

def registrar_gasto():
    print("\n[Función 2] Aquí capturaremos la categoría, tipo y cantidad del gasto.")

def consultar_movimientos():
    print("\n[Función 3] Aquí mostraremos los movimientos registrados.")

def modificar_movimiento():
    print("\n[Función 4] Aquí buscaremos y modificaremos un movimiento.")


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
                registrar_ingreso()
            elif opcion == 2:
                registrar_gasto()
            elif opcion == 3:
                consultar_movimientos()
            elif opcion == 4:
                modificar_movimiento()
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