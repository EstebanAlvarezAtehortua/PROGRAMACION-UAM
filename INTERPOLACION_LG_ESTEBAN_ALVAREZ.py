import numpy as np
import pandas
import math

#Se realiza la implementación de como llamar los datos que se realizaron en el archivo INTERPOLACION
datosinterpolacionL = pandas.read_csv(r'c:\Users\X415JA\Desktop\prueba unam\Datos Interpolacion L.csv', delimiter=',' , index_col="Col1")
print(datosinterpolacionL.columns)
print(datosinterpolacionL)


#Se crea una línea en donde se trabajara con los datos que se requieran interpolar, para conocer sus valores
#print(round(datosinterpolacionL.loc[55]),1)
print(datosinterpolacionL.loc[20]["Col9"])


#A partir del momento, Desplazamiento del mecanismo, sera nuestro DELTA = 20 cm.
print("Desplazamiento del mecanismo...")
desplazamiento = int(input())


#A partir del momento, Porcentaje de ciclo del mecanismo, sera el valor del Theta que queremos hallar
print("Porcentaje de ciclo del mecanismo...")
porcentaje = int(input())


#se solicita ingresar un digito establecido para hallar los valores de L, ya sea por rectitud o velocidad
print("Digite 1 si el mecanismo es optimizado por rectitud, Digite 2 si el mecanismo es optimizado por velocidad...")
optimizado = int(input())


#Se imprimiran los valores de las diferentes variables creadas anteriormente
print()
print(f"El valor desplazamiento ingresado es {desplazamiento}")
print(f"El valor porcentaje ingresado es {porcentaje}")
print(f"El metodo optimizacion ingresado es {optimizado}")
print()


#Se tomaran los datos de las demás columnas para realizar la interpolación y obtener los valores que deben tener de acuerdo a los valores suministrados

if porcentaje in datosinterpolacionL.index:
    if optimizado == 2:
        Den_L2 = (datosinterpolacionL.loc[porcentaje]["Col15"])
        Den_L1 = (datosinterpolacionL.loc[porcentaje]["Col13"])
        Den_L3 = (datosinterpolacionL.loc[porcentaje]["Col14"])

        if optimizado == 1:
            Den_L2 = (datosinterpolacionL.loc[porcentaje]["Col9"])
            Den_L1 = (datosinterpolacionL.loc[porcentaje]["Col7"])
            Den_L3 = (datosinterpolacionL.loc[porcentaje]["Col8"])
else:
    datosinterpolacionL.loc[porcentaje] = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
    baseimpar = (datosinterpolacionL.sort_index().interpolate())

    if optimizado == 1:
       Den_L2 = (baseimpar.loc[porcentaje]["Col9"])
       Den_L1 = (baseimpar.loc[porcentaje]["Col7"])
       Den_L3 = (baseimpar.loc[porcentaje]["Col8"])

    if optimizado == 2:
       Den_L2 = (baseimpar.loc[porcentaje]["Col15"])
       Den_L1 = (baseimpar.loc[porcentaje]["Col13"])
       Den_L3 = (baseimpar.loc[porcentaje]["Col14"])              


#if porcentaje in datosinterpolacionL.index:
#    print(datosinterpolacionL.loc[porcentaje]["Col1"])
#    #print(round(datosinterpolacionL.loc[55]),1)
#else:
#    datosinterpolacionL.loc[porcentaje] = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
#    print(datosinterpolacionL.sort_index().interpolate())
    


#Interpretación de las ecuaciones para obtener los delta solicitados en rectitud o velocidad

L2 = desplazamiento / Den_L2
str_L2 = str(L2)

L1 = Den_L1 * L2
str_L1 = str(L1)

L3 = Den_L3 * L2
str_L3 = str(L3)

L4 = L3
str_L4 = str(L4)

print ()
print("Valor de L1 es:" + str_L1)
print("Valor de L2 es:" + str_L2)
print("Valor de L3 es:" + str_L3)
print("Valor de L4 es:" + str_L4)
print()

        
