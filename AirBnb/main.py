import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd
import numpy as np
import math
import re

df = pd.read_csv("Montreal.csv", index_col=0, header=0)
cant_datos = df['name'].count()

# Eliminar las columnas que no se van a utilizar
df = df.drop(columns=['neighbourhood_group'])

print('Cantidad de datos:',len(df))


# El host mas solicitado
# El local mas pedido
# El host mas solicitado
# Lugar en donde mas solicitan
# Que tipos de habitación son los que mas solicitan
# Las 3 más baratas
# Las 3 más caras
# Las mas antiguas (reviews)
# Las mas nuevas (reviews)
# Las mas demandadas (reviews)
# Cantidad de review por año (no tiene sentido)
# Cantidad de dias disponibles en el año (los 3 mejores y peores)
"""
Es un recuento de listados que tiene un host específico
Básicamente, nos dice la cantidad de veces que ese host 
en particular ha usado airbnb en ese conjunto de datos. 
Entonces, si calcula_host_listings_count es 6, entonces
puede ver que host_name tiene exactamente 6 filas en ese
conjunto de datos.
"""