import pandas as pd
import math
import re

df = pd.read_excel("data.xlsx", index_col=0, header=0)

# Ordenamos los datos desde la columa D hasta la O (la columna M no tiene datos)
# Consideramos la prioridad 1 como la mayor y 5 como la menor

"""
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
"""


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
    print('R:', input)
    return input

# Expresión regular para identificar dígitos
def esNumerico(input):
    regex = '^[0-9]+$'
    if(re.search(regex, input) and int(input) > 100):  
        #print('F', int(input))
        print("Digit")
        return True
    else:  
        print("Not a Digit")
        return False

# Leemos la columna 2.1 (P) de movilización
aumento_movilizacion = df['2.1 Aumento Movilización']
aumento_movilizacion_filter = []
aumento_movilizacion_filter_suma = 0
aumento_movilizacion_filter_cant = 0

for valor in aumento_movilizacion:
    print('I:', valor)
    valor_str = str(valor)
    valor_str = eliminarCaracteres(valor_str)
    if(esNumerico(valor_str)):
        filtered_value = int(valor_str)
        aumento_movilizacion_filter.append(filtered_value)
        aumento_movilizacion_filter_cant += 1
        aumento_movilizacion_filter_suma += filtered_value

promedio = math.floor(aumento_movilizacion_filter_suma/aumento_movilizacion_filter_cant)
print("Promedio de aumento movilizacion con respecto a", aumento_movilizacion_filter_cant,"/",df['2.1 Aumento Movilización'].count(), "personas es: $", promedio)

print("funciona")