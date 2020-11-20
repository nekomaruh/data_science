import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd
import numpy as np
import math
import re

df = pd.read_csv("Montreal.csv", index_col=0, header=0)
cant_datos = df['name'].count()
print(cant_datos)

# Eliminar las columnas que no se van a utilizar
df = df.drop(columns=['neighbourhood_group'])

print('\nCantidad de datos:',len(df),'\n')

print('Top 5 hosts más solicitados:')
print(df['host_name'].value_counts()[0:5],'\n')

print('Top 5 locales más solicitados')
print(df['name'].value_counts()[0:5],'\n')

print('Top 5 barrios más solicitados')
print(df['neighbourhood'].value_counts()[0:5],'\n')

print('Solicitudes por barrio')
print(df['neighbourhood'].value_counts(),'\n')

print('Tipos de habitación solicitadas')
print(df['room_type'].value_counts(),'\n')

print('Las habitaciones mas baratas')
df1 = df.nsmallest(5, columns=['price'])
hc_nom = df1['name'].tolist()
hc_pre = df1['price'].tolist()

for i in range(len(hc_nom)):
    print('$', hc_pre[i], hc_nom[i])

print('\nLas habitaciones mas caras')
df1 = df.nlargest(5, columns=['price'])
hc_nom = df1['name'].tolist()
hc_pre = df1['price'].tolist()
for i in range(len(hc_nom)):
    print('$', hc_pre[i], hc_nom[i])

print("\n --- Datos de la ciudad de Montréal ---")

#print('\nSuma de reviews')
#print(df["number_of_reviews"].sum())

print('\nPromedio de reviews por mes')
print(df["reviews_per_month"].mean(), 'reviews')

print('\nPromedio de arriendos de locales por host')
print(df["calculated_host_listings_count"].mean(), 'arriendos por cada host')

print('\nPromedio de días disponibles de arriendos anual')
print(df["availability_365"].mean(), 'días')

print('\nGanancias totales')
print('$', df["price"].sum(), 'dólares')


# El host mas solicitado
# El local mas pedido
# Barrio en donde mas solicitan
# Que tipos de habitación son los que mas solicitan
# Las 3 más baratas
# Las 3 más caras
# Las mas antiguas (reviews)
# Las mas nuevas (reviews)
# Las mas demandadas (reviews)
# Cantidad de review por año (no tiene sentido)
# Cantidad de dias disponibles en el año (los 3 mejores y peores)
# Reviews por año
# Cuales son las habitaciones que se reservan por un tiempo mas largo
# Promedio de reviews por mes

"""
calculated_host_listings_count: Es un recuento de listados que tiene un host específico
Básicamente, nos dice la cantidad de veces que ese host 
en particular ha usado airbnb en ese conjunto de datos. 
Entonces, si calcula_host_listings_count es 6, entonces
puede ver que host_name tiene exactamente 6 filas en ese
conjunto de datos.
"""

"""
Mínima cantidad de casas arrendadas por tipo
Máxima cantidad de casas arrendadas por tipo

Precios como referencia
"""

#def getPFRT(dataframe, room_type):
#    df_r = dataframe.loc[dataframe['room_type'] == room_type]
#    p = df_r["price"]
#    return p.mean(), p.std(), p.count()

def showBoxPlot(dataframe, price_range):
    df_bp = dataframe[["room_type", "price"]]
    if(price_range != -1):
        df_bp = df_bp[df.price <= price_range]
    boxp = df_bp.boxplot(column="price", by="room_type", grid = True, vert=False, showmeans=True)

    boxp.set_yticklabels(['%s\n$n$=%d'%(k, len(v)) for k, v in df_bp.groupby('room_type')])
    boxp.set_title(None)
    boxp.set_xlabel('Precios')
    boxp.set_ylabel('Tipo de habitaciones')
    plt.subplots_adjust(left=0.2, bottom=0.2, right=0.9, top=0.8, wspace=None, hspace=None)
    plt.show()

# Muestra todos los datos
showBoxPlot(df, -1)

# Muestra los tados por rango de precio
showBoxPlot(df, 2000)
showBoxPlot(df, 1500)
showBoxPlot(df, 400)

