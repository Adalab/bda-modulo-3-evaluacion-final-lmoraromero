#%%
#Importaciones
from src import soporte_limpieza as sp
#from sklearn.impute import IterativeImputer
#------
#Leer csv:
print("Abriendo los csv para su limpieza:")
flight = sp.leer_cvs("files", "Customer Flight Activity")
loyalty = sp.leer_cvs("files", "Customer Loyalty History")
print("----")
#Comprobamos el total de filas y columnas que tenemos en el DF
print(f"En el DataFrame 'flight tenemos un total de {flight.shape[0]} filas y {flight.shape[1]} columnas.")
print(f"En el DataFrame 'loyalty' tenemos un total de {loyalty.shape[0]} filas y {loyalty.shape[1]} columnas.")
print("----")
#Vemos los duplicados en los dos DF:
print(f"En el primer DataFrame hay {flight.duplicated().sum()} duplicados")
print(f"En el segundo DataFrame hay {loyalty.duplicated().sum()} duplicados")
sp.eliminar_duplicados(flight)
print("----")
#Unimos las columnas para poder realizar los cambios:
df_union = loyalty.merge(flight, on =["Loyalty Number"], how = "left")
#Comprobamos de nuevo los duplicados y las filas:
print(f"Después de la unión en el DataFrame final tenemos un total de {df_union.shape[0]} filas y {df_union.shape[1]} columnas.")
print(f"Finalmente el total de duplicados en el DataFrame es de {flight.duplicated().sum()}")
print("----")
#Exploramos los nulos
print("Explorando los nulos del DataFrame")
sp.explorar_nulos(df_union)
print("----")
#Modificamos el DF:
print("Realizando la limpieza del DataFrame")
#Poner en minúsculas las columnas:
sp.col_minuscula(df_union)
#Poner en minúsculas los valores del DF. Para tener más homogeneidad en el DF y para que no haya que preocuparte de mayúsculas.
sp.minusculas(df_union)
#Cambiar los nombres de las columnas para que no existan espacios y sean reemplazados por '_'
sp.modificar_columnas(df_union)
#Cambiar algunos nombres de columnas para que esten más claros:
nuevas_columnas = {"year":"flight_year", "month":"flight_month"}
sp.cambiar_nombres_columnas(df_union, nuevas_columnas)
print(f"Las columnas después de ser cambiadas son: {list(df_union.columns)}")
print("----")
#Las columnas "cancellation_year", "points_accumulated" deben ser cambiados a INT
#Por otros lado, "cancellation_month", así como "enrollment_month" y "flight_month" serán cambiados de mes por número a mes por texto.
print("Cambiando tipo de dato:")
lista_int = ["cancellation_year", "points_accumulated"]
sp.cambiar_dato(df_union, lista_int, "int")
print("----")
print("Modificando las columnas de los meses:")
months = {
    1: 'january',
    2: 'february',
    3: 'march',
    4: 'april',
    5: 'may',
    6: 'june',
    7: 'july',
    8: 'august',
    9: 'september',
    10: 'october',
    11: 'november',
    12: 'december'
}
sp.aplicar_map(df_union, 'enrollment_month', months)
sp.aplicar_map(df_union, 'cancellation_month', months)
sp.aplicar_map(df_union, 'flight_month', months)
print("----")
#Cambiar a positivo al columna salary
print("Cambiando a positivo las columnas en negativo:")
sp.negativos(df_union, 'salary')
print("----")
#Gestión de Nulos:
print("gestionando nulos:")
print("Columnas categóricas:")
sp.rellenar_nulos(df_union, "cancellation_month", "unknown")
# Vamos a usar el IterativeImputer
print("Columnas numéricas:")
sp.rellenar_mediana(df_union, 'salary')
#Imputación con IterativeImputer:
#imputer_iterative = IterativeImputer(max_iter=20, random_state=42)
#imputer_iterative_imputado = imputer_iterative.fit_transform(df_union[["salary"]])
#df_union["salary"] = imputer_iterative_imputado
print(f"Después de la imputación iterativa, tenemos:\n{df_union['salary'].isnull().sum()} valores nulos")
print("----")
print("Guardando el csv en la carpeta 'files'")
sp.guardado_csv(df_union, "files", "customer_limpio")

#------
# %%
