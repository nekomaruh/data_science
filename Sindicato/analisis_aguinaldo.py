import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import statistics
import pandas as pd
import numpy as np
import math
import re

df = pd.read_excel("data.xlsx", index_col=0, header=0)
cant_datos = df['RUT.'].count()

print('\nEjercicio aguinaldo:')

# Aumento de aguinaldos

df.sort_values(by=[
    '6. Aguinaldo Navidad'], 
inplace=True)


# Eliminar puntos y signos del input
def eliminarCaracteres(input):
    input = input.replace(".","")
    input = input.replace("$","")
    input = input.replace("-","")
    input = input.replace(" ","")
    #print('R:', input)
    return input

def int_to_Roman(num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

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
    if('R.M' in input):
        input = 'RM'
    if('METRO' in input):
        input = 'RM'
    if('POLITANA' in input):
        input = 'RM'
    if('SANTIAGO' in input):
        input = 'RM'
    if('CASA MATRIZ' in input):
        input = 'RM'
    if(esNumerico(input)):
        input = int_to_Roman(int(input))
    input = input.replace('REGION', '')
    input = input.replace('|', 'I')
    input = input.replace('l', 'I')
    input = input.replace(' ', '')
    return input

# Leemos la columna 2.1 (P) de movilización
prioridades = df['6. Aguinaldo Navidad']
aguinaldos = df['6.1 El aguinaldo de navidad, en que monto debiera quedar']
regiones = df['REGIÓN']
contratos = df['14. Duración del Contrato Colectivo']
sueldos_base = df['1.2 Tu  sueldo base actualmente es...']

solo_aguinaldos_filter = []
prioridades_filter = []
aguinaldos_filter = []
sueldos_base_filter = []
regiones_filter = []
contratos_filter = []

for i in range(cant_datos):
    # Convertimos los datos a string
    aguinaldo = str(aguinaldos[i])
    sueldo = str(sueldos_base[i])

    # Eliminamos los carácteres ? . - (espacio)
    aguinaldo = eliminarCaracteres(aguinaldo)
    sueldo = eliminarCaracteres(sueldo)

    # Solo calculamos aguinaldos
    if(esNumerico(aguinaldo)):
        solo_aguinaldo = int(aguinaldo)
        if(solo_aguinaldo > 100 and solo_aguinaldo < 200000):
            solo_aguinaldos_filter.append(solo_aguinaldo)

    # Chequeamos si el valor es numerico (no porcentaje) y con aguinaldo restringido
    if(esNumerico(aguinaldo) and esNumerico(sueldo)):
        sueldo = int(sueldo)
        aguinaldo = int(aguinaldo)
        if(sueldo<7000000 and aguinaldo > 100 and aguinaldo<200000):
            prioridades_filter.append(prioridades[i])
            aguinaldos_filter.append(aguinaldo)
            sueldos_base_filter.append(sueldo)
            regiones_filter.append(transformarRegiones(regiones[i]))
            contratos_filter.append(contratos[i])

        # Chequeamos si el aumento es menor al sueldo base
        

promedio_solo_aguinaldo = sum(solo_aguinaldos_filter) / len(solo_aguinaldos_filter)
desviacion_estandar = np.std(solo_aguinaldos_filter)
print('Promedio solo aguinaldo',promedio_solo_aguinaldo)
print('Desviación estándar',desviacion_estandar)



#for i in range(len(regiones_filter)):
    #print(solo_aguinaldos_filter[i])
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
yline = np.linspace(70000, 1, 1)
ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
# Prioridades, sueldo base, aumento
zdata = prioridades_filter
xdata = sueldos_base_filter
ydata = aguinaldos_filter

ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')
ax.set_xlabel('Sueldos base', fontsize=10)
ax.set_ylabel('Aguinaldos', fontsize=10)
ax.set_zlabel('Prioridades', fontsize=10)
plt.title('Aguinaldos de navidad por sueldos base')
plt.show()


# Segundo filtro por promedios de regiones
num_region = []
cant_aguinaldo = []
sum_aguinaldo = []
prom_region = []

for x in range(len(regiones_filter)):
    encontrado = False
    pos_encontrado = -1
    for y in range(len(num_region)):
        if(regiones_filter[x] == num_region[y]):
            encontrado = True
            pos_encontrado = y
            break
    if(encontrado):
        cant_aguinaldo[pos_encontrado] += 1
        sum_aguinaldo[pos_encontrado] += aguinaldos_filter[x]
    else:
        num_region.append(regiones_filter[x])
        cant_aguinaldo.append(1)
        sum_aguinaldo.append(aguinaldos_filter[x])

# Sacamos el promedio por region
for i in range(len(num_region)):
    prom_region.append(sum_aguinaldo[i]/cant_aguinaldo[i])



plt.bar(range(len(prom_region)), prom_region, edgecolor='black')

plt.xticks(range(len(num_region)), num_region)
plt.title("Aguinaldos por regiones")
#plt.ylim(min(regiones_filter)-1, max(regiones_filter)+1)
plt.show()


# Segundo filtro por promedios de duracion de contrato
tipo_contrato = []
cant_contrato = []
sum_contrato = []
prom_contrato = []

for x in range(len(contratos_filter)):
    encontrado = False
    pos_encontrado = -1
    for y in range(len(tipo_contrato)):
        if(contratos_filter[x] == tipo_contrato[y]):
            encontrado = True
            pos_encontrado = y
            break
    if(encontrado):
        cant_contrato[pos_encontrado] += 1
        sum_contrato[pos_encontrado] += aguinaldos_filter[x]
    else:
        tipo_contrato.append(contratos_filter[x])
        cant_contrato.append(1)
        sum_contrato.append(aguinaldos_filter[x])

# Sacamos el promedio por region
for i in range(len(tipo_contrato)):
    prom_contrato.append(sum_contrato[i]/cant_contrato[i])





plt.bar(range(len(prom_contrato)), prom_contrato, edgecolor='black')

plt.xticks(range(len(tipo_contrato)), tipo_contrato)
plt.title("Aguinaldos por contratos")
#plt.ylim(min(regiones_filter)-1, max(regiones_filter)+1)
plt.show()







