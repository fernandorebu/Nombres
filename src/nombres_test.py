from nombres import *

def test_lee_frecuencias_nombres(archivo):
    datos = leer_frecuencias_nombres(archivo)
    print(datos[:2])


def test_filtra_por_genero(frecuencias,genero ):
    datos = filtra_por_genero(frecuencias, genero)
    print(datos[:2])
    print(len(datos))

def test_calcula_nombres(frecuencias, genero):
    datos = calcula_nombres(frecuencias, genero)
    print(datos)
    print(len(datos))


def test_calcula_top_nomnbre_de_años(frecuencias, año, n , genero):
    datos = calcula_top_nombres_de_año(frecuencias, año, n , genero)
    print(datos)


def test_calcula_nombre_ambos_generos(frecuencias):
    datos = calcula_nombre_ambos_generos(frecuencias)
    print(datos)
    print(len(datos))


def test_calcula_nombres_compuestos(frecuencias, genero):
    datos = calcula_nombres_compuestos(frecuencias, genero)
    print(datos)


def test_calcular_frecuencia_media_nombre_años(frecuencias, nombre, año_ini, año_final):
    datos = calcular_frecuencia_media_nombre_años(frecuencias, nombre, año_ini, año_final)
    print(datos)


def test_calcular_nombre_mas_frecuante_año_genero(frecuencias, año, genero):
    datos = calcular_nombre_mas_frecuante_año_genero(frecuencias, año, genero)
    print(datos)



if __name__=='__main__':
    archivo = 'data/frecuencias_nombres.csv'
    genero = 'Hombre'
    año = 2002
    n= 3
    nombre ='FERNANDO'
    año_ini= 2002
    año_final= 2009
    frecuencias = leer_frecuencias_nombres(archivo)


    test_lee_frecuencias_nombres(archivo)
    #test_filtra_por_genero(frecuencias,genero)
    #test_calcula_nombres(frecuencias, genero)
    #test_calcula_top_nomnbre_de_años(frecuencias, año, n , genero)
    #test_calcula_nombre_ambos_generos(frecuencias)
    #test_calcula_nombres_compuestos(frecuencias, genero)
    #test_calcular_frecuencia_media_nombre_años(frecuencias, nombre, año_ini, año_final)
    test_calcular_nombre_mas_frecuante_año_genero(frecuencias, año, genero)