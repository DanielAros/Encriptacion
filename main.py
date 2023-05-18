import pandas as pd
import numpy as np

matriz = pd.read_excel("prueba.xlsx")

columnas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

listafinal = np.vstack([matriz[columna].tolist() for columna in columnas])


parrafo = "RESULTA QUE EL REY A SUS CINCUENTA Y SIETE ANOS TENIA UN DEFECTILLO BASTANTE MOLESTO NO SE CALLABA NI DEBAJO DEL AGUA YA FUERA DE DIA O DE NOCHE SIEMPRE TENIA ALGO QUE DECIR Y ENLAZABA UNOS TEMAS CON OTROS CON UNA FACILIDAD PASMOSA"
parrafoEncriptado = "RQGMOXL QGS EX RQM A SGG CUBUXIYTN Y SUSLH AZCK TQBAD UZ DQTWFXTLYC BMGLDREE MAZWVXZ NA SQ CMZDDFL NU DQPSMS DQZ ASIS YM FGSJD DQ DUO O DQ NAQZH SUSESVP TQBAD AXUG QGS DQQAU Y EZZSCEMA UZCK TQASV CAB OFFGV CAB UZO FMQAOMOAQ PMGERWL"
# textoplano="RESULTA"
clave="AMOSDELANOCHE"

def encriptar(texto):
    mensajeencriptado=[]
    for i in range(len(texto)):    
        indicecolumna=list(matriz["A"].tolist()).index(texto[i])
        indicerenglon=list(matriz["A"].tolist()).index(clave[i])
        letraencriptada=listafinal[indicecolumna][indicerenglon]
        mensajeencriptado.append(letraencriptada)
    return "".join(mensajeencriptado)

def descencriptar(texto):
    mensajeencriptado=[]
    for i in range(len(texto)):
        indicecolumna=list(matriz["A"].tolist()).index(clave[i])
        indicerenglon=list(listafinal[indicecolumna]).index(texto[i])
        letraencriptada=listafinal[0][indicerenglon]
        mensajeencriptado.append(letraencriptada)
    return "".join(mensajeencriptado)

def encriptarDescencriptar(parrafo, metodo):
    arrayPalabras = parrafo.split()
    palabras = []

    if(metodo == 'encriptar'):
        for i in range(len(arrayPalabras)):
            palabra = encriptar(arrayPalabras[i])
            palabras.append(palabra)
        palabrasEncriptadas = " ".join(palabras)
        print(palabrasEncriptadas)
    else:
        for i in range(len(arrayPalabras)):
            palabra = descencriptar(arrayPalabras[i])
            palabras.append(palabra)
        palabrasDescencriptadas = " ".join(palabras)
        print(palabrasDescencriptadas)
    
    

# print(encriptar("RESULTA"))
# print(descencriptar("RQGMOXL"))
# encriptarDescencriptar(parrafo, 'encriptar')
encriptarDescencriptar(parrafoEncriptado, 'descencriptar')
