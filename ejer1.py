import pandas as pd
import numpy as np

datos={'Nombre':['Juan','Maria','Pedro','Luis','Ana','Lucia','Luisa','Luis','Luis','Luis'],
       'Edad':[25,30,35,40,45,50,55,60,65,70],
       'Altura':[1.75,1.65,1.80,1.70,1.60,1.75,1.65,1.80,1.70,1.60],
       'Peso':[70,60,80,70,60,70,60,80,70,60],
       'Sexo':['M','F','M','M','F','M','F','M','F','M'], 
       'Deportes':['Futbol','Baloncesto','Tenis','Golf','Ajedrez','Ajedrez','Ajedrez','Ajedrez','Ajedrez','Ajedrez']}

df=pd.DataFrame(datos)
print(df)
print("\n"*3)
datos2={'Nombre':['Juan','Maria','Pedro','Luis','Ana','Lucia','Luisa','Luis','Luis','Luis'],
       'Edad':[25,30,35,40,45,50,55,np.nan,65,70],
       'Sexo':['M','F','M','M','F','M','F','M','F','M'], 
       'Deportes':['Futbol','Baloncesto','Tenis','Golf','Ajedrez','Ajedrez','Ajedrez','Ajedrez','Ajedrez','Ajedrez']}
df2= pd.DataFrame(datos2)
nuevo= datos2.replace(np.nan,0)
df2= pd.DataFrame(nuevo)
print(df2)
print(df.describe())
print(df.info())
print(df2.info())