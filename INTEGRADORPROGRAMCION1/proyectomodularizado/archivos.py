import csv

def guardar_datos_csv(paises, ruta_archivo):
    if not paises:
        print("No hay países para guardar.")
        return
    cabeceras = ["nombre", "poblacion", "superficie", "continente"]
    try:
        with open(ruta_archivo, "w", newline="", encoding="utf-8-sig") as archivo:# modo w abre o crea archivo csv
            escritor = csv.DictWriter(archivo, fieldnames=cabeceras)# escribe lista de diccionarios en el csv
            escritor.writeheader()# primera fila con los nombres de las columnas 
            escritor.writerows(paises)#escribe los paises
        print(f"Datos guardados en '{ruta_archivo}'.")
    except Exception as e: #manejo de errores por si no se guarda correctamente el archivo
        print(f"Error al guardar CSV: {e}")

def cargar_datos_csv(ruta_archivo):
    paises = []
    try:
        with open(ruta_archivo, "r", encoding="utf-8-sig") as archivo:
            lector = csv.DictReader(archivo)#convierte las filas en diccionario
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]
                    }
                    paises.append(pais)
                except (ValueError, KeyError):
                    continue
    except FileNotFoundError:
        print(f"No se encontró '{ruta_archivo}'.")
        return None
    print(f"Se cargaron {len(paises)} países desde '{ruta_archivo}'.")
    return paises
