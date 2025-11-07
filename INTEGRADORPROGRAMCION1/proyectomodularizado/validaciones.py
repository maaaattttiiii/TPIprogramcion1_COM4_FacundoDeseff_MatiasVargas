#uno de los apartados mas importantes porque las validaciones y operaciones de este archivo son las que más usamos 

#funcion para validar las entradas de datos numericos
def validar_num(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            if num < 0:
                print("Debe ser positivo.")
            else:
                return num
        except ValueError:
            print("Ingrese un número válido.")

def confirmar_accion(mensaje): # devuelve bool 
    while True:
        resp = input(f"{mensaje} (S/N): ").strip().upper()
        if resp in ("S", "N"):
            return resp == "S"
        print("Respuesta inválida. Use S o N.")

def mostrar_paises(lista):# va mostrando los paises que cumplan los criterios en los que se usen 
    if not lista:
        print("No se encontraron países.")
        return
    for p in lista:
        print(f"- {p['nombre']}")
        print(f"  Población: {p['poblacion']:,}")
        print(f"  Superficie: {p['superficie']:,} km²")
        print(f"  Continente: {p['continente']}")
        print("-" * 20)
