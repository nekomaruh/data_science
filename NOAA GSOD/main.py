import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd
import numpy as np
import math
import re

df = pd.read_csv("compiled_raw_y.csv")
cant_datos = df['STATION'].count()

# Eliminar las columnas que no se van a utilizar
df = df.drop(columns=['Y','Y+1','Y+2','Y+3','Y+4','Y+5','Y+6','Y+7'])

print(df.head())
print(cant_datos)