# **EVALUACIÓN FINAL MÓDULO 3**

### **INTRODUCCIÓN**

Este repositorio contiene un proyecto de exploración y análisis de datos que forma parte de la evaluación final del Módulo 3 en el bootcamp de Data Analyst de ADALAB. Su objetivo es aplicar los conocimientos adquiridos en el análisis exploratorio de datos, así como su limpieza y su visualización, además de realizar pruebas estadísticas para evaluar hipótesis específicas.

### **DOCUMENTACIÓN**

El repositorio está compuesto por tres carpetas:

1. La carpeta 'files' que contiene los archivos en formato .csv:
    - 'Customer Flight Activity': Contiene información relacionada con las reservas de vuelos de clientes y su participación en el programa de fidelización.
    - 'Customer Loyalty History': Contiene información más detallada sobre los clientes y su participación en el programa de fidelización.
    - 'customer': Este es el archivo generado después de la limpieza de los datos para poder ser usado en el análisis posterior.

2. La carpeta 'src' contiene un único archivo, 'soporte_limpieza' que contiene funciones que ayudan en la limpieza y análisis de los datos. Estas funciones son:
    - **Gestión de .csv**:
        - leer_csv: Abre y lee los documentos CSV.
        - guardado_csv: Guarda un DataFrame en un archivo CSV.
    - **Gestión de columnas**:
        - modificar_columnas: Cambia los nombres de las columnas reemplazando los espacios por guiones bajos.
        - cambiar_nombres_columnas: Cambia los nombres de las columnas según un diccionario de mapeo.
        - col_minuscula: Pone en minúscula los nombres de las columnas del DataFrame.
        - minusculas: Convierte todos los valores del DataFrame a minúsculas.
        - eliminar_columnas: Elimina columnas de un DataFrame.
        - copiar_columna: Realiza una copia de una columna en un DataFrame de pandas.
        - mostrar_tipos: Muestra el dtype de cada columna del DataFrame.
        - valores_unicos: Muestra los valores únicos de las columnas numéricas de un DataFrame.
        - describir_columnas: Muestra las estadísticas descriptivas de las columnas especificadas de un DataFrame.
    - **Gestión de duplicados**:
        - explorar_duplicados: Muestra la cantidad de duplicados en el conjunto de datos.
        - eliminar_duplicados: Elimina los duplicados de un DataFrame.
    - **Gestión de nulos**:
        - explorar_nulos: Muestra el porcentaje de valores nulos para cada columna.
        - rellenar_nulos: Rellena los valores nulos en las columnas especificadas con un valor específico.
        - rellenar_mediana: Rellena los valores nulos en las columnas especificadas con la mediana de esas columnas.
        - rellenar_media: Rellena los valores nulos en las columnas especificadas con la media de esas columnas.
    - **Manipulación de datos**:
        - cambiar_dato: Cambia el tipo de dato de las columnas en un DataFrame.
        - negativos: Verifica si hay números negativos en una columna de un DataFrame y, en caso afirmativo, los convierte en su valor absoluto.
    - **Pruebas estadísticas**:
        - test_shapiro: Realiza el test de Shapiro-Wilk para determinar si una muestra sigue una distribución normal.
        - mann_whitney: Realiza el test de Mann-Whitney para comparar dos muestras independientes.

3. La carpeta 'notebooks' que contiene:
    - Archivo 'evaluación_final': documento .ipynb donde se explica el proceso de limpieza de los datos con comentarios y se realiza además un análisis profundo de los datos. También se encuentra la visualización de los datos mediante gráficas y la realización de las pruebas estadísticas para evaluar hipótesis.

4. Fuera de las carpetas encontramos el archivo *'main.py'*, que contiene la automatización del proceso de limpieza de los datos.
    **IMPORTANTE**❗En el archivo *'evaluación_final'* se realiza la imputación de los nulos de la columna 'salary' mediante IterativeImputer. Por problemas de compatibilidad, en el archivo de automatización del código se imputa la media. Aún así el IterativeImputer se encuentra comentado en caso de que en otros equipos funcione.

### *FASES DEL PROYECTO*

**FASE 1: Exploración y Limpieza de Datos.**
Se lleva a cabo una exploración inicial de los datos para identificar posibles problemas, como valores nulos, atípicos o datos faltantes en las columnas relevantes. Luego, se lleva a cabo la limpieza de datos para asegurar que estén completos y coherentes para el análisis posterior.

**FASE 2: Visualización de Datos.**
Se utiliza una variedad de herramientas de visualización para responder a preguntas específicas sobre los datos. Se exploran patrones, tendencias y relaciones entre variables utilizando gráficos y visualizaciones adecuadas. Las preguntas planteadas son:

- ¿Cómo se distribuye la cantidad de vuelos reservados por mes durante el año?
- ¿Existe una relación entre la distancia de los vuelos y los puntos acumulados por los clientes?
- ¿Cuál es la distribución de los clientes por provincia o estado?
- ¿Cómo se compara el salario promedio entre los diferentes niveles educativos de los clientes?
- ¿Cuál es la proporción de clientes con diferentes tipos de tarjetas de fidelidad?
- ¿Cómo se distribuyen los clientes según su estado civil y género?


**FASE 3: Prueba Estadística**
Se realiza una prueba de A/B testing para determinar si existe una diferencia significativa en el número de vuelos reservados entre los diferentes niveles educativos.

    
        
        
