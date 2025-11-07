def mostrar_menu():
    print("\n--- Menú Principal: Gestión de Países ---")
    print("1. Buscar país por nombre")
    print("2. Filtrar países")
    print("3. Ordenar países")
    print("4. Mostrar estadísticas")
    print("5. Salir")
    print("6. Actualizar datos desde la API")
    return input("Seleccione una opción (1-6): ")

def mostrar_menu_filtrado():
    print("\nSubmenú: Filtrar Países")
    print("1. Por continente")
    print("2. Por rango de población")
    print("3. Por rango de superficie")
    print("4. Volver")
    return input("Seleccione una opción (1-4): ")

def mostrar_menu_ordenar():
    print("\nSubmenú: Ordenar Países")
    print("1. Por nombre")
    print("2. Por población")
    print("3. Por superficie")
    print("4. Volver")
    return input("Seleccione una opción (1-4): ")
