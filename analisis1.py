import pandas as pd
import numpy as np
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

print('Ejercicio 1:')
lista_promedios = []
def calcularPromedio(texto):
    suma = 0
    cantidad = 0
    for valor in df[texto]:
        suma += valor
        cantidad += 1
    promedio = suma/cantidad
    lista_promedios.append([promedio,texto])
    #print('Promedio',texto,':', promedio)

# Promedio de prioridades
calcularPromedio('1. Sueldo Base')
calcularPromedio('2. Movilización')
calcularPromedio('3. Colación')
calcularPromedio('4. Aumento Asignación Perdida de Caja (servicio al cliente)')
calcularPromedio('5. Aguinaldo Septiembre')
calcularPromedio('6. Aguinaldo Navidad')
calcularPromedio('7. Regalo Navidad Hijo Trabajadores')
calcularPromedio('8. Beneficio Permanencia por años de Servicio')
calcularPromedio('9. Bono Vacaciones')
calcularPromedio('11. Préstamo Vacaciones')
calcularPromedio('12. Pago de los primeros 3 días en licencia médica (La primera anual)')

lista_promedios.sort(reverse=True)

for data in lista_promedios:
    print(data[1],":", data[0])


