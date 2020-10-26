import pandas as pd
import math
import re

df = pd.read_excel("data.xlsx", index_col=0, header=0)
cant_datos = df['RUT.'].count()

# Ordenamos los datos desde la columa D hasta la O (la columna M no tiene datos)
# Consideramos la prioridad 1 como la mayor y 5 como la menor


df.sort_values(by=[
    '1. Sueldo Base', 
    '2. Movilización', 
    '3. Colación', 
    '4. Aumento Asignación Perdida de Caja (servicio al cliente)',
    '5. Aguinaldo Septiembre',
    '6. Aguinaldo Navidad',
    '7. Regalo Navidad Hijo Trabajadores',
    '8. Beneficio Permanencia por años de Servicio',
    '9. Bono Vacaciones',
    #'10. Permiso Administrativo',
    '11. Préstamo Vacaciones',
    '12. Pago de los primeros 3 días en licencia médica (La primera anual)'], 
inplace=True)
print(df)



df.sort_values(by=['2. Movilización'], inplace=True)
print(df)


# Aumento de movilización

# Descartar los que contiene % o letras
def descartarDatos(input):
    print('hello')

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

#promedio = math.floor(aumento_movilizacion_filter_suma/aumento_movilizacion_filter_cant)
#print("Promedio de aumento movilizacion con respecto a", aumento_movilizacion_filter_cant,"/",df['2.1 Aumento Movilización'].count(), "personas es: $", promedio)

print("funciona")