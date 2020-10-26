import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd
import numpy as np
import math
import re

df = pd.read_excel("data.xlsx", index_col=0, header=0)
cant_datos = df['RUT.'].count()

print('\nEjercicio bono vacaciones:')

# Aumento de colacion

df.sort_values(by=[
    '9. Bono Vacaciones'], 
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
prioridades = df['9. Bono Vacaciones']
vacaciones = df['9.1 Bono Vacaciones, cuanto debiera ser.']
regiones = df['REGIÓN']
contratos = df['14. Duración del Contrato Colectivo']
sueldos_base = df['1.2 Tu  sueldo base actualmente es...']

solo_vacaciones_filter = []
prioridades_filter = []
vacaciones_filter = []
sueldos_base_filter = []
regiones_filter = []
contratos_filter = []




for i in range(cant_datos):
    # Convertimos los datos a string
    vacacion = str(vacaciones[i])
    sueldo = str(sueldos_base[i])

    # Eliminamos los carácteres ? . - (espacio)
    vacacion = eliminarCaracteres(vacacion)
    sueldo = eliminarCaracteres(sueldo)

    # Solo calculamos aguinaldos
    if(esNumerico(vacacion)):
        solo_vacacion = int(vacacion)
        if(solo_vacacion  > 100 and solo_vacacion  <= 20000):
            solo_vacaciones_filter.append(solo_vacacion)

    # Chequeamos si el valor es numerico (no porcentaje) y con aguinaldo restringido
    if(esNumerico(vacacion) and esNumerico(sueldo)):
        sueldo = int(sueldo)
        vacacion = int(vacacion)
        if(sueldo<7000000 and vacacion > 100 and vacacion<= 20000):
            prioridades_filter.append(prioridades[i])
            vacaciones_filter.append(vacacion)
            sueldos_base_filter.append(sueldo)
            regiones_filter.append(transformarRegiones(regiones[i]))
            contratos_filter.append(contratos[i])

        # Chequeamos si el aumento es menor al sueldo base
        

promedio_solo_aguinaldo = sum(solo_vacaciones_filter) / len(solo_vacaciones_filter)
desviacion_estandar = np.std(solo_vacaciones_filter)
print(promedio_solo_aguinaldo)
print(desviacion_estandar)



for i in range(len(solo_vacaciones_filter)):
    print(solo_vacaciones_filter[i])
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
ydata = vacaciones_filter

ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')
ax.set_xlabel('Sueldos base', fontsize=10)
ax.set_ylabel('Vacaciones', fontsize=10)
ax.set_zlabel('Prioridades', fontsize=10)
plt.title('Aguinaldos de navidad por sueldos base')
plt.show()




