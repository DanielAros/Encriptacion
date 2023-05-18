import pandas as pd
import numpy as np

matriz = pd.read_excel("prueba.xlsx")
mensajeencriptado=[]

columnas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

listafinal = np.vstack([matriz[columna].tolist() for columna in columnas])

# print(listafinal)

textoplano="RESULTA"
clave="AMOSDELANOCHE"

def encriptar(texto):
    for i in range(len(texto)):    
        indicecolumna=list(matriz["A"].tolist()).index(texto[i])
        indicerenglon=list(matriz["A"].tolist()).index(clave[i])
        letraencriptada=listafinal[indicecolumna][indicerenglon]
        mensajeencriptado.append(letraencriptada)
    return "".join(mensajeencriptado)

def descencriptar(texto):
    for i in range(len(texto)):
        indicecolumna=list(matriz["A"].tolist()).index(clave[i])
        indicerenglon=list(listafinal[indicecolumna]).index(texto[i])
        letraencriptada=listafinal[0][indicerenglon]
        mensajeencriptado.append(letraencriptada)
    return "".join(mensajeencriptado)

# print(encriptar("RESULTA"))
print(descencriptar("RQGMOXL"))
