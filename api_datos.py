import requests

def cargar_datos_api(url):
    lista_paises = []
    try:
        print("Obteniendo datos desde la API... (esto puede tardar un momento)")
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()
        datos_json = respuesta.json()
        print(f"Datos recibidos, {len(datos_json)} países")

        for pais_api in datos_json:
            try:
                name_data = pais_api.get("name", {})
                native_names = name_data.get("nativeName", {})
                if "spa" in native_names:
                    nombre = native_names["spa"].get("common", name_data.get("common"))
                else:
                    nombre = name_data.get("common", "Desconocido")

                pais = {
                    "nombre": nombre,
                    "poblacion": pais_api.get("population", 0),
                    "superficie": int(pais_api.get("area", 0)),
                    "continente": pais_api.get("continents", ["Indefinido"])[0]
                }
                lista_paises.append(pais)
            except (KeyError, IndexError, TypeError):
                print(f"  -> Datos incompletos para '{pais_api.get('name', {}).get('official', 'Desconocido')}'.")
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None

    print(f"Se procesaron {len(lista_paises)} países exitosamente desde la API.")
    return lista_paises
