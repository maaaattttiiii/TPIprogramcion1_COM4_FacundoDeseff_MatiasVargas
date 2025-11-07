import requests #sirve para obtener los datos de la API

#pedimos los datos a la API con get
def cargar_datos_api(url):
    lista_paises = []
    try:
        print("Obteniendo datos desde la API... (esto puede tardar un momento)")
        respuesta = requests.get(url, timeout=10)# esto es para que si no hay respuesta en 10 seg se cancela
        respuesta.raise_for_status()
        datos_json = respuesta.json()# en esta parte la respuesta que viene en formato .json la transformamos en una lista de diccionarios
        print(f"Datos recibidos, {len(datos_json)} países")

        for pais_api in datos_json:# se recorre la lista de países que trajimos desde la API
            try:
                # se obtiene el campo "name" del país, que contiene los nombres en distintos idiomas
                name_data = pais_api.get("name", {})
                native_names = name_data.get("nativeName", {})
                #si el pais tiene nombre en español ("spa"), se usa ese como nombre principal
                if "spa" in native_names:
                    nombre = native_names["spa"].get("common", name_data.get("common"))
                else:
                    #si no hay nombre en español se usa el normal 
                    nombre = name_data.get("common", "Desconocido")
                #diccionario con los datos del pais 
                pais = {
                    "nombre": nombre,
                    "poblacion": pais_api.get("population", 0),
                    "superficie": int(pais_api.get("area", 0)),
                    "continente": pais_api.get("continents", ["Indefinido"])[0]
                }
                lista_paises.append(pais)
            #si algun pais tiene mal el formato o le faltan datos salta un aviso
            except (KeyError, IndexError, TypeError):
                print(f"  -> Datos incompletos para '{pais_api.get('name', {}).get('official', 'Desconocido')}'.")
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None
    #muestra los paises que se cargaron bien 
    print(f"Se procesaron {len(lista_paises)} países exitosamente desde la API.")
    return lista_paises
