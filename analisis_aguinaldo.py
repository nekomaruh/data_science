import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd
import numpy as np
import math
import re

df = pd.read_excel("data.xlsx", index_col=0, header=0)
cant_datos = df['RUT.'].count()

print('\nEjercicio aguinaldo:')

# Aumento de aguinaldos

df.sort_values(by=[
    '5. Aguinaldo Septiembre',
    '6. Aguinaldo Navidad'], 
inplace=True)

septiembre = df['5. Aguinaldo Septiembre']
navidad = df['6. Aguinaldo Navidad']
prioridad_aguinaldos = []


for i in range(cant_datos):
    promedio = (septiembre[i] + navidad[i] / 2)
    prioridad_aguinaldos.append(int(promedio))

#print(prioridad_aguinaldos)

# Eliminar puntos y signos del input
def eliminarCaracteres(input):
    input = input.replace(".","")
    input = input.replace("$","")
    input = input.replace("-","")
    input = input.replace(" ","")
    #print('R:', input)
    return input

# Expresión regular para identificar dígitos incluyendo decimales
def esNumerico(input):
    regex = '^[0-9]+$'
    if(re.search(regex, input) and int(input)<7000000):  
        #print('F', int(input))
        #print("Digit")
        return True
    else:  
        #print("Not a Digit")
        return False

def esPorcentaje(input):
    return input <= 100


# Leemos la columna 2.1 (P) de movilización
prioridades = df['1. Sueldo Base']
sueldos_base = df['1.2 Tu  sueldo base actualmente es...']
aumentos = df['1.3 Aumento Sueldo Base']

aumento_sueldo_filter = []
aumentos_filter = []
sueldos_base_filter = []
prioridades_filter = []
filter_suma = 0
filter_cant = 0

for i in range(cant_datos):
    # Convertimos los datos a string
    valor_aumento = str(aumentos[i])
    valor_sueldo = str(sueldos_base[i])

    # Eliminamos los carácteres ? . - (espacio)
    valor_aumento = eliminarCaracteres(valor_aumento)
    valor_sueldo = eliminarCaracteres(valor_sueldo)

    # Chequeamos si el valor es numerico (no porcentaje) y con sueldo menor a 10k
    if(esNumerico(valor_aumento) and esNumerico(valor_sueldo)):
        sueldo = int(valor_sueldo)
        aumento = int(valor_aumento)
        # Chequeamos si el aumento es menor al sueldo base
        if(esPorcentaje(input=int(aumento))):
            aumento_sueldo_filter.append([prioridades[i], sueldo, aumento])
            aumentos_filter.append(aumento)
            sueldos_base_filter.append(sueldo)
            prioridades_filter.append(prioridades[i])

"""
for i in range(len(aumento_sueldo_filter)):
    print(aumento_sueldo_filter[i])
    print(aumentos_filter[i])
    print(sueldos_base_filter[i])
    print(prioridades_filter[i])
"""
"""
# Obtenemos el promedio por prioridad
prioridad = 1
suma = 0
cantidad = 0
for i in range(len(aumento_sueldo_filter)):
    if(aumento_sueldo_filter[i][0]>prioridad):
        if(cantidad == 0):
            continue
        print('Promedio prioridad', prioridad, 'es:', math.floor(suma/cantidad))
        prioridad = aumento_sueldo_filter[i][0]
        suma = 0
        cantidad = 0
    suma += aumento_sueldo_filter[i][]
    cantidad +=1
"""

fig = plt.figure()
ax = plt.axes(projection='3d')

# Data for a three-dimensional line
zline = np.linspace(0, 5, 1)
xline = np.linspace(0, 10000, 1)
yline = np.linspace(0, 1, 1)
ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
# Prioridades, sueldo base, aumento
zdata = prioridades_filter
xdata = sueldos_base_filter
ydata = aumentos_filter

ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')
ax.set_xlabel('Sueldos base', fontsize=10)
ax.set_ylabel('Porcentaje de aumentos', fontsize=10)
ax.set_zlabel('Prioridades', fontsize=10)
plt.title('Aumentos por sueldos base')
plt.show()

