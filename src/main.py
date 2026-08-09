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
    print("\n[Función 1] Aquí capturaremos el concepto y cantidad del ingreso.")

def registrar_gasto():
    print("\n[Función 2] Aquí capturaremos la categoría, tipo y cantidad del gasto.")

def consultar_movimientos():
    print("\n[Función 3] Aquí mostraremos los movimientos registrados.")

def modificar_movimiento():
    print("\n[Función 4] Aquí buscaremos y modificaremos un movimiento.")

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
                registrar_ingreso()
            elif opcion == 2:
                registrar_gasto()
            elif opcion == 3:
                consultar_movimientos()
            elif opcion == 4:
                modificar_movimiento()
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