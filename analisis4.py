import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("data.xlsx", index_col=0, header=0)
cant_datos = df['RUT.'].count()

print('\nEjercicio 4:')

# Pago de gratificacion

gratificaciones = df['Como prefieres el pago de la gratifición']

cant = [0,0,0]
nombres = ['Mensual', 'Semestral', 'Anual']

for data in gratificaciones:
    if(data=='Mensual'):
        cant[0] += 1
    elif(data=='Semestral'):
        cant[1] +=1
    else:
        cant[2] += 1

print('Mensual', cant[0])
print('Semestral', cant[1])
print('Anual', cant[2])

plt.pie(cant, labels=nombres, autopct="%0.1f %%")
plt.axis("equal")
plt.show()


