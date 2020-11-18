import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd
import numpy as np
import math
import re

df = pd.read_csv("Montreal.csv", index_col=0, header=0)
cant_datos = df['name'].count()

print(df['neighbourhood_group'])
