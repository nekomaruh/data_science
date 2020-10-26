import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd
import numpy as np
import math
import re

df = pd.read_excel("data.xlsx", index_col=0, header=0)
cant_datos = df['RUT.'].count()

print('\nEjercicio colacion:\n')

# Aumento de colacion

df.sort_values(by=[
    '3. Colación'], 
inplace=True)


# Eliminar puntos y signos del input
def eliminarCaracteres(input):
    input = input.replace(".","")
    input = input.replace("$","")
    input = input.replace("-","")
    input = input.replace(" ","")
    #print('R:', input)
    return input

def printRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90, 
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL", 
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    result = ''
    while number:
        div = number // num[i]
        number %= num[i]
 
        while div:
            print(sym[i], end = "")
            result += sym[i]
            div -= 1
        i -= 1
    return result

# Expresión regular para identificar dígitos incluyendo decimales
def esNumerico(input):
    regex = '^[0-9]+$'
    if(re.search(regex, input)):  
        return True
    else:  
        #print("Not a Digit")
        return False

def transformarRegiones(input):
    input = str(input).upper()
    
    """
    if ('METRO' and 'SANTIAGO' and 'CASA MATRIZ' and 'METROPOLITANA') in input:
        return 'RM'

    """
    return input
    """
    if esNumerico(input):
        return str(printRoman(int(input)))
    elif ('RM' or 'METRO') in input:
        return 'RM'
    else:
        return input
    """





# Leemos la columna 2.1 (P) de movilización
prioridades = df['3. Colación']
colaciones = df['3.1 Aumento Colación']
regiones = df['REGIÓN']
contratos = df['14. Duración del Contrato Colectivo']
sueldos_base = df['1.2 Tu  sueldo base actualmente es...']

solo_colaciones_filter = []
prioridades_filter = []
colaciones_filter = []
sueldos_base_filter = []
regiones_filter = []
contratos_filter = []




for i in range(cant_datos):
    # Convertimos los datos a string
    colacion = str(colaciones[i])
    sueldo = str(sueldos_base[i])

    # Eliminamos los carácteres ? . - (espacio)
    colacion = eliminarCaracteres(colacion)
    sueldo = eliminarCaracteres(sueldo)

    # Solo calculamos aguinaldos
    if(esNumerico(colacion)):
        solo_colacion = int(colacion)
        if(solo_colacion  > 100 and solo_colacion  < 10000):
            solo_colaciones_filter.append(solo_colacion )

    # Chequeamos si el valor es numerico (no porcentaje) y con aguinaldo restringido
    if(esNumerico(colacion) and esNumerico(sueldo)):
        sueldo = int(sueldo)
        colacion = int(colacion)
        if(sueldo<7000000 and colacion > 100 and colacion<10000):
            prioridades_filter.append(prioridades[i])
            colaciones_filter.append(colacion)
            sueldos_base_filter.append(sueldo)
            regiones_filter.append(transformarRegiones(regiones[i]))
            contratos_filter.append(contratos[i])

        # Chequeamos si el aumento es menor al sueldo base
        

promedio_solo_aguinaldo = sum(solo_colaciones_filter) / len(solo_colaciones_filter)
desviacion_estandar = np.std(solo_colaciones_filter)
print('Promedio:',promedio_solo_aguinaldo)
print('Desviación estándar:',desviacion_estandar)
print('Cantidad de datos:',len(solo_colaciones_filter),'/',cant_datos)



#for i in range(len(solo_colaciones_filter)):
    #print(solo_colaciones_filter[i])
    #print(sueldos_base_filter[i])
    #print(prioridades_filter[i])
    #print(aguinaldos_filter[i])
    #print(regiones_filter[i])
    #print(contratos_filter[i])
    #print('')

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
yline = np.linspace(0, 10000, 1)
ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
# Prioridades, sueldo base, aumento
zdata = prioridades_filter
xdata = sueldos_base_filter
ydata = colaciones_filter

ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')
ax.set_xlabel('Sueldos base', fontsize=10)
ax.set_ylabel('Colaciones', fontsize=10)
ax.set_zlabel('Prioridades', fontsize=10)
plt.title('Analisis colaciones por sueldos base')
plt.show()




