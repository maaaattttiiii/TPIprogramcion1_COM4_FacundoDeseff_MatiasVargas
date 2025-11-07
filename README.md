# TPIprogramcion1_COM4_FacundoDeseff_MatiasVargas
# 🌎 Proyecto Integrador de Programación 1

## 📘 Descripción general
Este proyecto tiene como objetivo **obtener, procesar y analizar información de países** utilizando una **API pública**.  
El sistema está **modularizado** para mantener el código ordenado y facilitar su mantenimiento, siguiendo buenas prácticas de programación en Python.


## 🧩 Estructura del proyecto
│
├── main.py # Programa principal
├── api.py # Módulo encargado de conectarse a la API y cargar los datos
├── archivos.py # Módulo para leer y escribir datos en archivos locales (CSV, TXT, etc.)
├── operaciones.py # Módulo que realiza cálculos o filtrados sobre los datos
├── menu.py # Módulo con las opciones del menú principal e interacción con el usuario
├── validaciones.py # Funciones auxiliares de validación, formato o manejo de errores
└── README.md # Documento con la descripción general del proyecto


## ⚙️ Funcionamiento del módulo `api.py`

El archivo `api.py` contiene la función principal:
def cargar_datos_api(url):

**Descripción:**

Realiza una solicitud a la URL de la API para obtener los datos en formato JSON.

Procesa cada país y extrae la siguiente información:

- Nombre (si se puede en español)

- Población

- Superficie

- Continente

Devuelve una lista de diccionarios con los países y sus datos listos para ser utilizados por otros módulos.

**Manejo de errores:**

Si ocurre un error de conexión o la API no responde, el sistema muestra un mensaje y retorna None.

Si un país tiene datos incompletos, se muestra una advertencia pero el programa continúa procesando los demás.

**Fuente de datos (API utilizada)**

Se utiliza la API pública REST Countries, que provee información de todos los países del mundo:

https://restcountries.com/v3.1/all

**Cómo usar el programa**

**1-Hay que tener Python 3.10 o superior instalado.**

**2-Abrí la terminal en la carpeta del proyecto:**

cd C:\INTEGRADORPROGRAMCION1


**3.Ejecutá el archivo principal**
python main.py


**4. El sistema se conectará a la API y descargará los datos de los países.
Luego se mostrará un menú interactivo con distintas opciones, por ejemplo:**


==== MENÚ PRINCIPAL ====
1. Listar todos los países
2. Buscar país por nombre
3. Mostrar país con mayor población
4. Mostrar país con mayor superficie
5. Guardar datos en archivo CSV
6. Salir



**AUTORES**

MATIAS VARGAS Y FACUNDO DESEFF

-Proyecto integrador de paises para la materia Programación 1

