from validaciones import validar_num, mostrar_paises
from menu import mostrar_menu_filtrado, mostrar_menu_ordenar

def buscar_pais_por_nombre(paises, nombre):
    resultados = [p for p in paises if nombre.lower() in p["nombre"].lower()]
    mostrar_paises(resultados)

def filtrar_paises(paises):
    while True:
        opcion = mostrar_menu_filtrado()
        resultados = [] #se crea lista vacia para que no salte errores
        if opcion == "1":
            cont = input("Ingrese continente: ").strip()
            resultados = [p for p in paises if cont.lower() == p["continente"].lower()]
        elif opcion == "2":
            min_p = validar_num("Población mínima: ")
            max_p = validar_num("Población máxima: ")
            resultados = [p for p in paises if min_p <= p["poblacion"] <= max_p]
        elif opcion == "3":
            min_s = validar_num("Superficie mínima: ")
            max_s = validar_num("Superficie máxima: ")
            resultados = [p for p in paises if min_s <= p["superficie"] <= max_s]
        elif opcion == "4":
            break
        mostrar_paises(resultados)#para imprimir resultados

def ordenar_paises(paises):
    #en las opciones usamos lambda para los criterios del sorted
    while True:
        opc = mostrar_menu_ordenar()
        if opc == "1":
            mostrar_paises(sorted(paises, key=lambda x: x["nombre"].lower()))#sorted ordena segun criterios
        elif opc == "2":
            mostrar_paises(sorted(paises, key=lambda x: x["poblacion"]))
        elif opc == "3":
            orden = input("Ascendente (A) o Descendente (D): ").upper()
            mostrar_paises(sorted(paises, key=lambda x: x["superficie"], reverse=(orden == "D")))
        elif opc == "4":
            break

def mostrar_estadisticas(paises):
    if not paises:
        print("No hay datos cargados.")
        return
    pais_mas_poblado = max(paises, key=lambda x: x["poblacion"])
    pais_menos_poblado = min(paises, key=lambda x: x["poblacion"])
    pais_mas_grande = max(paises, key=lambda x: x["superficie"])
    pais_mas_chico = min(paises, key=lambda x: x["superficie"])
    prom_poblacion = sum(p["poblacion"] for p in paises)/len(paises)
    prom_superficie = sum(p["superficie"] for p in paises if p["superficie"]>0)/len([p for p in paises if p["superficie"]>0])
    print(f"\nTotal de países: {len(paises)}")
    print(f"País más poblado: {pais_mas_poblado['nombre']} ({pais_mas_poblado['poblacion']:,} hab.)")
    print(f"País menos poblado: {pais_menos_poblado['nombre']} ({pais_menos_poblado['poblacion']:,} hab.)")
    print(f"País más grande: {pais_mas_grande['nombre']} ({pais_mas_grande['superficie']:,} km2)")
    print(f"País más chico: {pais_mas_chico['nombre']} ({pais_mas_chico['superficie']:,} km2)")
    print(f"Promedio de población: {prom_poblacion:,.0f} hab.")
    print(f"Promedio de superficie: {prom_superficie:,.0f} km2")
    continentes = {}
    for pais in paises:
        cont = pais["continente"]
        if cont not in continentes:
            continentes[cont] = {"poblacion_total":0,"superficie_total":0,"cantidad":0}
        continentes[cont]["poblacion_total"]+=pais["poblacion"]
        continentes[cont]["superficie_total"]+=pais["superficie"]
        continentes[cont]["cantidad"]+=1
    for cont, datos in continentes.items():
        pobl_prom = datos["poblacion_total"]/datos["cantidad"]
        sup_prom = datos["superficie_total"]/datos["cantidad"]
        print(f"\n{cont}:")
        print(f"  Países: {datos['cantidad']}")
        print(f"  Promedio población: {pobl_prom:,.0f} hab.")
        print(f"  Promedio superficie: {sup_prom:,.0f} km2")
