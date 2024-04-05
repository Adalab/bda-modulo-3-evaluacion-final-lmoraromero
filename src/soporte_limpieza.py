#IMPORTACIONES

import pandas as pd
import numpy as np

# -----------------------------------------------------------------------
pd.set_option('display.max_columns', None) 
import warnings
warnings.filterwarnings("ignore")


#función para leer los CSV
def leer_cvs(carpeta, nombre_archivo):
    '''
    Abre y lee los documentos CSV. 
        Si el archivo se encuentra, lo abre en un DataFrame de pandas y lo devuelve. 
        Si el archivo no se encuentra, la función imprime un mensaje indicando que el archivo no se encontró y devuelve None.
    
    Esta función el nombre de una carpeta y el nombre de archivo como entrada y lee el archivo CSV.
    
    Args:
    carpeta(str): El nombre de la carpeta donde se encuentra el archivo
    nombre_archivo (str): El nombre del archivo csv sin la extensión.
    
    Returns:
    pd.DataFrame: Un DataFrame que contiene los datos del archivo csv, o None si el archivo no se encuentra.
    '''
    try:
        df = pd.read_csv(f'{carpeta}/{nombre_archivo}.csv')
        return df
    
    except FileNotFoundError:
        print('No se ha encontrado el archivo')
        return None
    
#función pata guardar los CSV
def guardado_csv(dataframe, carpeta, nombre_archivo):
    '''
    Guarda un DataFrame en un archivo CSV.

    Esta función toma un DataFrame, el nombre de una carpeta y un nombre de archivo como entrada y guarda el DataFrame en un archivo CSV.
    
    Args:
    dataframe (pd.DataFrame): El DataFrame que se va a guardar.
    carpeta (str.): El nombre de la carpeta donde se desee guardar
    nombre (str): El nombre del archivo CSV resultante, sin la extensión ".csv".

    Returns:
    None
        La función no devuelve ningún valor, pero imprime un mensaje indicando si el guardado fue exitoso o si ocurrió algún error.
    '''
    try:
        dataframe.to_csv(f'{carpeta}/{nombre_archivo}_limpio.csv')
        print('El dataframe ha sido guardado con éxito.')
    except Exception as e:
        print(f'Error en el guardado: {e}')

#función para cambiar a minuscula el nombre de las columnas:
def columna_min(dataframe):
    '''
    Cambia los nombres de las columnas de un DataFrame a minúsculas.

    Esta función toma un DataFrame y cambia todos los nombres de las columnas a minúsculas.

    Args:
    dataframe (pd.DataFrame): El DataFrame cuyos nombres de columnas se van a cambiar.

    Returns:
    None
        La función modifica el DataFrame directamente cambiando el formato de sus nombres de columnas a minúsculas.
    '''
    print("Nombres de las columnas antes del cambio:")
    print(dataframe.columns)

    dataframe.columns = dataframe.columns.str.lower()
    
    print("----")
    print("\nNombres de las columnas después del cambio:")
    print(dataframe.columns)

#función para vonvertir los valores del DF en minúsculas
#Aplica la función str.lower() a cada celda del DataFrame
def minusculas(dataframe):
    '''
    Convierte todos los valores del DataFrame a minúsculas.

    Args:
    df (DataFrame): El DataFrame que se desea modificar.

    Returns:
    None: La función modifica el DataFrame original inplace.
    '''
    
    # Iterar sobre cada columna
    for col in dataframe.columns:
        # Verificar si la columna contiene strings y convertirlos a minúsculas
        if dataframe[col].dtype == 'object':
            dataframe[col] = dataframe[col].str.lower()

#función para modificar los nombres de las columnas
def modificar_nombres_columnas(df):
    '''
    Cambia los nombres de las columnas en un DataFrame para reemplazar los espacios por '_'.

    Args:
    df (DataFrame): El DataFrame cuyas columnas se van a modificar.

    Returns:
    None: La función modifica el DataFrame original inplace.
    '''
    print(f"Las columnas antes de ser cambiadas son: {list(df.columns)}")
    df.rename(columns=lambda x: x.replace(' ', '_'), inplace=True)
    print("---")
    print(f"Las columnas después de ser cambiadas son: {list(df.columns)}")

#función para cambiar el nombre de las columnas
def cambiar_nombres_columnas(df, nombres_nuevos):
    '''
    Cambia los nombres de las columnas en un DataFrame.

    Args:
    df (DataFrame): El DataFrame cuyas columnas se van a renombrar.
    nombres_nuevos (dict): Un diccionario donde las claves son los nombres de las columnas actuales
                        y los valores son los nuevos nombres que deseas asignar.

    Returns:
    None: La función modifica el DataFrame original inplace.
    '''
    df.rename(columns=nombres_nuevos, inplace=True)

#función para cambiar tipo de dato
def cambiar_dato(df, columnas, nuevo_tipo):
    '''
    Cambia el tipo de dato de las columnas en un DataFrame.

    Args:
    df (DataFrame): El DataFrame en el que se van a cambiar los tipos de datos.
    columnas (str o list): Un string o lista de strings que contiene los nombres de las columnas cuyo tipo de dato se va a cambiar.
    nuevo_tipo (str): El nuevo tipo de dato al que se van a convertir las columnas (por ejemplo, 'int', 'float', 'object', etc.).

    Returns:
    None: La función modifica el DataFrame original inplace.
    '''
    print("Antes del cambio de tipo:")
    display(pd.DataFrame(df[columnas].dtypes, columns=["type"]))
    print("----")
    
    for col in columnas:
        if nuevo_tipo in ['int', 'float']:
            if nuevo_tipo == 'int':
                df[col] = pd.to_numeric(df[col].fillna(0), errors='coerce').astype(int)
            else:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        else:
            if nuevo_tipo == 'object':
                df[col] = df[col].astype(nuevo_tipo)
            else:
                print("El nuevo tipo de dato no es válido. Se mantendrá el tipo original.")
    
    print("Después del cambio de tipo, las columnas quedan:")
    display(pd.DataFrame(df[columnas].dtypes, columns=["type"]))

#función para rellenar nulos:
def rellenar_nulos(dataframe, columnas, valor):
    '''
    Rellena los valores nulos en las columnas especificadas de un DataFrame con un valor específico.

    Args:
    dataframe (DataFrame): El DataFrame en el que se van a rellenar los valores nulos.
    columnas (str o list): Un string o lista de strings que contiene los nombres de las columnas en las que se van a rellenar los valores nulos.
    valor (int, float, str, etc.): El valor con el que se van a rellenar los valores nulos.

    Returns:
    None: La función modifica el DataFrame original inplace.
    '''
    dataframe[columnas] = dataframe[columnas].fillna(valor)
    print(f"El total de nulos en las columnas {columnas} después de aplicar .fillna() es: {dataframe[columnas].isna().sum()}")

#función para ver los valores únicos
def valores_unicos(dataframe, columnas):
    '''
    Muestra los valores únicos de las columnas numéricas de un DataFrame.

    Args:
    dataframe (DataFrame): El DataFrame del que se mostrarán los valores únicos.
    columnas (str o list): Un string o lista de strings que contiene los nombres de las columnas numéricas.

    Returns:
    None: La función imprime los valores únicos para cada columna numérica.
    '''
    for col in columnas:
        print(f"La columna {col.upper()} tiene los siguientes valores únicos:")
        display(pd.DataFrame(dataframe[col].value_counts()).head())
        print("----")