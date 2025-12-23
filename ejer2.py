import pandas as pd
import numpy as np
datos=pd.read_csv('ATP_DATA.csv', encoding='latin1')
print(datos.head())
print(datos.info())
print(datos.describe())
nuevo= pd.DataFrame(datos)
print(nuevo)
nuevo= nuevo.replace("N/A","0")
nuevo= nuevo.replace("NR","0")
print(nuevo)
print(datos.info())
print(datos.describe())


print(datos.iloc[0:5])
print(datos.iloc[[2,4,6,8,10],])
print(datos.iloc[:,[2,4,6,8,10]])
print(datos.iloc[0:5,5:8])