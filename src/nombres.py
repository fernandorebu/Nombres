from collections import namedtuple
import csv

FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'año,nombre,frecuencia,genero')

def leer_frecuencias_nombres(archivo):
    lista = []
    with open(archivo, encoding='utf-8')as f:
        lector = csv.reader(f)
        next(lector)
        for año, nombre, frecuencia, genero in lector:
            año = int(año)
            frecuencia = int(frecuencia)
            FrecuenciaNombres = FrecuenciaNombre(año, nombre, frecuencia, genero)
            lista.append(FrecuenciaNombres)
    return lista


def filtra_por_genero(frecuencias, genero):
    lista = []
    for elemento in frecuencias:
        if elemento.genero == genero:
            lista.append(elemento)
    return lista


def calcula_nombres(frecuencias, genero):
    conjunto = set()
    for elemento in frecuencias:
        if(genero==None or elemento.genero == genero):
            conjunto.add(elemento.nombre)
    return conjunto


def calcula_top_nombres_de_año(frecuencias, año, n, genero):
    lista = []
    for elemento in frecuencias:
        if elemento.año == año and (genero == None or elemento.genero == genero):
            lista.append((elemento.nombre, elemento.frecuencia))
    lista.sort(key=lambda t:t[1], reverse= True)
    return lista[:n]

#lambda (funciones sin nombre), creamos una funcion sobre la marcha sin dale nommbre a la funcion
# ejemplo Key=lambda c:c[-1]   A Key siempre le metemos una función, lambda acabamos de ver que es una fucion sin nombre, en este caso tenemos elementos y nos devuelve los mismo elementos pero el ultimo caracter




def calcula_nombre_ambos_generos(frecuencias):
    m = calcula_nombres(frecuencias,'Mujer')
    h = calcula_nombres(frecuencias,'Hombre')
    Interseccion = m & h # Esto es para hacer la interseccion de ambos conjuntos
    return Interseccion


def calcula_nombres_compuestos(frecuencias, genero):
    conjunto = set()
    for elemento in frecuencias:
        if ' ' in elemento.nombre and elemento.genero == genero:
            conjunto.add(elemento.nombre)
    return conjunto


def calcular_frecuencia_media_nombre_años(frecuancias, nombre, año_ini, año_final):
    media = 0
    lista = []
    for elemento in frecuancias:
        if elemento.año >= año_ini and elemento.año < año_final and elemento.nombre == nombre:
            lista.append(elemento.frecuencia)
   
    if len(lista) == 0:
        return media 
    else:
        media = sum(lista) / len(lista)
    return media


#Esta funcion tiene un error pero no sé donde
def calcular_nombre_mas_frecuante_año_genero(frecuencias, año, genero):
    lista = []
    for elemento in frecuencias:
        if elemento.año == año and elemento.genero == genero:
            lista.append((elemento.nombre, elemento.frecuencia))
    mas_frecuente = max(lista, Key=lambda t:t[1])
    return mas_frecuente
