import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd
import numpy as np
import math
import re

df = pd.read_excel("data.xlsx", index_col=0, header=0)
cant_datos = df['RUT.'].count()

print('\nEjercicio 2:')
# Aumento de movilización

df.sort_values(by=[
    '2. Movilización'], 
inplace=True)


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
    if(re.search(regex, input) and int(input) > 100 and int(input) < 10000000):  
        #print('F', int(input))
        #print("Digit")
        return True
    else:  
        #print("Not a Digit")
        return False

def chequearAumento(sueldo, aumento):
    return sueldo-aumento > 0

# Leemos la columna 2.1 (P) de movilización
p_movilizacion = df['2. Movilización']
a_movilizacion = df['2.1 Aumento Movilización']
sueldo_base = df['1.2 Tu  sueldo base actualmente es...']

aumento_movilizacion_filter = []
aumentos = []
sueldos_base = []
prioridades = []
aumento_movilizacion_filter_suma = 0
aumento_movilizacion_filter_cant = 0

for i in range(cant_datos):
    # Convertimos los datos a string
    valor_aumento = str(a_movilizacion[i])
    valor_sueldo = str(sueldo_base[i])

    # Eliminamos los carácteres ? . - (espacio)
    valor_aumento = eliminarCaracteres(valor_aumento)
    valor_sueldo = eliminarCaracteres(valor_sueldo)

    # Chequeamos si el valor es numerico (no porcentaje) y con sueldo menor a 10k
    if(esNumerico(valor_aumento) and esNumerico(valor_sueldo)):
        sueldo = int(valor_sueldo)
        aumento = int(valor_aumento)
        # Chequeamos si el aumento es menor al sueldo base
        if(chequearAumento(sueldo=int(valor_sueldo), aumento=int(valor_aumento))):
            aumento_movilizacion_filter.append([p_movilizacion[i], sueldo, aumento])
            aumentos.append(aumento)
            sueldos_base.append(sueldo)
            prioridades.append(p_movilizacion[i])

# Obtenemos el promedio por prioridad
prioridad = 0
suma = 0
cantidad = 0
for i in range(len(aumento_movilizacion_filter)):
    if(aumento_movilizacion_filter[i][0]>prioridad):
        print('Promedio prioridad', prioridad, 'es:', math.floor(suma/cantidad))
        prioridad = aumento_movilizacion_filter[i][0]
        suma = 0
        cantidad = 0
    suma += aumento_movilizacion_filter[i][2]
    cantidad +=1


fig = plt.figure()
ax = plt.axes(projection='3d')

# Data for a three-dimensional line
zline = np.linspace(0, 5, 1)
xline = np.linspace(0, 10000, 1)
yline = np.linspace(0, 1, 1)
ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
# Prioridades, sueldo base, aumento
zdata = prioridades
xdata = sueldos_base
ydata = aumentos

ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')
ax.set_xlabel('Sueldos base', fontsize=10)
ax.set_ylabel('Aumentos movilización', fontsize=10)
ax.set_zlabel('Prioridades', fontsize=10)
plt.title('Aumentos por movilización')
plt.show()

